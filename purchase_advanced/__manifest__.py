{
    'name': 'Custom Purchase App',
    'description': 'Customized Purchase App',
    'version': '1.0',
    'summary': 'Custom fields and signature in purchase app',
    'author': 'Ajay',
    'category': 'Inventory',
    'depends': ['purchase', 'base'],
    'data': [
        'views/new_purchase_order_form.xml',
        'report/new_purchase_order_template.xml',
    ],
    'category': 'Inventory/Purchase',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
