# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'pos2',
    'author': 'Ajay',
    'version' : '1.2',
    'summary': 'pos refund',
    'category': 'Sales/Point of Sale',
    'depends': ['point_of_sale'],
    'data': ['security/ir.model.access.csv', 'views/menu.xml', 'views/patient.xml'],
    'sequence': 10,
    'description': """
Hospital Management System
====================
The specific and easy-to-use hospital management system in Odoo allows you to keep track of your hospital datas.
    """,
    'category': 'Services/Services',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
