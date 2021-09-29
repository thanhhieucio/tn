
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime


class Employee(models.Model):
    _name = 'app.employee'

    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    # benefit = fields.Integer(default=3000000, string='Benefit')
    trial = fields.Boolean(default=False, string='Trial')
    income_date = fields.Date(string='Income Date')
    income_year = fields.Integer(string='Income Year')
    state = fields.Selection(
        selection=[('working', 'Working'), ('closed', 'Closed')],
        default='working', string='State')
    benefit = fields.Integer(compute='_get_benefit', string='Benefit', store=True)
    department_id = fields.Many2one(comodel_name='department', string='Department')
    order_ids = fields.Many2many(comodel_name='orders', relation='order_employee_rel',
                                 column1='employee_id',
                                 column2='order_id',
                                 string='Orders')
    level = fields.Selection(selection=[('1', 'Level 1'), ('2', 'Level 2'), ('3', 'Level 3')],
                             string='Level')

    _sql_constraints = [
        ('check_income_year', 'CHECK(income_year > 0)',
         'Please input income year greater than 0!'),
        ('check_unique_phone', 'UNIQUE(phone)',
         'Phone is already exist !')
    ]

    # @api.constrains('income_year')
    # def validate_income_year(self):
    #     if self.income_year <= 0:
    #         raise ValidationError('Please input income year greater than 0')

    # @api.constrains('phone')
    # def validate_phone(self):
    #     if not self.phone.isdigit():
    #         raise ValidationError('Please input phone is number')

    @api.depends('income_year')
    def _get_benefit(self):
        for employee in self:
            if employee.income_year <= 1:
                employee.benefit = 3000000
            elif 1 < employee.income_year <= 3:
                employee.benefit = 5000000
            else:
                employee.benefit = 10000000

    #@api.multi
    def set_closed(self):
        self.ensure_one()
        # ls_order = self.order_ids
        total = 0
        for order in self.order_ids:
            total += order.total_price
        print(total)
        print(sum(self.order_ids.mapped('total_price')))

        self.env['orders'].set_to_paid()

        self.order_ids.set_to_paid()

        ls_order = self.env['orders'].search([('employee_ids', 'in', self.id)])
        ls_order.set_to_paid()

        orders = self.env['orders'].browse(1)
        orders.set_to_paid()

        for emp in self:
            emp.state = 'closed'

    #@api.multi
    def set_working(self):
        print(self.env.context)
        # self.write({'state': 'working'})
        # for emp in self:
        #     emp.state = 'working'

    #@api.multi
    def write(self, vals):
        name = vals.get('name', False)
        # if name:
        #     vals['name'] = name.title()
        result = super(Employee, self).write(vals)
        # for emp in self:
        #     emp.with_context({'from': 'write'}).set_working()
        return result

    #@api.multi
    def unlink(self):
        return super(Employee, self).unlink()

    @api.model
    def create(self, vals):
        record = super(Employee, self).create(vals)
        # if not record.phone.isdigit():
        #     raise ValidationError('Please input phone is number 1')
        record.with_context({'from': 'create'}).set_working()

        return record

    # @api.onchange('income_date')
    # def onchange_income_date(self):
    #     current_year = datetime.now().year
    #     self.income_year = current_year - int(self.income_date[:4])
    #     if self.income_year <= 0:
    #         warning = {
    #             'title': 'This is title',
    #             'message': 'This is message'
    #     #         }
    #
    #         return {'warning': warning}

    # @api.onchange('income_year')
    # def onchange_income_year(self):
    #     if self.income_year <= 0:
    #         raise ValidationError('Error')

    @api.onchange('name')
    def onchange_name(self):
        if self.name != '' and self.name:
            domain = {
                'department_id': []
            }
            return {'domain': domain}
