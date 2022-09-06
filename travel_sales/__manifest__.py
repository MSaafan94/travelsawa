# -*- coding: utf-8 -*-
{
    'name': "TravelSwa Sales",

    'depends': ['base','sale_management','account','sales_extra_fields','sale_stock','account'],


    'data': [
        'security/ir.model.access.csv',
        'wizards/payment_wizard.xml',
        'views/sale_order_option.xml',
        'views/payment_count.xml',
        'views/account_payment.xml',
        'views/account_payment_receipt.xml',
        'views/sale_report.xml',
        'views/sale_report_views.xml',
        'views/account_payment_cashout.xml',
        'views/account_payment_cashout_templ.xml',
        'data/ir_cron.xml',
    ],

}