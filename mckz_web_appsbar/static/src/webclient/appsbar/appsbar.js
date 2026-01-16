/** @odoo-module **/

import { url } from '@web/core/utils/urls';
import { useService } from '@web/core/utils/hooks';
import { browser } from "@web/core/browser/browser";
import { session } from "@web/session";

import { Component, onWillUnmount, useState, useRef } from '@odoo/owl';

export class AppsBar extends Component {
    static template = 'mckz_web_appsbar.AppsBar';
    static props = {};

    setup() {
        this.companyService = useService('company');
        this.appMenuService = useService('app_menu');
        this.menuService = useService('menu');
        this.actionService = useService('action');

        // Refs for DOM elements
        this.sidebarPanel = useRef('sidebarPanel');

        // State for sidebar and submenu
        this.state = useState({
            sidebarOpen: false,
            hoveredApp: null,
            submenuVisible: false,
            submenuItems: [],
            submenuPosition: { top: 0 },
            isPinned: false,
            mouseInSidebar: false,
            mouseInSubmenu: false,
            userMenuOpen: false,
        });

        // Timeouts
        this._hideTimeout = null;
        this._closeTimeout = null;

        // Get user info from session
        this.userName = session.name || session.username || 'Usuário';
        this.userId = session.uid;

        if (this.companyService.currentCompany.has_appsbar_image) {
            this.sidebarImageUrl = url('/web/image', {
                model: 'res.company',
                field: 'appbar_image',
                id: this.companyService.currentCompany.id,
            });
        }

        const renderAfterMenuChange = () => {
            this.render();
        };

        this.env.bus.addEventListener(
            'MENUS:APP-CHANGED', renderAfterMenuChange
        );

        onWillUnmount(() => {
            this.env.bus.removeEventListener(
                'MENUS:APP-CHANGED', renderAfterMenuChange
            );
            this._clearAllTimeouts();
        });

        // Setup keyboard shortcut (ESC to close)
        this.keydownHandler = (ev) => {
            if (ev.key === 'Escape' && this.state.sidebarOpen) {
                this.closeSidebar();
            }
        };
        document.addEventListener('keydown', this.keydownHandler);

        onWillUnmount(() => {
            document.removeEventListener('keydown', this.keydownHandler);
        });
    }

    _clearAllTimeouts() {
        if (this._hideTimeout) {
            clearTimeout(this._hideTimeout);
            this._hideTimeout = null;
        }
        if (this._closeTimeout) {
            clearTimeout(this._closeTimeout);
            this._closeTimeout = null;
        }
    }

    // Toggle sidebar
    toggleSidebar() {
        if (this.state.sidebarOpen) {
            this.closeSidebar();
        } else {
            this.openSidebar();
        }
    }

    openSidebar() {
        this._clearAllTimeouts();
        this.state.sidebarOpen = true;
        const actionContainer = document.querySelector('.o_action_manager');
        if (actionContainer) {
            actionContainer.style.marginLeft = '260px';
            actionContainer.style.transition = 'margin-left 0.25s ease';
        }
    }

    closeSidebar() {
        this._clearAllTimeouts();
        this.state.sidebarOpen = false;
        this.state.userMenuOpen = false;
        this._hideSubmenu();
        const actionContainer = document.querySelector('.o_action_manager');
        if (actionContainer) {
            actionContainer.style.marginLeft = '0';
            actionContainer.style.transition = 'margin-left 0.25s ease';
        }
    }

    // Sidebar mouse events
    _onSidebarMouseEnter() {
        this._clearAllTimeouts();
        this.state.mouseInSidebar = true;
    }

    _onSidebarMouseLeave() {
        this.state.mouseInSidebar = false;
        this._hideTimeout = setTimeout(() => {
            if (!this.state.mouseInSubmenu && !this.state.isPinned) {
                this._hideSubmenu();
            }
        }, 150);
    }

    _onAppClick(app) {
        this._hideSubmenu();
        this.closeSidebar();
        return this.appMenuService.selectApp(app);
    }

    _onAppMouseEnter(app, event) {
        this._clearAllTimeouts();

        const childMenus = this.menuService.getMenuAsTree(app.id)?.childrenTree || [];

        if (childMenus.length > 0) {
            const rect = event.currentTarget.getBoundingClientRect();

            this.state.hoveredApp = app;
            this.state.submenuItems = childMenus;
            this.state.submenuVisible = true;
            this.state.submenuPosition = {
                top: Math.min(rect.top, window.innerHeight - 400),
            };
        } else {
            this._hideTimeout = setTimeout(() => {
                if (!this.state.mouseInSubmenu) {
                    this._hideSubmenu();
                }
            }, 100);
        }
    }

    _onAppMouseLeave() {
        this._hideTimeout = setTimeout(() => {
            if (!this.state.mouseInSubmenu && !this.state.mouseInSidebar && !this.state.isPinned) {
                this._hideSubmenu();
            }
        }, 200);
    }

    _onSubmenuMouseEnter() {
        this._clearAllTimeouts();
        this.state.mouseInSubmenu = true;
    }

    _onSubmenuMouseLeave() {
        this.state.mouseInSubmenu = false;

        if (!this.state.isPinned) {
            this._hideTimeout = setTimeout(() => {
                if (!this.state.mouseInSidebar) {
                    this._hideSubmenu();
                }
            }, 150);
        }
    }

    _hideSubmenu() {
        this.state.hoveredApp = null;
        this.state.submenuVisible = false;
        this.state.submenuItems = [];
    }

    _onSubmenuItemClick(menu) {
        this._hideSubmenu();
        this.closeSidebar();
        this.menuService.selectMenu(menu);
    }

    _togglePin() {
        this.state.isPinned = !this.state.isPinned;
    }

    _hasChildren(menu) {
        return menu.childrenTree && menu.childrenTree.length > 0;
    }

    _getMenuItems(app) {
        const tree = this.menuService.getMenuAsTree(app.id);
        return tree?.childrenTree || [];
    }

    // User menu actions
    toggleUserMenu() {
        this.state.userMenuOpen = !this.state.userMenuOpen;
    }

    openSettings() {
        this.closeSidebar();
        this.actionService.doAction('base_setup.action_general_configuration');
    }

    openPreferences() {
        this.closeSidebar();
        this.actionService.doAction({
            type: 'ir.actions.act_window',
            res_model: 'res.users',
            res_id: this.userId,
            views: [[false, 'form']],
            target: 'current',
        });
    }

    openDocumentation() {
        browser.open('https://www.odoo.com/documentation', '_blank');
    }

    openSupport() {
        browser.open('https://www.odoo.com/help', '_blank');
    }

    openShortcuts() {
        this.closeSidebar();
        // Trigger keyboard shortcut display (Alt+Shift by default in Odoo)
        const event = new KeyboardEvent('keydown', {
            key: '?',
            altKey: true,
            bubbles: true,
        });
        document.dispatchEvent(event);
    }

    openUserPreferences() {
        this.closeSidebar();
        this.actionService.doAction({
            type: 'ir.actions.act_window',
            res_model: 'res.users',
            res_id: this.userId,
            views: [[false, 'form']],
            target: 'new',
            context: { 'form_view_ref': 'base.view_users_form_simple_modif' },
        });
    }

    openOdooStore() {
        this.closeSidebar();
        this.actionService.doAction('base.open_module_tree');
    }

    logout() {
        browser.location.href = '/web/session/logout';
    }
}
