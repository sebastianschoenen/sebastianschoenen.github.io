(function () {
  document.documentElement.classList.add('js');

  // Tabs in the Innovation section
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab-btn'));
  function activate(btn) {
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
        b.setAttribute('tabindex', active ? '0' : '-1');
      });
      reveal();
  }
  tabs.forEach(function (btn, i) {
    btn.setAttribute('tabindex', btn.classList.contains('active') ? '0' : '-1');
    btn.addEventListener('click', function () { activate(btn); });
    btn.addEventListener('keydown', function (e) {
      var next = null;
      if (e.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
      if (e.key === 'ArrowLeft') next = tabs[(i - 1 + tabs.length) % tabs.length];
      if (e.key === 'Home') next = tabs[0];
      if (e.key === 'End') next = tabs[tabs.length - 1];
      if (next) { e.preventDefault(); activate(next); next.focus(); }
    });
  });

  // Reveal cards on scroll
  var io = null;
  function reveal() {
    var items = document.querySelectorAll('.reveal:not(.in)');
    if (!('IntersectionObserver' in window)) { items.forEach(function (el) { el.classList.add('in'); }); return; }
    if (!io) {
      io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    }
    items.forEach(function (el) { if (el.offsetParent !== null) io.observe(el); });
  }
  reveal();
  // Safety net: anything already scrolled past is shown immediately
  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () {
      document.querySelectorAll('.reveal:not(.in)').forEach(function (el) {
        if (el.getBoundingClientRect().bottom < 0) el.classList.add('in');
      });
      ticking = false;
    });
  }, { passive: true });

  // Active section in navigation
  var navLinks = document.querySelectorAll('.nav-links a[data-section]');
  if (navLinks.length && 'IntersectionObserver' in window) {
    var current = null;
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) current = en.target.id; });
      navLinks.forEach(function (a) { a.classList.toggle('active', a.getAttribute('data-section') === current); });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
    navLinks.forEach(function (a) { var sec = document.getElementById(a.getAttribute('data-section')); if (sec) so.observe(sec); });
  }

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
