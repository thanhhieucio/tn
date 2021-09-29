from odoo import models, api, fields


class nhapxuatchitiet(models.Model):
    _name = 'tabas.nhapxuatchitiet'
    _description = 'Thông tin chiết về nhập xuất'

    nxct_nx_id = fields.Many2one(comodel_name='tabas.nhapxuat', string='Số Nhập xuất')
    nxct_sp_id = fields.Many2one(comodel_name='tabas.sanpham', string='Sản phẩm')
    nxct_dvt_id=fields.Many2one(comodel_name='tabas.donvitinh', string='Đơn Vị Tính')
    nxct_sl = fields.Float(string='Số Lượng')
    nxct_dongia = fields.Float(string='Đ. Giá')
    nxct_thanhtien =fields.Float(compute='_set_thanhtien',  store=True, string='T. Tiền')

    @api.multi
    def _set_thanhtien(self):
        self.ensure_one()
            # ls_order = self.order_ids
        self.nxct_thanhtien =99
