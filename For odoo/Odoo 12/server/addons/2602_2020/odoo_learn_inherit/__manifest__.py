{
    'name': 'Odoo learn inherit',
    'version': '1',
    'summary': '',
    'sequence': 1,
    'description': '',
    'category': '',
    'author': '',
    'website': '',
    'license': '',
    'depends': [
        'sale',
        'odoo_learn',
    ],
    'data': [
        'data/data.xml',
        'wizard/employee_wizard_view.xml',

        'views/res_partner_view.xml',
        'views/employee_view.xml',
        'views/orders_view.xml',

        'report/order_report.xml',
        'wizard/order_report_wizard_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True
}