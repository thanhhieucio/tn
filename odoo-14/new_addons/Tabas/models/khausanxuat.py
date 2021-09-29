from odoo import models, fields, api


class khausanxuat(models.Model):
    _name = 'tabas.khausanxuat'
    _description = 'Thông tin các khâu, công đoạn sản xuất'
    name = fields.Char(string='Tên')
    ksx_Ma = fields.Char(string='Mã (Khâu, Mã công đoạn')
    ksx_description = fields.Text(string='Ghi chú')



