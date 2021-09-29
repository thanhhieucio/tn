from odoo import models, fields, api


class donvitinh(models.Model):
    _name = 'tabas.donvitinh'
    _description = 'Thông tin đơn vị tính của sản phẩm'
    name = fields.Char(string='Tên')
    dvt_Ma = fields.Char(string='Mã ĐVT')
    dvt_description = fields.Text(string='Description')
    dvt_sp_id = fields.One2many(comodel_name='tabas.sanpham', inverse_name='sp_dv_id', string='Ds Sản Phẩm')


