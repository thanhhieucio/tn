from odoo import models, fields
from . import  employee
from datetime import datetime


class Department(models.Model):
    _name = 'hieubt.department'
    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    description = fields.Text(string='Description')
    summary = fields.Float(string='summary - Tổng số nhân viên')




