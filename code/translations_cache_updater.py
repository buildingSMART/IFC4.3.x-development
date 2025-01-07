import os
import time
import requests
import subprocess

CROWDIN_REPO_DIR = os.environ.get('CROWDIN_REPO_DIR', '/crowdin_repository')  
TRANSLATION_DIR = os.environ.get('TRANSLATION_DIR', '/ifc_translations')  
TRANSLATIONS_CHECK_INTERVAL = int(os.environ.get('TRANSLATIONS_CHECK_INTERVAL', 86400))  # Default to 24h

BRANCH_NAME = "translations"


def update_repository(latest_commit):
    try:
        subprocess.run(["git", "-C", CROWDIN_REPO_DIR, "reset", "--hard", latest_commit], check=True)
        print(f"Repository updated to commit {latest_commit}")
    except subprocess.CalledProcessError as e:
        print(f"Error updating repository: {e}")


def copy_translations():
    source_dir = os.path.join(CROWDIN_REPO_DIR, "translations")
    target_dir = os.path.join(TRANSLATION_DIR, "translations")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    try:
        print(f"Copying translations from {source_dir} to {target_dir}...")
        if os.path.exists(source_dir):
            subprocess.run(["cp", "-r", source_dir, '/tmp/translations'], check=True)
            print("Translations copied successfully.")
        else:
            print(f"Source directory {source_dir} does not exist.")
    except Exception as e:
        print(f"Error copying translations: {e}")
        raise


def refresh_cache():
    try:
        subprocess.run(["wget", "-q", "--recursive", "--spider", "-S", "http://localhost:5000"], check=True)
        response = requests.post("http://localhost:5000/build_index")
        subprocess.call("redis-cli shutdown".split(" "))
        if response.status_code == 200:
            print("Cache refreshed successfully.")
        else:
            print(f"Failed to refresh cache: {response.status_code}")
    except Exception as e:
        print(f"Error refreshing cache: {e}")


def main():
    
    while True:
        current_commit = subprocess.check_output(["git", "-C", CROWDIN_REPO_DIR, "rev-parse", "HEAD"]).strip().decode('utf-8')
        subprocess.run(["git", "-C", CROWDIN_REPO_DIR, "fetch"], check=True)
        latest_commit = subprocess.check_output(["git", "-C", CROWDIN_REPO_DIR, "rev-parse", f"origin/{BRANCH_NAME}"]).strip().decode('utf-8')
                
        if (
        (current_commit and latest_commit and current_commit != latest_commit) or
        not all(os.path.exists(os.path.join(TRANSLATION_DIR, folder)) for folder in ['types', 'entities', 'properties'])
        ):
            print(f"New commit {latest_commit} detected. Updating repository...")
            update_repository(latest_commit)
            copy_translations()
            refresh_cache()
        else:
            print("No new commits.")

        time.sleep(TRANSLATIONS_CHECK_INTERVAL)

if __name__ == "__main__":
    main()
