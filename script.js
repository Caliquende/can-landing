/* can.is-a.dev — bilingual landing page
   English is the default language; TR/EN buttons swap every translated
   string, the document metadata and the html lang/data-language flags. */

(function () {
  "use strict";

  var STRINGS = {
    en: {
      title: "Hamdi Can Ernalbantoğulları — QA Engineer & SDET",
      metaDesc:
        "QA Engineer with 3+ years of Smart TV software testing at Vestel. Manual, regression and test automation with Python, Selenium, Pytest and Playwright.",
      ogTitle: "Hamdi Can Ernalbantoğulları — QA Engineer & SDET",
      ogDesc:
        "QA Engineer with 3+ years of Smart TV QA at Vestel. Test automation with Python, Selenium, Pytest, Playwright.",
      skip: "Skip to content",
      navLabel: "Primary navigation",
      langLabel: "Language selection",
      navExperience: "Experience",
      navProjects: "Projects",
      navContact: "Contact",
      open: "Open to QA, Test Automation & SDET roles",
      role: "Software QA · Test Engineer · SDET",
      pitch:
        "I help teams ship reliable software through structured testing, clear defect reporting and practical automation.",
      cv: "Download CV",
      contact: "Get in touch",
      stat1n: "4,000+",
      stat1d: "defect records handled in Jira",
      stat2n: "150+",
      stat2d: "mass-production & field issues investigated",
      stat3n: "9",
      stat3d: "Smart TV projects validated (+20 variants)",
      stat4n: "3+",
      stat4d: "years in software QA",
      expTitle: "Experience",
      exp1org: "Vestel Electronics",
      exp1date: "Nov 2022 – Nov 2025",
      exp1role: "R&D TV Software Design Verification Test & QA Engineer",
      exp1i1: "Functional and regression testing of Smart TV software features",
      exp1i2: "Designed and maintained test scenarios from requirements",
      exp1i3: "Reported, tracked and validated defects in Jira",
      exp1i4: "Worked side by side with developers on issue analysis",
      exp2org: "Vestel Electronics",
      exp2date: "Jul 2021 – Nov 2022",
      exp2role: "LED-Wall System Design Engineer",
      exp2i1: "Product development for LED display systems",
      exp2i2: "R&D discipline, system thinking, cross-functional work",
      earlier:
        "Earlier: Embedded Software Design Intern (DVLX) · R&D Intern Engineer (ESINOTEK)",
      refs: "References",
      refNote: "Professional and academic references available upon request.",
      skillsTitle: "Toolbox",
      projTitle: "Projects",
      proj1d:
        "API tests (Requests/Pytest) and UI tests (Selenium, Page Object Model) with CI on GitHub Actions.",
      proj2d:
        "LLM-assisted trading bot with risk controls, regime detection and Telegram reports.",
      proj3d:
        "Local-first research app bridging Android and NotebookLM via FastAPI.",
      proj4d:
        "Offline-first Windows disk auditor built with Python, FastAPI and pywebview.",
      proj5d:
        "Bilingual multi-seller marketplace demo in React + TypeScript with role dashboards.",
      qa: "This page is tested too — Pytest, Playwright and Selenium check loading, navigation, both languages, metadata and layouts.",
      contactLabel: "contact",
      ctaTitle: "Let's build something that doesn't break.",
      emailLabel: "Email"
    },
    tr: {
      title: "Hamdi Can Ernalbantoğulları — QA Mühendisi & SDET",
      metaDesc:
        "Vestel'de 3+ yıl Smart TV yazılım testi deneyimine sahip QA Mühendisi. Python, Selenium, Pytest ve Playwright ile manuel, regresyon ve test otomasyonu.",
      ogTitle: "Hamdi Can Ernalbantoğulları — QA Mühendisi & SDET",
      ogDesc:
        "Vestel'de 3+ yıl Smart TV QA deneyimine sahip QA Mühendisi. Python, Selenium, Pytest ve Playwright ile test otomasyonu.",
      skip: "İçeriğe geç",
      navLabel: "Birincil navigasyon",
      langLabel: "Dil seçimi",
      navExperience: "Deneyim",
      navProjects: "Projeler",
      navContact: "İletişim",
      open: "QA, Test Otomasyonu ve SDET pozisyonlarına açığım",
      role: "Yazılım QA · Test Mühendisi · SDET",
      pitch:
        "Yapılandırılmış testler, net hata raporları ve pratik otomasyonla ekiplerin güvenilir yazılım çıkarmasına yardımcı oluyorum.",
      cv: "CV İndir",
      contact: "İletişime geç",
      stat1n: "4.000+",
      stat1d: "Jira'da ele alınan hata kaydı",
      stat2n: "150+",
      stat2d: "incelenen üretim ve saha sorunu",
      stat3n: "9",
      stat3d: "doğrulanan Smart TV projesi (+20 varyant)",
      stat4n: "3+",
      stat4d: "yıl yazılım QA deneyimi",
      expTitle: "Deneyim",
      exp1org: "Vestel Elektronik",
      exp1date: "Kas 2022 – Kas 2025",
      exp1role: "Ar-Ge TV Yazılım Tasarım Doğrulama Test ve QA Mühendisi",
      exp1i1:
        "Smart TV yazılım özelliklerinin fonksiyonel ve regresyon testleri",
      exp1i2: "Gereksinimlerden test senaryoları tasarlama ve güncel tutma",
      exp1i3: "Jira ile hata raporlama, takip ve doğrulama",
      exp1i4: "Geliştiricilerle birlikte hata analizi",
      exp2org: "Vestel Elektronik",
      exp2date: "Tem 2021 – Kas 2022",
      exp2role: "LED-Wall Sistem Tasarım Mühendisi",
      exp2i1: "LED ekran sistemleri için ürün geliştirme",
      exp2i2: "Ar-Ge disiplini, sistem düşüncesi, ekipler arası çalışma",
      earlier:
        "Önce: Gömülü Yazılım Tasarım Stajyeri (DVLX) · Ar-Ge Stajyer Mühendis (ESINOTEK)",
      refs: "Referanslar",
      refNote: "Profesyonel ve akademik referanslar talep üzerine paylaşılır.",
      skillsTitle: "Araç kutusu",
      projTitle: "Projeler",
      proj1d:
        "Requests/Pytest ile API, Selenium + Page Object Model ile UI testleri; GitHub Actions CI.",
      proj2d:
        "Risk kontrolleri, piyasa rejimi tespiti ve Telegram raporlu LLM destekli bot.",
      proj3d:
        "FastAPI ile Android'i NotebookLM'e bağlayan yerel öncelikli araştırma uygulaması.",
      proj4d:
        "Python, FastAPI ve pywebview ile çevrimdışı çalışan Windows disk denetçisi.",
      proj5d:
        "React + TypeScript ile çift dilli, çok satıcılı pazar yeri demosu.",
      qa: "Bu sayfa da test ediliyor — Pytest, Playwright ve Selenium yüklemeyi, gezinmeyi, iki dili, metadata'yı ve düzenleri kontrol ediyor.",
      contactLabel: "iletişim",
      ctaTitle: "Bozulmayan bir şey inşa edelim.",
      emailLabel: "E-posta"
    }
  };

  var DEFAULT_LANGUAGE = "en";
  var root = document.documentElement;

  function applyLanguage(language) {
    var strings = STRINGS[language];

    if (!strings) {
      return;
    }

    document.querySelectorAll("[data-i18n]").forEach(function (element) {
      var key = element.getAttribute("data-i18n");

      if (Object.prototype.hasOwnProperty.call(strings, key)) {
        element.textContent = strings[key];
      }
    });

    document.querySelectorAll("[data-i18n-aria]").forEach(function (element) {
      var key = element.getAttribute("data-i18n-aria");

      if (Object.prototype.hasOwnProperty.call(strings, key)) {
        element.setAttribute("aria-label", strings[key]);
      }
    });

    document.querySelectorAll("[data-i18n-content]").forEach(function (element) {
      var key = element.getAttribute("data-i18n-content");

      if (Object.prototype.hasOwnProperty.call(strings, key)) {
        element.setAttribute("content", strings[key]);
      }
    });

    root.setAttribute("lang", language);
    root.setAttribute("data-language", language);

    document.querySelectorAll("[data-lang]").forEach(function (button) {
      button.setAttribute(
        "aria-pressed",
        String(button.getAttribute("data-lang") === language)
      );
    });
  }

  document.querySelectorAll("[data-lang]").forEach(function (button) {
    button.addEventListener("click", function () {
      applyLanguage(button.getAttribute("data-lang"));
    });
  });

  applyLanguage(DEFAULT_LANGUAGE);
})();
