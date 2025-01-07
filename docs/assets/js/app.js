function renderToggleIcon(element) {
    let icons = element.getElementsByClassName('toggle-icon');
    if (icons.length) {
        icons[0].remove();
    }

    let a = document.createElement('a');
    a.classList.add('toggle-icon');
    element.prepend(a);
    if (element.classList.contains('collapsed')) {
        a.innerHTML = feather.icons['chevron-up'].toSvg();
    } else {
        a.innerHTML = feather.icons['chevron-down'].toSvg();
    }
}

function refreshCollapsed(element) {
    let hide = element.classList.contains('collapsed');
    renderToggleIcon(element);

    let headerLevel = element.tagName.slice(-1);
    let sibling = element.nextElementSibling;
    while (sibling) {
        if (sibling.tagName.slice(0, 1) == 'H' && sibling.tagName.slice(-1) <= headerLevel)  {
            break;
        }
        sibling.style.display = hide ? 'none' : '';
        sibling = sibling.nextElementSibling;
    }
}

function makeHeadersCollapsible() {
    let elements = document.querySelectorAll('h2, h3, h4, h5, h6');
    for (let i=0; i<elements.length; i++) {
        let element = elements[i];
        renderToggleIcon(element);
        refreshCollapsed(element);

        element.onclick = function(e) {
            let target = e.target;
            if (target.classList.contains('feather-link')) {
                return;
            }
            while (target.tagName.slice(0, 1) != "H") {
                target = target.parentNode;
            }
            target.classList.toggle('collapsed');
            refreshCollapsed(target);
        }
    }
}

function generateSectionNavigation() {
    let content = document.getElementById('main-content');
    let nav = document.getElementById('section-navigation');
    let ol = nav.getElementsByTagName('ol')[0];
    Array.from(document.querySelectorAll('h2, h3, h4, h5, h6')).forEach((h2) => {
        let href = null;
        Array.from(h2.getElementsByTagName('a')).forEach((anchor) => {
            if (anchor.getAttribute('href')) {
                href = anchor.getAttribute('href');
            }
        });
        if (href) {
            let name = h2.textContent.trim();
            let subDivs = Array.from(h2.children).filter(el => el.tagName.toLowerCase() === "div");
            let number;
            if (subDivs.length === 2 && subDivs[0].className === 'number') {
                // terms and cond
                [number, name] = subDivs.map(el => el.textContent);
            } else if (h2.tagName.toLowerCase() === 'h2') {
                number = name.split(' ', 1)[0];
                if (name == number || ! /\d/.test(number)) {
                    number = '';
                } else {
                    name = name.substring(number.length);
                }
            } else {
                // to keep behaviour as before we only process h3+ on Ch 3.
                return;
            }
            

            li = document.createElement('li');
            li.setAttribute('number', number);
            a = document.createElement('a');
            a.setAttribute('href', href);
            a.textContent = name;
            li.append(a);
            ol.append(li);
        }
    });
    if (ol.getElementsByTagName('li').length > 1) {
        nav.classList.remove('hidden');
    }
}


function initialiseBackToTopButton() {
    let backToTop = document.getElementById('back-to-top');

    window.onscroll = function() {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                backToTop.style.display = "block";
            } else {
                backToTop.style.display = "none";
        }
    };

    backToTop.addEventListener('click', function() {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
    });
}

function setupInheritanceToggle() {
    let showElements = document.getElementsByClassName('show-inherited');
    let hideElements = document.getElementsByClassName('hide-inherited');

    function refreshInheritanceDisplay(type, showInherited) {
        let inheritedRows = document.getElementsByClassName('inherited');
        for (let i=0; i<inheritedRows.length; i++) {
            if (inheritedRows[i].getAttribute('data-type') == type) {
                inheritedRows[i].style.display = showInherited ? 'table-row' : 'none';
            }
        }
        for (let i=0; i<showElements.length; i++) {
            if (showElements[i].getAttribute('data-type') == type) {
                showElements[i].style.display = showInherited ? 'none' : 'block';
            }
        }
        for (let i=0; i<hideElements.length; i++) {
            if (hideElements[i].getAttribute('data-type') == type) {
                hideElements[i].style.display = showInherited ? 'block' : 'none';
            }
        }
    }

    for (let i=0; i<showElements.length; i++) {
        showElements[i].addEventListener('click', function() {
            refreshInheritanceDisplay(showElements[i].getAttribute('data-type'), true);
        });
    }

    for (let i=0; i<hideElements.length; i++) {
        hideElements[i].addEventListener('click', function() {
            refreshInheritanceDisplay(showElements[i].getAttribute('data-type'), false);
        });
    }

    refreshInheritanceDisplay('attribute', false);
    refreshInheritanceDisplay('concept', false);
}

