/** @odoo-module **/

import { registry } from '@web/core/registry';

/**
 * MckZ Font Service
 * Handles Google Fonts integration for theme customization
 */

// Available Google Fonts
const GOOGLE_FONTS = {
    'system': { name: 'System Default', url: null },
    'inter': { name: 'Inter', url: 'Inter:wght@300;400;500;600;700' },
    'roboto': { name: 'Roboto', url: 'Roboto:wght@300;400;500;700' },
    'open-sans': { name: 'Open Sans', url: 'Open+Sans:wght@300;400;500;600;700' },
    'lato': { name: 'Lato', url: 'Lato:wght@300;400;700' },
    'poppins': { name: 'Poppins', url: 'Poppins:wght@300;400;500;600;700' },
    'montserrat': { name: 'Montserrat', url: 'Montserrat:wght@300;400;500;600;700' },
    'source-sans-pro': { name: 'Source Sans Pro', url: 'Source+Sans+Pro:wght@300;400;600;700' },
    'nunito': { name: 'Nunito', url: 'Nunito:wght@300;400;500;600;700' },
    'raleway': { name: 'Raleway', url: 'Raleway:wght@300;400;500;600;700' },
    'work-sans': { name: 'Work Sans', url: 'Work+Sans:wght@300;400;500;600;700' },
    'dm-sans': { name: 'DM Sans', url: 'DM+Sans:wght@400;500;700' },
    'plus-jakarta-sans': { name: 'Plus Jakarta Sans', url: 'Plus+Jakarta+Sans:wght@300;400;500;600;700' },
    'mulish': { name: 'Mulish', url: 'Mulish:wght@300;400;500;600;700' },
    'quicksand': { name: 'Quicksand', url: 'Quicksand:wght@300;400;500;600;700' },
    'rubik': { name: 'Rubik', url: 'Rubik:wght@300;400;500;600;700' },
    'ubuntu': { name: 'Ubuntu', url: 'Ubuntu:wght@300;400;500;700' },
    'cabin': { name: 'Cabin', url: 'Cabin:wght@400;500;600;700' },
    'exo-2': { name: 'Exo 2', url: 'Exo+2:wght@300;400;500;600;700' },
    'josefin-sans': { name: 'Josefin Sans', url: 'Josefin+Sans:wght@300;400;500;600;700' },
    'manrope': { name: 'Manrope', url: 'Manrope:wght@300;400;500;600;700' },
};

const fontService = {
    dependencies: [],

    start(env) {
        const loadedFonts = new Set();
        let currentFont = null;

        const loadGoogleFont = (fontKey) => {
            const font = GOOGLE_FONTS[fontKey];
            if (!font || !font.url || loadedFonts.has(fontKey)) {
                return;
            }

            // Create link element for Google Fonts
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.href = `https://fonts.googleapis.com/css2?family=${font.url}&display=swap`;
            link.id = `mckz-font-${fontKey}`;

            // Check if already exists
            if (!document.getElementById(link.id)) {
                document.head.appendChild(link);
                loadedFonts.add(fontKey);
            }
        };

        const applyFont = (fontKey) => {
            const body = document.body;

            // Remove existing font classes
            Object.keys(GOOGLE_FONTS).forEach(key => {
                body.classList.remove(`mckz_font_${key.replace(/-/g, '_')}`);
            });

            // Apply new font class
            if (fontKey && fontKey !== 'system') {
                loadGoogleFont(fontKey);
                body.classList.add(`mckz_font_${fontKey.replace(/-/g, '_')}`);
            }

            currentFont = fontKey;
        };

        // Get saved font from localStorage
        const getSavedFont = () => {
            try {
                return localStorage.getItem('mckz_font_family') || 'system';
            } catch (e) {
                return 'system';
            }
        };

        // Apply font settings
        const applyFontSettings = () => {
            const fontFamily = getSavedFont();
            applyFont(fontFamily);
        };

        // Apply on start
        applyFontSettings();

        // Listen for font changes
        env.bus.addEventListener('MCKZ_FONT:UPDATE', (ev) => {
            const detail = ev.detail || {};
            if (detail.fontKey) {
                applyFont(detail.fontKey);
            }
        });

        return {
            getAvailableFonts() {
                return GOOGLE_FONTS;
            },
            getCurrentFont() {
                return currentFont;
            },
            setFont(fontKey) {
                try {
                    localStorage.setItem('mckz_font_family', fontKey);
                } catch (e) {}
                applyFont(fontKey);
            },
            applyFontSettings,
        };
    },
};

registry.category('services').add('mckz_font', fontService);
