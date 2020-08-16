# -*- coding: utf-8 -*-

import time
from odoo import api, models, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ReportOrder(models.AbstractModel):
    _name = 'report.odoo_learn_inherit.report_order'

    @api.model
    def format_employee_name(self, name):
        return name.title()

    @api.model
    def get_list_employee(self, order_id):
        self.env.cr.execute("""
            select e.name, e.phone, e.address 
            from orders o 
            inner join order_employee_rel oer on o.id = oer.order_id
            inner join employee e on oer.employee_id = e.id
            where o.id = %s
        """ % (order_id,))
        result = self.env.cr.fetchall()
        # self.env.cr.execute('INSERT or UPDATE')
        # self.env.cr.commit()
        return result or False

    @api.model
    def get_report_values(self, docids, data=None):
        print(docids)
        # docs = self.env['orders'].browse(docids)
        self.env.cr.execute("""
            SELECT * FROM orders
        """)
        result = self.env.cr.fetchall()
        print(result)
        return {
            'doc_ids': docids,
            # 'doc_model': model,
            # 'data': data['form'],
            'docs': False,
            'list_order': result,
            'get_list_employee': self.get_list_employee,
            'format_employee_name': self.format_employee_name,
            # 'time': time,
            # 'get_partner_lines': movelines,
            # 'get_direction': total,
        }
