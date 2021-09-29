from odoo import models, fields, api


class phanxuongsanxuat(models.Model):
    _name = 'tabas.phanxuongsanxuat'
    _description = 'Thông tin tên phân xưởng'
    name = fields.Char(string='Tên phân xưởng')
    Px_Ma = fields.Char(string='Mã phân xưởng')
    Px_SoNhanCong = fields.Float(string='Số lượng nhân công hiện tại')
    Px_description = fields.Text(string='Ghi chú')
