from odoo import models, fields, api


class nhomsanpham(models.Model):
    _name = 'tabas.nhomsanpham'
    _description = 'Thông tin nhóm sản phẩm 1- N SP'
    name = fields.Char(string='Name')
    nsp_code = fields.Char(string='Code')
    nsp_description = fields.Text(string='Description')
    nsp_cock = fields.Float(string='COCK')
    nsp_summary = fields.Float(string='summary - Product')
    nsp_sp_id = fields.One2many(comodel_name='tabas.sanpham',
                                inverse_name='sp_nsp_id',
                                string='Sản phẩm')

    #@api.multi
    def write(self, vals):
        name = vals.get('name', False)
        if name:
            vals['name'] = name.title()
        result = super(nhomsanpham, self).write(vals)
        return result
