from odoo import api, models, fields, tools
from odoo.tools.misc import formatLang
from odoo.addons.base.models.res_currency import Currency


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    commission = fields.Float(compute='_compute_commission', string='Commission(%)')
    commission_amount = fields.Float(compute='_compute_commission_amount', string="Commission Amount", default=0.00)
    # amount_total = fields.Monetary(compute='_compute_amounts', store=True)

    @api.depends('user_id.commission')
    def _compute_commission(self):
        for order in self:
            order.commission = order.user_id.commission

    def _compute_commission_amount(self):
        res = self._compute_tax_totals()
        for order in self:
            print(order)
            if res:
                order.commission_amount = res
            else:
                order.commission_amount = 0.00

    @api.depends('order_line.tax_id', 'order_line.price_unit', 'amount_total', 'amount_untaxed', 'currency_id')
    def _compute_tax_totals(self):
        super()._compute_tax_totals()
        for order in self:
            if order.tax_totals['amount_untaxed'] >= self.commission:
                old_amount_total = order.tax_totals['amount_total']
                order.tax_totals['amount_untaxed'] += (self.commission/100)*order.tax_totals['amount_total']
                order.tax_totals['amount_total'] += (self.commission/100)*order.tax_totals['amount_total']
                order.tax_totals['formatted_amount_total'] = formatLang(self.env, order.tax_totals['amount_total'], currency_obj=order.company_id.currency_id)
                order.tax_totals['formatted_amount_untaxed'] = formatLang(self.env, order.tax_totals['amount_untaxed'], currency_obj=order.company_id.currency_id)
                self.commission_amount = order.tax_totals['amount_total'] - old_amount_total
                return self.commission_amount


class AccountMove(models.Model):
    _inherit = 'account.move'

    commission = fields.Float(compute='_compute_commission', string='Commission(%)')
    commission_amount = fields.Float(compute='_compute_commission_amount', string="Commission Amount", default=0.00)
    # amount_total = fields.Monetary(compute='_compute_amounts', store=True)

    @api.depends('user_id.commission')
    def _compute_commission(self):
        for order in self:
            order.commission = order.user_id.commission

    def _compute_commission_amount(self):
        res = self._compute_tax_totals()
        for move in self:
            if res:
                move.commission_amount = res
            else:
                move.commission_amount = 0.00

    def _compute_tax_totals(self):
        super()._compute_tax_totals()
        for move in self:
            for i in move.line_ids:
                print(i.debit)
        for move in self:
            old_amount_total = move.tax_totals['amount_total']
            if move.tax_totals['amount_untaxed'] >= self.commission:
                move.tax_totals['amount_untaxed'] += (self.commission/100)*move.tax_totals['amount_total']
                move.tax_totals['amount_total'] += (self.commission/100)*move.tax_totals['amount_total']
                move.tax_totals['formatted_amount_total'] = formatLang(self.env, move.tax_totals['amount_total'], currency_obj=move.company_id.currency_id)
                move.tax_totals['formatted_amount_untaxed'] = formatLang(self.env, move.tax_totals['amount_untaxed'], currency_obj=move.company_id.currency_id)
                self.amount_residual = move.tax_totals['amount_total']  # to change amount due
                self.commission_amount = move.tax_totals['amount_total'] - old_amount_total
                return self.commission_amount


# class AccountTaxGroup(models.Model):
#     _inherit = 'account.tax'
#
#     order_id = fields.Many2one('sale.order', string='Sale Order')
#
#     def _prepare_tax_totals(self, base_lines, currency, tax_lines=None):
#         res = super()._prepare_tax_totals(base_lines, currency, tax_lines=tax_lines)
#         commission_amount = self.env.user.commission
#         if res['amount_untaxed'] >= commission_amount:
#             res['amount_untaxed'] -= commission_amount
#             res['amount_total'] -= commission_amount
#             res['formatted_amount_total'] = formatLang(self.env, res['amount_total'], currency_obj=currency)
#             res['formatted_amount_untaxed'] = formatLang(self.env, res['amount_untaxed'], currency_obj=currency)
#         # print(res)
#         # sale_order_commission = self.order_id.user_id.commission
#         # print(sale_order_commission)
#         # print(self._module)
#         return res
#     @api.model
#     def _prepare_tax_totals(self, base_lines, currency, tax_lines=None):
#         modified_amount = super(AccountTaxGroup, self)._prepare_tax_totals(self, currency)
#         modified_amount['amount_total'] = super.amount_untaxed + super.amount_tax
#         return modified_amount
