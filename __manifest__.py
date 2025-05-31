{
    'name': 'Cemic Website & Portal Base',
    'version': '1.0',
    'category': 'Website/Theme',
    'summary': 'Base content and configurations for Cemic',
    'depends': ['website', 'website_crm', 'helpdesk'],
    'data': [
        'data/page.xml',
        # 'views/pages.xml',
        'views/snippets/s_desenvolvimento_agil.xml',
        'views/snippets/s_nossa_cultura.xml',
        'views/snippets/snippets.xml',

        'views/hello_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'cemic_website_portal/static/src/css/cemic_website_portal.scss',
            'cemic_website_portal/static/src/js/cemic_website_portal.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}