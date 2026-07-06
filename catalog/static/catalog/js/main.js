(function () {
  "use strict";

  var tabs = document.querySelectorAll(".rail-tab");
  var panels = document.querySelectorAll(".panel");

  function activate(brandSlug) {
    tabs.forEach(function (tab) {
      var isActive = tab.getAttribute("data-brand") === brandSlug;
      tab.classList.toggle("is-active", isActive);
      tab.setAttribute("aria-selected", isActive ? "true" : "false");
    });
    panels.forEach(function (panel) {
      panel.classList.toggle("is-active", panel.getAttribute("data-panel") === brandSlug);
    });
  }

  tabs.forEach(function (tab) {
    tab.addEventListener("click", function () {
      activate(tab.getAttribute("data-brand"));
    });
  });
})();
