from odoo import models, fields, api


class nhapxuatchitiet(models.Model):
    _name = 'tabas.nhapxuatchitiet'
    _description = 'Thông tin chiết về nhập xuất'

    nxct_nx_id = fields.Many2one(comodel_name='tabas.nhapxuat', string='Số Nhập xuất')
    nxct_sp_id = fields.Many2one(comodel_name='tabas.sanpham', string='Sản phẩm')
    nxct_dvt_id = fields.Many2one(comodel_name='tabas.donvitinh', string='Đơn Vị Tính')
    nxct_sl = fields.Float(string='Số Lượng')
    nxct_dongia = fields.Float(string='Đ. Giá')
    nxct_ck = fields.Float(string='% CK')
    nxct_tienck = fields.Float(compute='_set_tienCK', store=True, string='Tiền CK')  #
    nxct_thanhtien = fields.Float(compute='_set_thanhtien', store=True, string='T. Tiền')  #
    nxct_tiensauck = fields.Float(string='Tiền sau CK')

    @api.depends('nxct_tienck', 'nxct_dongia', 'nxct_sl', 'nxct_ck')
    def _set_tienCK(seft):
        #seft.ensure_one()
        for i in seft:
            i.nxct_tienck = ((i.nxct_sl * i.nxct_dongia) * i.nxct_ck)/100

    @api.onchange('nxct_tienck', 'nxct_dongia', 'nxct_sl', 'nxct_ck')
    def _set_tienCK_1(seft):
        seft._set_tienCK()

    @api.depends('nxct_tienck', 'nxct_dongia', 'nxct_sl', 'nxct_ck')
    def _set_thanhtien(self):
        #self.ensure_one()
        # ls_order = self.order_ids
        for i in self:
            i.nxct_thanhtien = (i.nxct_dongia * i.nxct_sl) - i.nxct_tienck

    @api.onchange('nxct_tienck', 'nxct_dongia', 'nxct_sl', 'nxct_ck')
    def _set_thanhtien_1(self):
        self._set_tienCK()

    @api.depends('nxct_tienck', 'nxct_dongia', 'nxct_sl', 'nxct_ck')
    def _set_tienhang(seft):
        tienhang = 0
        for nxct in seft:
             tienhang += sum(nxct.nxct_sl * nxct.nxct_dongia)
        seft.nxct_nx_id.nx_tienhang = tienhang