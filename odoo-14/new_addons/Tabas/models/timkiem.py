from odoo import fields, models

class timkiem(models.Model):
    _name = 'tabas.timkiem'
    _description = 'Tìm kiếm thông tin'

    name = fields.Text(string='Tiêu đề')
    tknd_code = fields.Char(string='Mã nội dung')
    tkghichu_description = fields.Text(string='Ghi Chú')



