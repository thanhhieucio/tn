from odoo import api, models, fields


class khachhang(models.Model):
    _name = 'tabas.khachhang'
    _description = 'Thông tin khách hàng và NCC'

    name = fields.Char(string='Tên khách hàng')
    kh_code = fields.Char(string='Mã Khách Hàng')
    kh_description = fields.Text(string='Ghi Chú')
    kh_diachi = fields.Text('Địa chỉ')
    kh_kv_id = fields.Many2one(comodel_name="tabas.khuvuc", string="Khu vực")
    kh_loai = fields.Selection(selection=[('1', 'NCC'), ('2', 'Khách Hàng'), ('3', 'Nhân Viên')])
    kh_tel = fields.Char(string='Điện thoại')
    kh_nx_id = fields.One2many(comodel_name='tabas.nhapxuat', inverse_name='nx_kh_id', string='Nhập Xuất')

    _sql_constraints = [
        # ('check_unique_tel', 'UNIQUE(kh_tel)',
        #  'Số điện thoại khách hàng đã tồn tại !'),
        # ('check_unique_code', 'UNIQUE(kh_code)', 'Mã Code khách hàng đã tồn tại !'),
        # ('check_unique_tenkh', 'UNIQUE(name)' or 'UNIQUE(kh_diachi)','Khách hàng đã tồn tại  [Trùng tên và địa chỉ] !'),
        #====================================================================================================================

    ]
