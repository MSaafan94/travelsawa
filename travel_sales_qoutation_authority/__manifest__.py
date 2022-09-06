{
    'name': 'travel sales quotation',
    'description': 'sales quatation templete module',
    'category': 'App',
    'version': '12.0',
    'depends': ['base', 'crm','sale','sales_extra_fields','details','sales_team'],
    'data': [
        'security/quotation_templetes_groups.xml',
        'views/quotation_templete_view.xml',
        'views/quotation_edit_for_manager.xml',
        'views/from_expired_to_order_view.xml',
        'views/manager_only_create_vendor.xml',
    ],

}
