from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.exceptions import ValidationError
from datetime import datetime
import base64
import io
from PIL import Image


class ReportEmployeeXlsx(models.TransientModel):
    _name = 'report.employee.xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def set_column_size(self):
        self.sheet.set_column('A:A', 25)
        self.sheet.set_column('B:B', 20)
        self.sheet.set_column('C:C', 20)
        self.sheet.set_column('D:D', 12)
        self.sheet.set_column('E:E', 20)

    def generate_xlsx_report(self, workbook, data, objects):
        self.sheet = workbook.add_worksheet('Report')

        self.sheet.set_paper(9)
        self.sheet.set_margins(left=0.5, right=0.2)
        self.sheet.fit_to_pages(1, 0)

        result = self.get_data()
        self.report_format(workbook)
        self.set_column_size()

        # self.generate_header()

        row = 2
        # table header line
        self.sheet.write(row, 0, 'Employee Name', self.format_table_header)
        self.sheet.write(row, 1, 'Phone', self.format_table_header)
        self.sheet.write(row, 2, 'Address', self.format_table_header)
        self.sheet.write(row, 3, 'Year', self.format_table_header)
        self.sheet.write(row, 4, 'Benefit', self.format_table_header)

        # table body
        for line in result:
            row += 1
            self.sheet.write(row, 0, line[0], self.format_wrap)
            self.sheet.write(row, 1, line[1], self.format_wrap)
            self.sheet.write(row, 2, line[2], self.format_wrap)
            self.sheet.write(row, 3, line[3], self.format_decimal_number)
            self.sheet.write(row, 4, line[4], self.format_decimal_number)

    def get_data(self):
        _query = """
            SELECT name, phone, address, income_year, benefit FROM employee
        """

        self.env.cr.execute(_query)

        data = self.env.cr.fetchall()
        return data

    def report_format(self, workbook):
        # common for all
        workbook.formats[0].set_font_size(10)
        workbook.formats[0].set_font_name('Times New Roman')

        format_config = {
            'font_name': 'Times New Roman',
            'font_size': 10,
            'valign': 'vcenter'
        }
        self.format_default = workbook.add_format(format_config)
        #############################################
        format_top_header = format_config.copy()
        format_top_header.update({
            'font_name': 'Times New Roman',
            'align': 'left',
            'bold': True,
            'font_size': 10,
        })
        self.format_top_header = workbook.add_format(
            format_top_header)
        #############################################
        format_table_header = format_config.copy()
        format_table_header.update({
            'bold': True,
            'text_wrap': True,
            'align': 'center',
            'top': 1,
            'bottom': 1,
        })
        self.format_table_header = workbook.add_format(format_table_header)
        #############################################
        format_wrap = format_config.copy()
        format_wrap.update({
            'text_wrap': True,
        })
        self.format_wrap = workbook.add_format(format_wrap)
        #############################################
        format_decimal_number = format_config.copy()
        format_decimal_number.update({
            'num_format': '#,##0.00'
        })
        self.format_decimal_number = workbook.add_format(
            format_decimal_number)
        #############################################
        format_summary = format_config.copy()
        format_summary.update({
            'bold': True,
            'num_format': '#,##0.00',
            'top': 1,
            'bottom': 1,
        })
        self.format_summary = workbook.add_format(
            format_summary)
        #############################################
        format_qty_summary = format_config.copy()
        format_qty_summary.update({
            'bold': True,
            'num_format': '#,##0',
            'top': 1,
            'bottom': 1,
        })
        self.format_qty_summary = workbook.add_format(
            format_qty_summary)
        #############################################
        format_summary_title = format_config.copy()
        format_summary_title.update({
            'bold': True,
            'align': 'right',
        })
        self.format_summary_title = workbook.add_format(format_summary_title)
