{
    'name': 'POS advanced',
    'description': 'pos advanced module',
    'version': '1.0',
    'summary': 'Added refund reasons',
    'author': 'Ajay',
    'category': 'Sales/Point of Sale',
    'depends': ['base', 'point_of_sale', 'hr'],
    'data': ['security/ir.model.access.csv',
             'views/pos_return_reasons_view.xml',
             'views/assets.xml',
             'views/employee_access.xml'
             ],
    'assets': {
       'point_of_sale.assets': [
           'pos_advanced/static/src/view/return_reasons_button.xml',
           'pos_advanced/static/src/view/return_reasons_popup.xml',
           'pos_advanced/static/src/js/return_reason_popup.js',
           'pos_advanced/static/src/view/employee_button.xml',
           'pos_advanced/static/src/js/employee_button.js',
           'pos_advanced/static/src/view/employee_popup.xml',

       ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
