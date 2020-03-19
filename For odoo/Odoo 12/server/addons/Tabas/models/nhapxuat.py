from odoo import models, api, fields


class Nhapxuat(models.Model):
    _name = 'tabas.nhapxuat'
    _description = 'Thông tin nhập xuất - khách hàng'

    name = fields.Char(string='Hóa đơn')
    nx_code = fields.Char(string='Số HĐ')
    nx_ngay = fields.datetime(string='Ngày NX')
    nx_kh_code = fields.Many2one(comodel_name='tabas.khachhang' )