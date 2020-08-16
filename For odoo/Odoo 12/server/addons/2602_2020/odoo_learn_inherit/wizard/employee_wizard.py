
from odoo import models, fields, api


class EmployeeWizard(models.TransientModel):
    _name = 'employee.wizard'

    income_year = fields.Integer(string='Income Year')

    @api.multi
    def calc_benefit(self):
        if self.income_year > 0:
            employee_id = self.env.context.get('active_id', False)
            employee = self.env['employee'].browse(employee_id)
            employee.income_year = self.income_year
