Array.from(document.querySelectorAll("h3")).forEach(n => {
  n.onclick = function(evt) {
    elem = evt.target.nextElementSibling;
    var hide = evt.target.classList.toggle('collapsed');
    while (elem) {
      elem.style.display = hide ? 'none' : '';
      elem = elem.nextElementSibling;
      if (elem.tagName == evt.target.tagName) {
        break;
      }
    }
  }
});