function setupMathJax() {
    window.MathJax = {
        loader: {
            load: ['output/svg']
        },
        startup: {
            output: 'svg',
        },
    };
}

function setupHighlightJS() {
    hljs.registerLanguage("express", (function(e) {
        var s = e.COMMENT("#", "$");
        return {
            aliases: ["robotstxt", "robots.txt"],
            case_insensitive: !0,
            lexemes: "[a-z-]+",
            keywords: {
                // I actually didn't check what these are I just did trial and error until I liked the colours
                section: "ENTITY END_ENTITY TYPE END_TYPE FUNCTION END_FUNCTION LOCAL END_LOCAL BEGIN END IF THEN ELSE END_IF REPEAT END_REPEAT CASE END_CASE OTHERWISE RULE END_RULE SCHEMA END_SCHEMA",
                built_in: "OPTIONAL NOT OR EXISTS SET SIZEOF SELF TYPEOF AND IN ONEOF LIST QUERY ARRAY INTEGER LOGICAL HIINDEX NVL STRING REAL BINARY",
                keyword: "SUBTYPE OF WHERE ENUMERATION ABSTRACT SUPERTYPE INVERSE FOR TO RETURN DERIVE UNIQUE FIXED"
            }
        }
    }));
    // HighlightJS does not support HTML inside highlighted code:
    // https://github.com/highlightjs/highlight.js/wiki/security
    // This hook selectively allows links.
    const link_regex = /<a href="(.*?)">(\w+?)<\/a>/g;
    const anchor_regex = /#(\d+)/g;
    const id_regex = /#(\d+)(\W*=)/g;
    const fakelink_regex = /{{(.*?):(\w+?)}}/g;
    const fakeanchor_regex = /\[\[anchor(\d+):anchor(\d+)\]\]/g;
    const fakeid_regex = /\[\[id(\d+):id(\d+)\]\]/g;
    hljs.addPlugin({
        'before:highlightElement': ({ el, language }) => {
            let result = '';
            el.innerHTML = el.innerHTML.replace(link_regex, '{{$1:$2}}');
            if (language == "step21") {
                el.innerHTML = el.innerHTML.replace(id_regex, '[[id$1:id$1]]$2');
                el.innerHTML = el.innerHTML.replace(anchor_regex, '[[anchor$1:anchor$1]]');
            }
            console.log(language);
        },
        'after:highlightElement': ({ el, result }) => {
            el.innerHTML = el.innerHTML.replace(fakelink_regex, '<a href="$1">$2</a>')
            el.innerHTML = el.innerHTML.replace(fakeanchor_regex, '<a href="#$1">#$2</a>')
            el.innerHTML = el.innerHTML.replace(fakeid_regex, '<a id="$1"></a><span class="hljs-symbol">#$2</span>')
        }
    });
    hljs.highlightAll();
    hljs.initLineNumbersOnLoad();
}



