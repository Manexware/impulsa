{
    'name': 'Impulsa',
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
    ],
    'demo': [

    ],
    'data': [
        # 'security/sie_security.xml',
        'security/ir.model.access.csv',
        'menu/sie_menu.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
