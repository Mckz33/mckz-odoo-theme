/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { browser } from "@web/core/browser/browser";

import { Chatter } from "@mail/chatter/web_portal/chatter";

/**
 * MckZ Chatter Patch
 * Adds notification toggle functionality
 */
patch(Chatter.prototype, {
    setup() {
        super.setup();

        // Initialize notification toggle state
        try {
            const showNotificationMessages = browser.localStorage.getItem(
                'mckz_web_chatter.notifications'
            );
            if (this.state) {
                this.state.showNotificationMessages = (
                    showNotificationMessages != null ?
                    JSON.parse(showNotificationMessages) : true
                );
            }
        } catch (e) {
            console.warn('MckZ Chatter: Failed to load notification settings', e);
        }
    },

    /**
     * Toggle notification messages visibility
     */
    onClickNotificationsToggle() {
        if (!this.state) return;

        const showNotificationMessages = !this.state.showNotificationMessages;
        try {
            browser.localStorage.setItem(
                'mckz_web_chatter.notifications',
                JSON.stringify(showNotificationMessages)
            );
        } catch (e) {}
        this.state.showNotificationMessages = showNotificationMessages;
    },
});
