# -*- coding: utf-8 -*-
{
    'name': 'Advance Date Filter And Group By',
    'version': '1.0',
    'category': 'Tools',
    'author': 'FreelancerApps',
    'summary': 'Advance Date Filter Tomorrow, Today, Yesterday, Current Week, Last 7 days, Last Week, Current Month, Last 30 Days, Last Month, Current Year, Last 365 Days, Last Year, And Group By Week, Month, Year',
    'depends': ['sale', 'crm', 'crm_claim', 'purchase', 'project', 'account', 'stock'],
    'description': """
Advance Date Filters And Group By
=================================
* Advance Date Filters Tomorrow, Today, Yesterday, Current Week, Last 7 days, Last Week, Current Month, Last 30 Days, Last Month, Current Year, Last 365 Days, Last Year.
* Group By
* Week, Month, Year'
""",
    'data': [
        'security/advance_date_filter_security.xml',
        'views/sale_filter.xml',
        'views/logged_calls_filter.xml',
        'views/claim_filter.xml',
        'views/task_filter.xml',
        'views/invoice_filter.xml',
        'views/purchase_filter.xml',
        'views/picking_filter.xml',
        'views/move_filter.xml',
    ],
    'images': ['static/description/advance_date_filter_group_banner.png'],
    'price': 9.99,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'installable': True,
    'auto_install': False,
}
