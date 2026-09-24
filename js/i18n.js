(function() {
    'use strict';

    var currentLang = localStorage.getItem('smartEduLang') || 'en';
    var translations = {};

    var SUPPORTED_LANGS = {
        en: { name: 'English', flag: 'images/flags/uk.png' },
        fr: { name: 'Français', flag: 'images/flags/france.png' }
    };

    function loadTranslations(lang, callback) {
        fetch('lang/' + lang + '.json')
            .then(function(response) { return response.json(); })
            .then(function(data) {
                translations[lang] = data;
                if (callback) callback();
            })
            .catch(function() {
                if (callback) callback();
            });
    }

    function getTranslation(key) {
        var langData = translations[currentLang];
        if (!langData) return null;
        var parts = key.split('.');
        var value = langData;
        for (var i = 0; i < parts.length; i++) {
            if (value == null || typeof value !== 'object') return null;
            value = value[parts[i]];
        }
        return typeof value === 'string' ? value : null;
    }

    function applyTranslations() {
        if (!translations[currentLang]) return;

        var elements = document.querySelectorAll('[data-i18n]');
        elements.forEach(function(el) {
            var key = el.getAttribute('data-i18n');
            var translation = getTranslation(key);
            if (translation) {
                var html = translation;
                var map = {};
                var match;
                var regex = /\{\{(\w+)\}\}/g;
                while ((match = regex.exec(translation)) !== null) {
                    map[match[1]] = el.getAttribute('data-i18n-' + match[1]) || '';
                }
                for (var placeholder in map) {
                    html = html.replace(new RegExp('{{' + placeholder + '}}', 'g'), map[placeholder]);
                }
                el.innerHTML = html;
            }
        });

        document.querySelectorAll('[data-i18n-title]').forEach(function(el) {
            var key = el.getAttribute('data-i18n-title');
            var value = getTranslation(key);
            if (value) el.setAttribute('title', value);
        });

        document.querySelectorAll('[data-i18n-alt]').forEach(function(el) {
            var key = el.getAttribute('data-i18n-alt');
            var value = getTranslation(key);
            if (value) el.setAttribute('alt', value);
        });

        document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el) {
            var key = el.getAttribute('data-i18n-placeholder');
            var value = getTranslation(key);
            if (value) el.setAttribute('placeholder', value);
        });

        document.documentElement.lang = currentLang;
    }

    function switchLanguage(lang) {
        if (lang === currentLang) return;
        loadTranslations(lang, function() {
            currentLang = lang;
            localStorage.setItem('smartEduLang', lang);
            applyTranslations();
            updateToggleButton();
        });
    }

    function updateToggleButton() {
        var toggle = document.getElementById('language-toggle');
        if (!toggle) return;
        var nextLang = currentLang === 'en' ? 'fr' : 'en';
        var info = SUPPORTED_LANGS[nextLang];
        if (!info) return;

        var flag = toggle.querySelector('.lang-flag');
        var label = toggle.querySelector('.lang-label');

        if (!flag || !label) {
            toggle.innerHTML =
                '<img class="lang-flag" src="' + info.flag + '" alt="' + nextLang.toUpperCase() + '" width="20" height="14">' +
                '<span class="lang-label">' + info.name + '</span>';
        } else {
            flag.src = info.flag;
            flag.alt = nextLang.toUpperCase();
            label.textContent = info.name;
        }
    }

    function initToggle() {
        var toggle = document.getElementById('language-toggle');
        if (!toggle) {
            var container = document.querySelector('.nav-container');
            if (!container) return;
            toggle = document.createElement('button');
            toggle.id = 'language-toggle';
            toggle.className = 'lang-toggle';
            toggle.setAttribute('aria-label', 'Switch language');
            container.appendChild(toggle);
        }

        toggle.addEventListener('click', function() {
            var nextLang = currentLang === 'en' ? 'fr' : 'en';
            switchLanguage(nextLang);
        });

        updateToggleButton();
    }

    loadTranslations(currentLang, function() {
        applyTranslations();
        initToggle();
        updateToggleButton();
    });
})();
