{
    'name': 'Impulsa Map',
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
    'depends': [
        'impulsa_core',
    ],
    'demo': [

    ],
    'data': [
        'views/schedule_view.xml',
        'views/schedule_inherit_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
