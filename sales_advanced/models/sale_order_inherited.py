from odoo import api, models, fields, tools


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection_add=[('approved', 'Approved'), ('sale',)])
    discount = fields.Float(string='Discount')

    def action_approve(self):
        for rec in self:
            rec.state = 'approved'

    @api.onchange('order_line')
    def _onchange_order_line(self):
        for order in self:
            order_lines = order.order_line
            disc = [line.discount for line in order_lines if line.discount > 5]
            if disc:
                order.discount = disc[-1]
            else:
                order.discount = 0









