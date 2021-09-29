from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError


class students(models.Model):
    _name = 'tabas.students'
    _description = 'Thông tin Sinh viên'

    name = fields.Char(string='Họ và tên')
    sv_sex = fields.Selection(selection=[('1', 'Nam'), ('2', 'Nữ'), ('3', 'Khác')])
    sv_code = fields.Char(string='Mã')
    sv_ngaysinh = fields.Datetime(string='Ngày Sinh', default=lambda self: fields.datetime.now() - 18)
    sv_kv_id = fields.Many2one(comodel_name="tabas.khuvuc", string="Khu vực")
    sv_nguyenquan = fields.Text('Nguyên Quán')
    sv_tongiao = fields.Text('Tôn giáo')
    sv_cmt = fields.Text('Số CMT/CCCD')
    sv_diachi = fields.Text(string='Địa Chỉ')
    sv_qh_id = fields.Many2one(comodel_name="tabas.quanhuyen", string="Quận Huyện")
    sv_kv_id = fields.Many2one(comodel_name="tabas.khuvuc", string="Khu vực", domain="['kv_loai','=','1' ]")
    sv_loai = fields.Selection(selection=[('1', '1'), ('2', '2'), ('3', '3')])
    sv_tel = fields.Char(string='Điện thoại')
    sv_nx_id = fields.One2many(comodel_name='tabas.nhapxuat', inverse_name='nx_kh_id', string='Nhập Xuất')
    sv_description = fields.Text(string='Ghi Chú')
    sv_email = fields.Char(string='Email')
    sv_fathername = fields.Text(string='Họ Tên Bố')
    sv_fatherBirthDay = fields.Datetime(string='Ngày Sinh')
    sv_fatherBusiness = fields.Text('Nghề Nghiệp')
    sv_fatherOffice = fields.Text('Đơn vị công tác')
    sv_fatherPhone = fields.Char('Tel')
    sv_fatherEmail = fields.Char('Email')
    sv_fatherAdress = fields.Text('Đại Chỉ')
    sv_mothername = fields.Text(string='Họ Tên Bố')
    sv_motherBirthDay = fields.Datetime(string='Ngày Sinh')
    sv_motherBusiness = fields.Text('Nghề Nghiệp')
    sv_motherOffice = fields.Text('Đơn vị công tác')
    sv_motherPhone = fields.Char('Tel')
    sv_motherEmail = fields.Char('Email')
    sv_motherAdress = fields.Text('Đại Chỉ')

    @api.onchange('sv_email', 'sv_fatherEmail', 'sv_motherEmail')
    def validate_mail(self):
        if self.email_id:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email_id)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')
