
from odoo import models, fields, api
from odoo.addons import decimal_precision as dp


class Orders(models.Model):
    _name = 'orders'

    total_price = fields.Float(string='Total Price', digits=dp.get_precision('Product Unit of Measure'))
    employee_ids = fields.Many2many(comodel_name='employee',
                                    relation='order_employee_rel',
                                    column1='order_id',
                                    column2='employee_id',
                                    string='Employees')
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('ordered', 'Ordered'),
        ('paid', 'Paid')], string='State', default='draft')
    # user_id = fields.Many2one('res.users', string='Users')
    # employee_ids = fields.Many2many('employee', string='Employees')

    # @api.one
    # def set_to_paid(self):
    #     self.state = 'paid'

    # @api.multi
    # def set_to_paid(self):
    #     for order in self:
    #         order.state = 'paid'

    @api.model
    def set_to_paid(self):
        ls_order = self.search([])
        for order in ls_order:
            order.state = 'paid'