document.addEventListener('DOMContentLoaded', (event) => {
Array.from(document.querySelectorAll('a')).concat(Array.from(document.querySelectorAll('em'))).forEach((a) => {
    let popup = null;
    let timeout = null;
    let onElem = false;
    let onPopup = false;

    let clearPopup = () => {
        if (onElem || onPopup) {
            return false;
        }
        if (popup) {
            document.body.removeChild(popup);
        }
        popup = null;
    };

    let soonClearPopup = () => {
        setTimeout(clearPopup, 1000.);
    };

    let showPopup = () => {
        if (!onElem) {
            return false;
        }
        fetch('/api/v0/resource/' + a.innerText).then(r => r.json()).then(data => {
            if (popup) {
                onElem = true;
                return;
            }
            popup = document.createElement('div');
            h1 = document.createElement('h1');
            p = document.createElement('div');
            table = document.createElement('table');
            h1.appendChild(document.createTextNode(data.resource));
            p.innerHTML = data.definition;
            data.attributes.forEach(a => {
                tr = document.createElement('tr');
                let inv = false;
                a.forEach((c,i) => {
                    if (i === 0 && c === '') {
                        inv = true;
                    } else if (i === 3) {
                        // don't add definition
                        return;
                    }
                    td = document.createElement('td');
                    tr.appendChild(td)
                    if (inv) {
                        ii = document.createElement('i');
                        ii.style.opacity = 0.7;
                        td.appendChild(ii);
                        td = ii;
                    }
                    td.appendChild(document.createTextNode(c));
                });
                table.appendChild(tr)
            });
            popup.className = 'popup';
            popup.appendChild(h1);
            popup.appendChild(p);
            popup.appendChild(table);
            document.body.appendChild(popup);

            popup.onmouseenter = () => {
                onPopup = true;
            }

            popup.onmouseleave = () => {
                onPopup = false;
                soonClearPopup();
            };

            let rect = a.getBoundingClientRect();
            popup.style.left = ((rect.left + rect.right) / 2. - 250 + window.scrollX) + 'px';
            popup.style.top = (rect.bottom + 10. + window.scrollY) + 'px';
        });
    }

    let soonShowPopup = () => {
        timeout = setTimeout(showPopup, 1000.);
    };

    a.onmouseenter = () => {
        onElem = true;
        soonShowPopup();
    };

    a.onmouseleave = () => {
        onElem = false;
        soonClearPopup();
        clearTimeout(timeout);
    };

});

if (!window.is_iso) {
fetch(`https://api.github.com/repos/${window.appconfig.repo}/commits?path=${window.appconfig.path}`).then(r => r.json()).then(j => {
    if (document.getElementById('contributors') === null) {
        return;
    }
    let n = {};
    j.forEach(c => {
        n[c.author.avatar_url] = (n[c.author.avatar_url || 0]) + 1;
    });
    let es = Object.entries(n);
    document.getElementById('contributors').appendChild(
        document.createTextNode(es.length + ' contributor(s): ')
    );
    es.map(kv => [kv[1], kv[0]]).sort().forEach(kv => {
        let img = document.createElement('img');
        img.src = kv[1] + '&s=32';
        img.classList.add('contributor-icon');
        document.getElementById('contributors').appendChild(img);
    });
    document.getElementById('last-change').innerHTML += 'Last change: ' +
    '<em>' + j[0].commit.message + '</em>' + ' by ' + j[0].commit.author.name + ' on ' + (new Date(j[0].commit.author.date)).toLocaleString();
});
}

setupMathJax();
setupHighlightJS();
setupInheritanceToggle();
if (!document.body.classList.contains('terms-and-definitions') && !document.body.classList.contains('cover')) {
    makeHeadersCollapsible();
}
generateSectionNavigation();
initialiseBackToTopButton();
feather.replace();

});

function getCookie(name) {
    var value = `; ${document.cookie}`;
    var parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

document.addEventListener("DOMContentLoaded", () => {
    const languagePreference = getCookie('languagePreference') || 'English_UK';
    console.log("Language Preference:", languagePreference);

    const activeTranslations = document.querySelectorAll(`.lang-${languagePreference}`);
    console.log("Active translations found:", activeTranslations.length);

    activeTranslations.forEach((translation) => {
        console.log("Setting display:block for:", translation.className);
        translation.style.display = 'block';
    });
});


function setLanguagePreference(value) {
    let languageMapping = {
        "English_UK": "English (UK)",
        "English": "English",
        "Arabic": "Arabic",
        "Czech": "Czech",
        "Danish": "Danish",
        "German": "German",
        "Spanish": "Spanish",
        "Finnish": "Finnish",
        "French": "French",
        "Hindi": "Hindi",
        "Croatian": "Croatian",
        "Icelandic": "Icelandic",
        "Italian": "Italian",
        "Japanese": "Japanese",
        "Korean": "Korean",
        "Lithuanian": "Lithuanian",
        "Dutch": "Dutch",
        "Norwegian": "Norwegian",
        "Polish": "Polish",
        "Portuguese": "Portuguese",
        "Portuguese_Brazilian": "Portuguese (Brazilian)",
        "Romanian": "Romanian",
        "Slovenian": "Slovenian",
        "Swedish": "Swedish",
        "Turkish": "Turkish",
        "ChineseSimplified": "Chinese (Simplified)"
    };

    var date = new Date();
    date.setTime(date.getTime() + (30 * 24 * 60 * 60 * 1000));  // Cookie expires in 30 days
    var expires = "; expires=" + date.toUTCString();

    document.cookie = `languagePreference=${value}${expires}; path=/;`;
    location.reload();
}