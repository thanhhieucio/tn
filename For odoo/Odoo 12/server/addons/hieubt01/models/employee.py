from odoo import models, fields, api
from datetime import datetime
import re
from odoo.exceptions import ValidationError


class Employee(models.Model):
    _name = 'hieubt.employee'

    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    birthday = fields.Date(string='Birth day')
    email_id = fields.Char(string='Email')
    trial = fields.Boolean(default=False, string='Trial')
    state = fields.Selection([('working', 'Đang làm việc'), ('closed', 'Đã nghỉ việc'), ('trial', 'Đang thử việc')],
                             Default='working', string='State')
    basicpay = fields.Float(string='BasicPay', default=2.34)
    department_id = fields.Many2one(comodel_name='hieubt.department', string='Department')
    age = fields.Integer(string='Age', compute='_calculate_age',store=True)

    _sql_constraints = [
        ('check_income_year', 'CHECK(state)',
         'Please input income year greater than 0!'),
        ('check_unique_phone', 'UNIQUE(phone)',
         'Phone is already exist !')
    ]



    @api.multi
    # @api.depends('birthday')
    # def Test(self):
    #     self.ensure_one()
    #     total = 0
    #     for order in self.department_id:
    #         total += order.summary
    #         print(total)

    @api.onchange('email_id')
    def validate_mail(self):
        if self.email_id:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email_id)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')


    import datetime
    #@api.depends('birthday')
    @api.onchange('birthday')
    def _calculate_age(self):
        if self.birthday:
            for record in self:
                year = int(format(datetime.now().year)) - int(format(self.birthday.year))
                record.age = year

