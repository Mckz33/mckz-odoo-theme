{
    'name': 'MckZ Colors', 
    'summary': 'Customize your Odoo colors',
    'description': '''
        This module gives you options to customize the theme colors.
    ''',
    'version': '18.0.1.0.6',
    'category': 'Tools/UI',
    'license': 'LGPL-3', 
    'author': 'MckZ IT',
    'website': 'http://www.mukit.at',
    'live_test_url': 'https://my.mukit.at/r/f6m',
    'contributors': [
        'Mathias Markl <mathias.markl@mukit.at>',
    ],
    'depends': [
        'base_setup',
        'web_editor',
    ],
    'data': [
        'templates/webclient.xml',
        'views/res_config_settings.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [
            ('prepend', 'mckz_web_colors/static/src/scss/colors.scss'),
            (
                'before',
                'mckz_web_colors/static/src/scss/colors.scss',
                'mckz_web_colors/static/src/scss/colors_light.scss'
            ),
        ],
        'web.assets_backend': [
            'mckz_web_colors/static/src/scss/settings.scss',
        ],
        'web.assets_web_dark': [
            (
                'after',
                'mckz_web_colors/static/src/scss/colors.scss',
                'mckz_web_colors/static/src/scss/colors_dark.scss'
            ),
        ],
    },
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'uninstall_hook': '_uninstall_cleanup',
}
