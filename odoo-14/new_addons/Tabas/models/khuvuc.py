from odoo import  fields, models


class Khuvuc(models.Model):
    _name = "tabas.khuvuc"
    _description = "Khu vực khách hàng"

    name = fields.Char(string="Tên khu vực")
    kv_code = fields.Char(string="Mã Khu vực")
    kv_description = fields.Text(string="Ghi chú")
    kv_loai = fields.Selection(selection=[('1', 'Thành Phố'), ('2', 'Quận Huyện'), ('3', 'Khác')])
    kv_kh_id = fields.One2many(comodel_name="tabas.khachhang", inverse_name="kh_kv_id")