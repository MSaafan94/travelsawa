# -*- coding: utf-8 -*-
{
    'name': "Travel Dashboard",

    'summary': """
    """,

    'description': """
        Travel Dashboard v12.0,
    """,

    'author': "Saafan",
    'license': 'OPL-1',
    'currency': 'EUR',
    'price': 158.0,
    'website': "https://www.checkmate.com",
    'maintainer': 'Ksolves India Pvt. Ltd.',
    'live_test_url': 'https://checkmate.com',
    'category': 'Tools',
    'version': '6.1.1',
    'images': ['static/description/banner.gif'],

    'depends': ['base', 'web', 'base_setup'],

    'data': [
        'security/ir.model.access.csv',
        'security/ks_security_groups.xml',
        'data/ks_default_data.xml',
        'views/ks_dashboard_ninja_view.xml',
        'views/ks_dashboard_ninja_item_view.xml',
        'views/ks_dashboard_ninja_assets.xml',
        'views/ks_dashboard_action.xml',
    ],

    'qweb': [
        'static/src/xml/ks_dashboard_ninja_templates.xml',
        'static/src/xml/ks_dashboard_ninja_item_templates.xml',
        'static/src/xml/ks_dashboard_ninja_item_theme.xml',
        'static/src/xml/ks_widget_toggle.xml',
        'static/src/xml/ks_dashboard_pro.xml',
        'static/src/xml/ks_import_list_view_template.xml',
        'static/src/xml/ks_quick_edit_view.xml',
    ],

    'demo': [
        'demo/ks_dashboard_ninja_demo.xml',
    ],

    'uninstall_hook': 'uninstall_hook',

}
