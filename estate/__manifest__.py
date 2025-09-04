{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Thibaut Colnot",
    'category': 'Tutorials',
    'description': """
    An Odoo tutorial application for managing real estate.
    """,
    'data': [
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'security/ir.model.access.csv'
    ],
    'application': True
}
