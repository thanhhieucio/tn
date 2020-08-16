# -*- coding: utf-8 -*-

from odoo import api, fields, models


class OrderReportWizard(models.TransientModel):
    _name = "order.report.wizard"

    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')

    def print_order_report(self, data):
        # data['form'].update(self.read(['date_from_cmp', 'debit_credit', 'date_to_cmp', 'filter_cmp', 'account_report_id', 'enable_filter', 'label_filter', 'target_move'])[0])
        self.env.cr.execute("""
            SELECT id FROM orders WHERE create_date BETWEEN '%s' AND '%s'
        """ % (self.date_from, self.date_to))
        result = self.env.cr.fetchall()
        ids = []
        for id in result:
            ids.append(id[0])
        print(ids)
        # orders = self.env['orders'].browse(result)
        return self.env.ref('odoo_learn_inherit.action_report_order').report_action(
            docids=ids, data=None, config=False)
