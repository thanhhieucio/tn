from odoo import models, fields, api


class calamviec(models.Model):
    _name = 'tabas.calamviec'
    _description = 'Thông tin ca kíp, thời gian vào ca ra ca'
    name = fields.Char(string='Tên')
    Ca_Ma = fields.Char(string='Mã (Khâu, Mã công đoạn')
    Ca_Vao = fields.Float(string='Thời gian vào ca (8H15 = 8.15)')
    Ca_Ra = fields.Float(string='Thời gian ra(22H15 = 22.15)')
    Ca_description = fields.Text(string='Ghi chú')
