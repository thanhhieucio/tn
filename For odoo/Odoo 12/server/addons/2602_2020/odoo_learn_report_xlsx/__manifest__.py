# -*- coding: utf-8 -*-
# __author__ = 'minhld'

{
    'name': 'Employee Report',
    'version': '1.0.1',
    'category': 'Point Of Sale',
    'sequence': 20,
    'summary': '',
    'description': "",
    'depends': [
        'report_xlsx',
        'odoo_learn',
    ],
    'data': [
        'report/report_employee_xlsx.xml',
    ],
    'installable': True,
    'application': True,
}
