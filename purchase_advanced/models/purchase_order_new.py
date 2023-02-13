from odoo import api, models, fields, tools


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    signature = fields.Char(string='Signature')


