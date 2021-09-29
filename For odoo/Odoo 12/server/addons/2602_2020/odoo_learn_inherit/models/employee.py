from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'employee'

    phone = fields.Char(string='Employee Phone', required=True)
    order_count = fields.Integer(string='Order Count', compute='_get_order_count', store=True)

    @api.depends('order_ids')
    def _get_order_count(self):
        for emp in self:
            emp.order_count = len(emp.order_ids)

    @api.onchange('level')
    def onchange_level(self):
        print(self.level)

    @api.model
    def create(self, vals):
        return super(Employee, self).create(vals)

    #@api.multi
    def set_working(self):
        super(Employee, self).set_working()
        print('continue of set working function')
