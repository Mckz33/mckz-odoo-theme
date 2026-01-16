from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    @property
    def THEME_COLOR_FIELDS(self):
        return [
            'color_appbar_text',
            'color_appbar_active',
            'color_appbar_background',
        ]

    @property
    def COLOR_ASSET_THEME_LIGHT_URL(self):
        return '/mckz_web_enterprise_theme/static/src/scss/colors_light.scss'

    @property
    def COLOR_BUNDLE_THEME_LIGHT_NAME(self):
        return 'web._assets_primary_variables'

    @property
    def COLOR_ASSET_THEME_DARK_URL(self):
        return '/mckz_web_enterprise_theme/static/src/scss/colors_dark.scss'

    @property
    def COLOR_BUNDLE_THEME_DARK_NAME(self):
        return 'web.assets_web_dark'

    #----------------------------------------------------------
    # Fields - Theme Settings
    #----------------------------------------------------------

    theme_favicon = fields.Binary(
        related='company_id.favicon',
        readonly=False
    )

    theme_background_image_light = fields.Binary(
        related='company_id.background_image_light',
        readonly=False
    )

    theme_background_image_dark = fields.Binary(
        related='company_id.background_image_dark',
        readonly=False
    )

    #----------------------------------------------------------
    # Fields - Border Radius
    #----------------------------------------------------------

    theme_border_radius = fields.Selection([
        ('none', 'Nenhum (0px)'),
        ('sm', 'Pequeno (4px)'),
        ('md', 'Médio (8px)'),
        ('lg', 'Grande (12px)'),
        ('xl', 'Extra Grande (16px)'),
        ('2xl', 'Máximo (24px)'),
    ], string='Borda Arredondada', default='md',
       config_parameter='mckz_web_enterprise_theme.border_radius')

    #----------------------------------------------------------
    # Fields - Font Family
    #----------------------------------------------------------

    theme_font_family = fields.Selection([
        ('system', 'Padrão do Sistema'),
        ('inter', 'Inter'),
        ('roboto', 'Roboto'),
        ('open-sans', 'Open Sans'),
        ('lato', 'Lato'),
        ('poppins', 'Poppins'),
        ('montserrat', 'Montserrat'),
        ('source-sans-pro', 'Source Sans Pro'),
        ('nunito', 'Nunito'),
        ('raleway', 'Raleway'),
        ('work-sans', 'Work Sans'),
        ('dm-sans', 'DM Sans'),
        ('plus-jakarta-sans', 'Plus Jakarta Sans'),
        ('mulish', 'Mulish'),
        ('quicksand', 'Quicksand'),
        ('rubik', 'Rubik'),
        ('ubuntu', 'Ubuntu'),
        ('cabin', 'Cabin'),
        ('exo-2', 'Exo 2'),
        ('josefin-sans', 'Josefin Sans'),
        ('manrope', 'Manrope'),
    ], string='Família de Fonte', default='system',
       config_parameter='mckz_web_enterprise_theme.font_family')

    #----------------------------------------------------------
    # Fields - Density
    #----------------------------------------------------------

    theme_density = fields.Selection([
        ('compact', 'Compacto'),
        ('comfortable', 'Confortável'),
        ('spacious', 'Espaçoso'),
    ], string='Densidade da Interface', default='comfortable',
       config_parameter='mckz_web_enterprise_theme.density')

    #----------------------------------------------------------
    # Fields - AppsBar Colors
    #----------------------------------------------------------

    theme_color_appbar_text_light = fields.Char(
        string='Cor do Texto do Menu (Claro)'
    )

    theme_color_appbar_active_light = fields.Char(
        string='Cor do Item Ativo (Claro)'
    )

    theme_color_appbar_background_light = fields.Char(
        string='Cor de Fundo do Menu (Claro)'
    )

    theme_color_appbar_text_dark = fields.Char(
        string='Cor do Texto do Menu (Escuro)'
    )

    theme_color_appbar_active_dark = fields.Char(
        string='Cor do Item Ativo (Escuro)'
    )

    theme_color_appbar_background_dark = fields.Char(
        string='Cor de Fundo do Menu (Escuro)'
    )

    #----------------------------------------------------------
    # Helper
    #----------------------------------------------------------

    def _get_light_theme_color_values(self):
        return self.env['web_editor.assets'].get_color_variables_values(
            self.COLOR_ASSET_THEME_LIGHT_URL,
            self.COLOR_BUNDLE_THEME_LIGHT_NAME,
            self.THEME_COLOR_FIELDS
        )

    def _get_dark_theme_color_values(self):
        return self.env['web_editor.assets'].get_color_variables_values(
            self.COLOR_ASSET_THEME_DARK_URL,
            self.COLOR_BUNDLE_THEME_DARK_NAME,
            self.THEME_COLOR_FIELDS
        )

    def _set_light_theme_color_values(self, values):
        colors = self._get_light_theme_color_values()
        for var, value in colors.items():
            values[f'theme_{var}_light'] = value
        return values

    def _set_dark_theme_color_values(self, values):
        colors = self._get_dark_theme_color_values()
        for var, value in colors.items():
            values[f'theme_{var}_dark'] = value
        return values

    def _detect_light_theme_color_change(self):
        colors = self._get_light_theme_color_values()
        return any(
            self[f'theme_{var}_light'] != val
            for var, val in colors.items()
        )

    def _detect_dark_theme_color_change(self):
        colors = self._get_dark_theme_color_values()
        return any(
            self[f'theme_{var}_dark'] != val
            for var, val in colors.items()
        )

    def _replace_light_theme_color_values(self):
        variables = [
            {
                'name': field,
                'value': self[f'theme_{field}_light']
            }
            for field in self.THEME_COLOR_FIELDS
        ]
        return self.env['web_editor.assets'].replace_color_variables_values(
            self.COLOR_ASSET_THEME_LIGHT_URL,
            self.COLOR_BUNDLE_THEME_LIGHT_NAME,
            variables
        )

    def _replace_dark_theme_color_values(self):
        variables = [
            {
                'name': field,
                'value': self[f'theme_{field}_dark']
            }
            for field in self.THEME_COLOR_FIELDS
        ]
        return self.env['web_editor.assets'].replace_color_variables_values(
            self.COLOR_ASSET_THEME_DARK_URL,
            self.COLOR_BUNDLE_THEME_DARK_NAME,
            variables
        )

    def _reset_light_theme_color_assets(self):
        self.env['web_editor.assets'].reset_asset(
            self.COLOR_ASSET_THEME_LIGHT_URL,
            self.COLOR_BUNDLE_THEME_LIGHT_NAME,
        )

    def _reset_dark_theme_color_assets(self):
        self.env['web_editor.assets'].reset_asset(
            self.COLOR_ASSET_THEME_DARK_URL,
            self.COLOR_BUNDLE_THEME_DARK_NAME,
        )

    #----------------------------------------------------------
    # Action
    #----------------------------------------------------------

    def action_reset_light_color_assets(self):
        self._reset_light_theme_color_assets()
        return super().action_reset_light_color_assets()

    def action_reset_dark_color_assets(self):
        self._reset_dark_theme_color_assets()
        return super().action_reset_dark_color_assets()

    #----------------------------------------------------------
    # Functions
    #----------------------------------------------------------

    def get_values(self):
        res = super().get_values()
        res = self._set_light_theme_color_values(res)
        res = self._set_dark_theme_color_values(res)
        return res

    def set_values(self):
        res = super().set_values()
        if self._detect_light_theme_color_change():
            self._replace_light_theme_color_values()
        if self._detect_dark_theme_color_change():
            self._replace_dark_theme_color_values()
        return res
