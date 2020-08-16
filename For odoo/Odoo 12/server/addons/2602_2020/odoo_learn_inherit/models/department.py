
from odoo import models, fields, api


class Department(models.Model):
    _inherit = 'department'

    @api.multi
    def remove_description(self):
        for department in self.search([]):
            department.description = ''
