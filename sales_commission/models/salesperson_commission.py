from odoo import api, models, fields, tools


class SaleOrder(models.Model):
    _inherit = 'res.users'

    commission = fields.Float(string='Commission')
