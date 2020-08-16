
from odoo import models, fields, api


class Department(models.Model):
    _name = 'app.department'
    _rec_name = 'department_name'

    department_name = fields.Char('Name')
    description = fields.Text(string='Description')
    employee_ids = fields.One2many(comodel_name='employee',
                                   inverse_name='department_id',
                                   string='Employees')
    display_description = fields.Boolean(compute='get_display_desc',
                                         string='Display', default=False, store=True)

    @api.depends('department_name')
    def get_display_desc(self):
        for department in self:
            if department.department_name != '' and department.department_name != False:
                department.display_description = True
            else:
                department.display_description = False


