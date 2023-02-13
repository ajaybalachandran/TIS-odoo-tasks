from odoo import api, models, fields, tools


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    # custom_country = fields.Char(string='Country')
    custom_country = fields.Many2one(
        'res.country', string='Country',
        compute='_compute_partner_address_values', readonly=False, store=True)

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.custom_country = self.partner_id.country_id

    # def _prepare_customer_values(self, partner_name, is_company=False, parent_id=False):
    #     email_parts = tools.email_split(self.email_from)
    #     res = {
    #         'name': partner_name,
    #         'user_id': self.env.context.get('default_user_id') or self.user_id.id,
    #         'comment': self.description,
    #         'team_id': self.team_id.id,
    #         'parent_id': parent_id,
    #         'phone': self.phone,
    #         'mobile': self.mobile,
    #         'email': email_parts[0] if email_parts else False,
    #         'title': self.title.id,
    #         'function': self.function,
    #         'street': self.street,
    #         'street2': self.street2,
    #         'zip': self.zip,
    #         'city': self.city,
    #         'country_id': self.custom_country.id,  # here is the change
    #         'state_id': self.state_id.id,
    #         'website': self.website,
    #         'is_company': is_company,
    #         'type': 'contact'
    #     }
    #     if self.lang_id:
    #         res['lang'] = self.lang_id.code
    #     return res

    def _prepare_customer_values(self, partner_name, is_company=False, parent_id=False):
        partner = super(CrmLead, self)._prepare_customer_values(partner_name, is_company=False, parent_id=False)
        partner['country_id'] = self.custom_country.id
        return partner









