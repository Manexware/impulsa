{
    'name': 'Impulsa Core',
    'version': '1.0',
    'author': 'Manexware S.A.',
    'category': 'Education',
    'website': 'http://www.manexware.com',
    'summary': 'Impulsa Odoo',
    'description': """
        Customer
        Seller
        Schedule

        """,
    'css': [],
    'qweb': [],
    'summernote': [],
    'images': [],
    'depends': ['base',
                'hr',
                'base_geoengine',
    ],
    'demo': [

    ],
    'data': [
        'views/hr_employee_inherit_view.xml',
        'views/res_partner_inherit_view.xml',
        'views/schedule_view.xml',
        'views/schedule_graph_view.xml',
        'security/impulsa_security.xml',
        # 'security/sie_security.xml',
        # 'security/ir.model.access.csv',
        'menu/menu.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
