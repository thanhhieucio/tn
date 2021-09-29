from odoo import models, fields, api


class Sanpham(models.Model):
    _name = 'tabas.sanpham'
    _description = 'Thông tin sản phẩm'

    name = fields.Char(string='Tên sản phẩm')
    sp_ma = fields.Char(string='Mã sản phẩm')
    sp_dv_id = fields.Many2one(comodel_name='tabas.donvitinh', string='Đơn vị')
    sp_gianhap = fields.Float(string='Giá Nhập')
    sp_giaxuat = fields.Float(string='Giá Xuất')
    sp_giaxuat1 = fields.Float(string='Giá Xuất 1')
    sp_giaxuat2 = fields.Float(string='Giá Xuất 2')
    sp_tondinhmuc = fields.Float(string='Tồn Định Mức')
    sp_tonthucte = fields.Float(compute='get_tonthucte', string='Tồn kho', store=True)
    sp_hinhanh = fields.Binary(string="Attachment")
    sp_store_fname = fields.Char(string="File Name", type="jpg,png")
    sp_nsp_id = fields.Many2one(comodel_name='tabas.nhomsanpham', string='Nhóm sản phẩm')

    _sql_constraints = [
        ('check_unique_nsp', 'UNIQUE(sp_ma)',
         'Mã sản phẩm đã tồn tại vui lòng chọn mã khác !'),
    ]

    #@api.multi
    def get_tonthucte(self):
        # lấy tồn trong nhập - xuất đưa vào đây
        #self.ensure_one()
        for sp in self:
            sp.sp_tonthucte = 10000000

    #@api.multi
    def write(self, vals):
        name = vals.get('name', False)
        if name:
            vals['name'] = name.title()
        result = super(Sanpham, self).write(vals)

        # print(self.sp_dv_id('name'))
        # # for emp in self:
        # #     emp.with_context({'from': 'write'}).set_working()
        return result


#warning = {
    #             'title': 'This is title',
    #             'message': 'This is message'
    #     #         }
    #
    #         return {'warning': warning}