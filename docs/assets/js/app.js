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
    Array.from(content.getElementsByTagName('h2')).forEach((h2) => {
        let href = null;
        Array.from(h2.getElementsByTagName('a')).forEach((anchor) => {
            if (anchor.getAttribute('href')) {
                href = anchor.getAttribute('href');
            }
        });
        if (href) {
            let name = h2.textContent.trim();
            let number = name.split(' ', 1)[0];
            if (name == number) {
                number = '';
            } else {
                name = name.substring(number.length);
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
    if (ol.getElementsByTagName('li').length) {
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

fetch(`https://api.github.com/repos/${window.appconfig.repo}/commits?path=${window.appconfig.path}`).then(r => r.json()).then(j => {
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

makeHeadersCollapsible();
generateSectionNavigation();
initialiseBackToTopButton();
feather.replace();
