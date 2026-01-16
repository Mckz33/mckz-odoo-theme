/** @odoo-module **/

import { registry } from '@web/core/registry';

/**
 * MckZ Theme Service
 * Handles theme customization (border radius, density)
 */
const themeService = {
    dependencies: [],

    start(env) {
        // Get saved settings from localStorage
        const getSavedSettings = () => {
            try {
                return {
                    borderRadius: localStorage.getItem('mckz_border_radius') || 'md',
                    density: localStorage.getItem('mckz_density') || 'comfortable',
                };
            } catch (e) {
                return { borderRadius: 'md', density: 'comfortable' };
            }
        };

        // Apply theme settings
        const applyThemeSettings = () => {
            const root = document.documentElement;
            const body = document.body;
            const settings = getSavedSettings();

            // Apply border radius
            const radiusClasses = ['mckz_radius_none', 'mckz_radius_sm', 'mckz_radius_md', 'mckz_radius_lg', 'mckz_radius_xl', 'mckz_radius_2xl'];
            radiusClasses.forEach(cls => body.classList.remove(cls));
            body.classList.add(`mckz_radius_${settings.borderRadius}`);

            // Apply density
            const densityClasses = ['mckz_density_compact', 'mckz_density_comfortable', 'mckz_density_spacious'];
            densityClasses.forEach(cls => body.classList.remove(cls));
            body.classList.add(`mckz_density_${settings.density}`);

            // Set CSS variables
            const radiusValues = {
                'none': '0px',
                'sm': '4px',
                'md': '8px',
                'lg': '12px',
                'xl': '16px',
                '2xl': '24px'
            };

            const densityValues = {
                'compact': '0.75',
                'comfortable': '1',
                'spacious': '1.25'
            };

            root.style.setProperty('--mckz-border-radius', radiusValues[settings.borderRadius] || '8px');
            root.style.setProperty('--mckz-density-factor', densityValues[settings.density] || '1');
        };

        // Apply on start
        applyThemeSettings();

        // Listen for theme changes
        env.bus.addEventListener('MCKZ_THEME:UPDATE', applyThemeSettings);

        return {
            applyThemeSettings,
            setBorderRadius(radius) {
                try {
                    localStorage.setItem('mckz_border_radius', radius);
                } catch (e) {}
                applyThemeSettings();
            },
            setDensity(density) {
                try {
                    localStorage.setItem('mckz_density', density);
                } catch (e) {}
                applyThemeSettings();
            }
        };
    },
};

registry.category('services').add('mckz_theme', themeService);
