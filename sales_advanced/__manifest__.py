{
    'name': 'Custom Sales App',
    'description': 'Customized Sales App',
    'version': '1.0',
    'summary': 'A sales order must be approved if the discount is greater than 5% only after that confirm the order',
    'author': 'Ajay',
    'category': 'Sales',
    'depends': ['sale'],
    'data': [
        'security/approve_discount.xml',
        'views/inherited_sale_order_views.xml',
    ],
    'js': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
