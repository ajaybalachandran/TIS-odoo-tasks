from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    min_sale_amount = fields.Float(string="Minimum Sale Amount",
                                   config_parameter="minimum_sale_amount.min_sale_amount")
