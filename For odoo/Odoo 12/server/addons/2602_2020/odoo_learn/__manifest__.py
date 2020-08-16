{
    'name': 'Odoo Learn 1',
    'version': '1',
    'summary': '',
    'sequence': 1,
    'description': '',
    'category': '',
    'author': '',
    'website': '',
    'license': '',
    'depends': [
        'base',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'views/employee_view.xml',
        'views/department_view.xml',
        'views/orders_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}