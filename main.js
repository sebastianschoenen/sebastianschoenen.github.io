(function () {
  // Tabs in the Innovation section
  var tabs = document.querySelectorAll('.tab-btn');
  tabs.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var id = btn.getAttribute('data-tab');
      document.querySelectorAll('.proj-group').forEach(function (g) {
        var on = g.id === 'tab-' + id;
        g.classList.toggle('visible', on);
        g.hidden = !on;
      });
      tabs.forEach(function (b) {
        var active = b === btn;
        b.classList.toggle('active', active);
        b.setAttribute('aria-selected', active ? 'true' : 'false');
      });
    });
  });

  // Mobile menu
  var hamburger = document.getElementById('hamburger');
  var mobileMenu = document.getElementById('mobileMenu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function () {
      var open = mobileMenu.classList.toggle('open');
      hamburger.classList.toggle('open', open);
      hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    mobileMenu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
      });
    });
  }
})();
