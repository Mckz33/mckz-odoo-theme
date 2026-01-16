from odoo import api, fields, models


# Definição dos 8 esquemas de cores do Lavend
COLOR_SCHEMES = {
    'metronic': {
        'name': 'Metronic',
        'light': {
            'color_brand': '#1B84FF',
            'color_primary': '#7239EA',
            'color_success': '#17C653',
            'color_info': '#7239EA',
            'color_warning': '#F6C000',
            'color_danger': '#F8285A',
        },
        'dark': {
            'color_brand': '#1B84FF',
            'color_primary': '#7239EA',
            'color_success': '#17C653',
            'color_info': '#7239EA',
            'color_warning': '#F6C000',
            'color_danger': '#F8285A',
        },
    },
    'slate': {
        'name': 'Slate',
        'light': {
            'color_brand': '#334155',
            'color_primary': '#3B82F6',
            'color_success': '#22C55E',
            'color_info': '#06B6D4',
            'color_warning': '#EAB308',
            'color_danger': '#EF4444',
        },
        'dark': {
            'color_brand': '#475569',
            'color_primary': '#60A5FA',
            'color_success': '#4ADE80',
            'color_info': '#22D3EE',
            'color_warning': '#FACC15',
            'color_danger': '#F87171',
        },
    },
    'haze': {
        'name': 'Haze',
        'light': {
            'color_brand': '#6366F1',
            'color_primary': '#8B5CF6',
            'color_success': '#10B981',
            'color_info': '#06B6D4',
            'color_warning': '#F59E0B',
            'color_danger': '#EF4444',
        },
        'dark': {
            'color_brand': '#818CF8',
            'color_primary': '#A78BFA',
            'color_success': '#34D399',
            'color_info': '#22D3EE',
            'color_warning': '#FBBF24',
            'color_danger': '#F87171',
        },
    },
    'gray': {
        'name': 'Gray',
        'light': {
            'color_brand': '#4B5563',
            'color_primary': '#6B7280',
            'color_success': '#10B981',
            'color_info': '#3B82F6',
            'color_warning': '#F59E0B',
            'color_danger': '#EF4444',
        },
        'dark': {
            'color_brand': '#6B7280',
            'color_primary': '#9CA3AF',
            'color_success': '#34D399',
            'color_info': '#60A5FA',
            'color_warning': '#FBBF24',
            'color_danger': '#F87171',
        },
    },
    'neutral': {
        'name': 'Neutral',
        'light': {
            'color_brand': '#78716C',
            'color_primary': '#A8A29E',
            'color_success': '#84CC16',
            'color_info': '#06B6D4',
            'color_warning': '#FBBF24',
            'color_danger': '#F87171',
        },
        'dark': {
            'color_brand': '#A8A29E',
            'color_primary': '#D6D3D1',
            'color_success': '#A3E635',
            'color_info': '#22D3EE',
            'color_warning': '#FCD34D',
            'color_danger': '#FCA5A5',
        },
    },
    'sage': {
        'name': 'Sage',
        'light': {
            'color_brand': '#4D7C0F',
            'color_primary': '#65A30D',
            'color_success': '#22C55E',
            'color_info': '#0EA5E9',
            'color_warning': '#EAB308',
            'color_danger': '#DC2626',
        },
        'dark': {
            'color_brand': '#65A30D',
            'color_primary': '#84CC16',
            'color_success': '#4ADE80',
            'color_info': '#38BDF8',
            'color_warning': '#FACC15',
            'color_danger': '#F87171',
        },
    },
    'zinc': {
        'name': 'Zinc',
        'light': {
            'color_brand': '#3F3F46',
            'color_primary': '#71717A',
            'color_success': '#22C55E',
            'color_info': '#38BDF8',
            'color_warning': '#FACC15',
            'color_danger': '#F43F5E',
        },
        'dark': {
            'color_brand': '#52525B',
            'color_primary': '#A1A1AA',
            'color_success': '#4ADE80',
            'color_info': '#7DD3FC',
            'color_warning': '#FDE047',
            'color_danger': '#FB7185',
        },
    },
    'mauve': {
        'name': 'Mauve',
        'light': {
            'color_brand': '#7C3AED',
            'color_primary': '#A855F7',
            'color_success': '#34D399',
            'color_info': '#22D3EE',
            'color_warning': '#FCD34D',
            'color_danger': '#FB7185',
        },
        'dark': {
            'color_brand': '#8B5CF6',
            'color_primary': '#C084FC',
            'color_success': '#6EE7B7',
            'color_info': '#67E8F9',
            'color_warning': '#FDE68A',
            'color_danger': '#FDA4AF',
        },
    },
}


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    # ----------------------------------------------------------
    # Properties
    # ----------------------------------------------------------

    @property
    def COLOR_FIELDS(self):
        return [
            'color_brand',
            'color_primary',
            'color_success',
            'color_info',
            'color_warning',
            'color_danger',
        ]

    @property
    def COLOR_ASSET_LIGHT_URL(self):
        return '/mckz_web_colors/static/src/scss/colors_light.scss'

    @property
    def COLOR_BUNDLE_LIGHT_NAME(self):
        return 'web._assets_primary_variables'

    @property
    def COLOR_ASSET_DARK_URL(self):
        return '/mckz_web_colors/static/src/scss/colors_dark.scss'

    @property
    def COLOR_BUNDLE_DARK_NAME(self):
        return 'web.assets_web_dark'

    #----------------------------------------------------------
    # Fields - Color Scheme Selection
    #----------------------------------------------------------

    color_scheme = fields.Selection([
        ('metronic', 'Metronic'),
        ('slate', 'Slate'),
        ('haze', 'Haze'),
        ('gray', 'Gray'),
        ('neutral', 'Neutral'),
        ('sage', 'Sage'),
        ('zinc', 'Zinc'),
        ('mauve', 'Mauve'),
        ('custom', 'Custom'),
    ], string='Color Scheme', default='metronic',
       config_parameter='mckz_web_colors.color_scheme')

    #----------------------------------------------------------
    # Fields Light Mode
    #----------------------------------------------------------

    color_brand_light = fields.Char(
        string='Brand Light Color'
    )

    color_primary_light = fields.Char(
        string='Primary Light Color'
    )

    color_success_light = fields.Char(
        string='Success Light Color'
    )

    color_info_light = fields.Char(
        string='Info Light Color'
    )

    color_warning_light = fields.Char(
        string='Warning Light Color'
    )

    color_danger_light = fields.Char(
        string='Danger Light Color'
    )

    #----------------------------------------------------------
    # Fields Dark Mode
    #----------------------------------------------------------

    color_brand_dark = fields.Char(
        string='Brand Dark Color'
    )

    color_primary_dark = fields.Char(
        string='Primary Dark Color'
    )

    color_success_dark = fields.Char(
        string='Success Dark Color'
    )

    color_info_dark = fields.Char(
        string='Info Dark Color'
    )

    color_warning_dark = fields.Char(
        string='Warning Dark Color'
    )

    color_danger_dark = fields.Char(
        string='Danger Dark Color'
    )

    #----------------------------------------------------------
    # Scheme Methods
    #----------------------------------------------------------

    @api.model
    def get_color_schemes(self):
        """Retorna todos os esquemas de cores disponíveis"""
        return COLOR_SCHEMES

    @api.model
    def get_scheme_colors(self, scheme_name):
        """Retorna as cores de um esquema específico"""
        return COLOR_SCHEMES.get(scheme_name, {})

    def _apply_color_scheme(self, scheme_name):
        """Aplica um esquema de cores predefinido"""
        if scheme_name == 'custom' or scheme_name not in COLOR_SCHEMES:
            return

        scheme = COLOR_SCHEMES[scheme_name]

        # Aplicar cores light mode
        for field in self.COLOR_FIELDS:
            self[f'{field}_light'] = scheme['light'].get(field, '')

        # Aplicar cores dark mode
        for field in self.COLOR_FIELDS:
            self[f'{field}_dark'] = scheme['dark'].get(field, '')

    @api.onchange('color_scheme')
    def _onchange_color_scheme(self):
        """Quando o esquema muda, aplica as cores predefinidas"""
        if self.color_scheme and self.color_scheme != 'custom':
            self._apply_color_scheme(self.color_scheme)

    def action_apply_scheme(self):
        """Ação para aplicar um esquema de cores e salvar"""
        self.ensure_one()
        if self.color_scheme and self.color_scheme != 'custom':
            self._apply_color_scheme(self.color_scheme)
            self._replace_light_color_values()
            self._replace_dark_color_values()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    #----------------------------------------------------------
    # Helper
    #----------------------------------------------------------

    def _get_light_color_values(self):
        return self.env['web_editor.assets'].get_color_variables_values(
            self.COLOR_ASSET_LIGHT_URL,
            self.COLOR_BUNDLE_LIGHT_NAME,
            self.COLOR_FIELDS
        )

    def _get_dark_color_values(self):
        return self.env['web_editor.assets'].get_color_variables_values(
            self.COLOR_ASSET_DARK_URL,
            self.COLOR_BUNDLE_DARK_NAME,
            self.COLOR_FIELDS
        )

    def _set_light_color_values(self, values):
        colors = self._get_light_color_values()
        for var, value in colors.items():
            values[f'{var}_light'] = value
        return values

    def _set_dark_color_values(self, values):
        colors = self._get_dark_color_values()
        for var, value in colors.items():
            values[f'{var}_dark'] = value
        return values

    def _detect_light_color_change(self):
        colors = self._get_light_color_values()
        return any(
            self[f'{var}_light'] != val
            for var, val in colors.items()
        )

    def _detect_dark_color_change(self):
        colors = self._get_dark_color_values()
        return any(
            self[f'{var}_dark'] != val
            for var, val in colors.items()
        )

    def _replace_light_color_values(self):
        variables = [
            {
                'name': field,
                'value': self[f'{field}_light']
            }
            for field in self.COLOR_FIELDS
        ]
        return self.env['web_editor.assets'].replace_color_variables_values(
            self.COLOR_ASSET_LIGHT_URL,
            self.COLOR_BUNDLE_LIGHT_NAME,
            variables
        )

    def _replace_dark_color_values(self):
        variables = [
            {
                'name': field,
                'value': self[f'{field}_dark']
            }
            for field in self.COLOR_FIELDS
        ]
        return self.env['web_editor.assets'].replace_color_variables_values(
            self.COLOR_ASSET_DARK_URL,
            self.COLOR_BUNDLE_DARK_NAME,
            variables
        )

    def _reset_light_color_assets(self):
        self.env['web_editor.assets'].reset_color_asset(
            self.COLOR_ASSET_LIGHT_URL,
            self.COLOR_BUNDLE_LIGHT_NAME,
        )

    def _reset_dark_color_assets(self):
        self.env['web_editor.assets'].reset_asset(
            self.COLOR_ASSET_DARK_URL,
            self.COLOR_BUNDLE_DARK_NAME,
        )

    #----------------------------------------------------------
    # Action
    #----------------------------------------------------------

    def action_reset_light_color_assets(self):
        self._reset_light_color_assets()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    def action_reset_dark_color_assets(self):
        self._reset_dark_color_assets()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    #----------------------------------------------------------
    # Functions
    #----------------------------------------------------------

    def get_values(self):
        res = super().get_values()
        res = self._set_light_color_values(res)
        res = self._set_dark_color_values(res)
        return res

    def set_values(self):
        res = super().set_values()
        if self._detect_light_color_change():
            self._replace_light_color_values()
        if self._detect_dark_color_change():
            self._replace_dark_color_values()
        return res
