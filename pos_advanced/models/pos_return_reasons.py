from odoo import api, models, fields, tools


class ReturnReason(models.Model):
    _name = 'pos.return.reason'
    _description = 'Return Reasons'

    return_reasons = fields.Char(string="Return Reasons", required=True)


class EmployeeAccess(models.Model):
    _inherit = 'hr.employee'
    is_employee_access = fields.Boolean('Is Employee Access')


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result += [
            'hr.employee'
        ]
        return result

    def _loader_params_hr_employee(self):
        return{
            'search_params':{
                'fields': ['name'],
                'domain': [('is_employee_access', '=', True)]
            }
        }

    def _get_pos_ui_hr_employee(self, params):
        return self.env['hr.employee'].search_read(**params['search_params'])


class PosOrder(models.Model):
    _inherit = 'pos.order'

    return_reason_id = fields.Many2one(
        'pos.return.reason',
        string='Return Reason',
    )


