{
    'name': 'Ngynlabs document templates',
    'category': 'Tools',
    'version': '10.0.1.0.0',
    'description': """
Ngynlabs documents
==================

This module provides templates for documents (invoice and more).
""",
    'depends': [
        'base',
        'account',
    ],
    'installable': True,
    'data': [
        'views/external_layout_footer.xml',
        'views/external_layout_header.xml',
        'views/report_invoice_document.xml',
    ],
    'author': 'Antoine Nguyen, NGYNLABS',
    'license': 'AGPL-3',
}
