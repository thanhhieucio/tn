from odoo import fields, models


class quanhuyen(models.Model):
    _name = "tabas.quanhuyen"
    _description = "Quận/Huyện"

    name = fields.Char(string="Tên Quận/Huyện")
    qh_code = fields.Char(string="Mã Quận/Huyện")
    qh_description = fields.Text(string="Ghi chú")
    qh_sv_id = fields.One2many(comodel_name="tabas.students", inverse_name="sv_qh_id")
