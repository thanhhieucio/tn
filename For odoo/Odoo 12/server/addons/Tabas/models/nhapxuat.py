from odoo import models, api, fields


# new_field_id = fields.Many2one(comodel_name="", string="", required=False, )
# new_field_ids = fields.One2many(comodel_name="", inverse_name="", string="", required=False, )

class Nhapxuat(models.Model):
    _name = 'tabas.nhapxuat'
    _description = 'Thông tin nhập xuất - khách hàng'

    name = fields.Char(string='Hóa đơn')
    nx_code = fields.Char(string='Số HĐ')
    nx_ngay = fields.Datetime(string='Ngày NX', default=lambda self: fields.datetime.now())
    nx_kh_id = fields.Many2one(comodel_name='tabas.khachhang', string='Tên Khách Hàng')
    nx_dc = fields.Text(compute='get_dc', string='Địa chỉ', store=False)
    nx_nxct_id = fields.One2many(comodel_name='tabas.nhapxuatchitiet', inverse_name="nxct_nx_id", string='Thông tin chi tiết nhập xuất')

    @api.onchange('nx_kh_id')
    def get_dc(self):
        kh = self.env['tabas.khachhang'].search([('kh_nx_id', '=', self.nx_kh_id)])
        self.nx_dc = "Chưa xác định"

# @api.onchange('level')
#     def onchange_kh(self):
#         print(self.level)
