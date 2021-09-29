from odoo import fields, models, api


class Noidungthuchi(models.Model):
    _name = 'tabas.noidungthuchi'
    _description = 'Thông tin về nội dung thu chi'

    name = fields.Char(string='Tên nội dung thu chi')
    ndtc_code = fields.Char(string='Mã nội dung')
    ndtc_description = fields.Text(string='Ghi Chú')
    ndtc_hanmuc = fields.Float(string='Hạn mức tối đa')
    state = fields.Selection(selection=[
        ('1', 'Cố định'),
        ('2', 'Tự tạo')], string='Loại', default='draft')


