/* 777 for ALS — interactions */
(function () {
  "use strict";

  /* ---------- Mobile nav ---------- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.classList.toggle("open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        links.classList.remove("open");
        toggle.classList.remove("open");
      });
    });
  }

  /* ---------- Header background on scroll ---------- */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (!header) return;
    if (window.scrollY > 30) header.classList.add("scrolled");
    else header.classList.remove("scrolled");
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Scroll reveal ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && revealEls.length) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("in");
            io.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }
    );
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Custom countdown ---------- */
  var cd = document.getElementById("countdown");
  if (cd) {
    // First marathon of the 2027 World Marathon Challenge — Antarctica, Jan 30 2027
    var target = new Date(cd.getAttribute("data-target") || "2027-01-30T00:00:00").getTime();
    var units = [
      { id: "cd-days", label: "Days" },
      { id: "cd-hours", label: "Hours" },
      { id: "cd-mins", label: "Minutes" },
      { id: "cd-secs", label: "Seconds" }
    ];
    // build markup
    cd.innerHTML = units.map(function (u) {
      return '<div class="cd-unit"><div class="cd-unit__num" id="' + u.id + '">00</div>' +
             '<div class="cd-unit__lbl">' + u.label + '</div></div>';
    }).join("");
    function pad(n) { return (n < 10 ? "0" : "") + n; }
    function tick() {
      var diff = target - Date.now();
      if (diff < 0) diff = 0;
      var d = Math.floor(diff / 86400000);
      var h = Math.floor((diff % 86400000) / 3600000);
      var m = Math.floor((diff % 3600000) / 60000);
      var s = Math.floor((diff % 60000) / 1000);
      document.getElementById("cd-days").textContent = d;
      document.getElementById("cd-hours").textContent = pad(h);
      document.getElementById("cd-mins").textContent = pad(m);
      document.getElementById("cd-secs").textContent = pad(s);
    }
    tick();
    setInterval(tick, 1000);
  }

  /* ---------- Lite video embeds (custom poster -> load player on click) ---------- */
  document.querySelectorAll(".video-lite").forEach(function (box) {
    box.addEventListener("click", function () {
      var src = box.getAttribute("data-src");
      if (!src) return;
      var iframe = document.createElement("iframe");
      iframe.setAttribute("src", src);
      iframe.setAttribute("allow", "autoplay; fullscreen");
      iframe.setAttribute("allowfullscreen", "");
      iframe.setAttribute("title", box.getAttribute("data-title") || "Video");
      box.innerHTML = "";
      box.classList.remove("video-lite");
      box.appendChild(iframe);
    });
  });

  /* ---------- Footer year ---------- */
  var yr = document.getElementById("year");
  if (yr) yr.textContent = new Date().getFullYear();
})();
