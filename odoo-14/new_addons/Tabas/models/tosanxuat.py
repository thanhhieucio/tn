from odoo import models, fields, api


class tosanxuat(models.Model):
    _name = 'tabas.tosanxuat'
    _description = 'Thông tin danh sách các tổ sản xuất tham gia quá trình'
    name = fields.Char(string='Tên')
    To_Ma = fields.Char(string='Mã Tổ')
    To_SoNhanCong = fields.Float(string='Số lượng nhân công hiện')
    To_description = fields.Text(string='Ghi chú')
