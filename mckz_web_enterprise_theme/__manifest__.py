{
    'name': 'MckZ Backend Theme', 
    'summary': 'Odoo Enterprise Backend Theme',
    'description': '''
        This module offers a mobile compatible design for Odoo Enterprise. 
        Furthermore it allows the user to define some design preferences.
    ''',
    'version': '18.0.1.2.4',
    'category': 'Themes/Backend', 
    'license': 'LGPL-3', 
    'author': 'MckZ IT',
    'website': 'http://www.mukit.at',
    'live_test_url': 'https://my.mukit.at/r/f6m',
    'contributors': [
        'Mathias Markl <mathias.markl@mukit.at>',
    ],
    'depends': [
        'mckz_web_chatter',
        'mckz_web_dialog',
        'mckz_web_appsbar',
        'mckz_web_colors',
    ],
    'data': [
        'templates/web_layout.xml',
        'views/res_config_settings.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            (
                'before', 
                'mckz_web_colors/static/src/scss/colors.scss', 
                'mckz_web_enterprise_theme/static/src/scss/colors_light.scss'
            ),
            (
                'after', 
                'web/static/src/scss/primary_variables.scss', 
                'mckz_web_enterprise_theme/static/src/scss/variables.scss'
            ),
        ],
        'web.assets_backend': [
            'mckz_web_enterprise_theme/static/src/scss/theme.scss',
            'mckz_web_enterprise_theme/static/src/scss/fonts.scss',
            'mckz_web_enterprise_theme/static/src/webclient/theme_service.js',
            'mckz_web_enterprise_theme/static/src/webclient/font_service.js',
            'mckz_web_enterprise_theme/static/src/webclient/**/*.scss',
            'mckz_web_enterprise_theme/static/src/views/**/*.js',
            'mckz_web_enterprise_theme/static/src/views/**/*.scss',
            ('remove', 'mckz_web_enterprise_theme/static/src/**/*.dark.scss'),
            ('remove', 'mckz_web_enterprise_theme/static/src/webclient/home_menu/*'),
        ],
        "web.assets_web_dark": [
            (
                'after', 
                'mckz_web_colors/static/src/scss/colors.scss', 
                'mckz_web_enterprise_theme/static/src/scss/colors_dark.scss'
            ),
            'mckz_web_enterprise_theme/static/src/**/*.dark.scss',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'post_init_hook': '_setup_module',
    'uninstall_hook': '_uninstall_cleanup',
}
