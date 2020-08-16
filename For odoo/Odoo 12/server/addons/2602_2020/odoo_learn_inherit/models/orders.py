
from odoo import models, fields, api


class Orders(models.Model):
    _inherit = 'orders'

    name = fields.Char(string='Name', default=lambda self: self.env['ir.sequence'].next_by_code('ORDER_SEQ'))

    @api.model
    def create(self, vals):
        # vals['name'] = self.env['ir.sequence'].next_by_code('ORDER_SEQ') or '/'
        # 2 / 0
        return super(Orders, self).create(vals)

    @api.multi
    def format_employee_name(self, name):
        return name.title()
