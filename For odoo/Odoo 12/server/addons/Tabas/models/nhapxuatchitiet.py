from odoo import models, api, fields


class nhapxuatchitiet(models.Model):
    _name = 'tabas.nhapxuatchitiet'
    _description = 'Thông tin chiết về nhập xuất'

    nxct_nx_id = fields.Many2one(comodel_name='tabas.nhapxuat', string='Số Nhập xuất')
    nxct_sp_id = fields.Many2one(comodel_name='tabas.sanpham', string='Sản phẩm')
    nxct_sl = fields.Float(string='Số Lượng')
