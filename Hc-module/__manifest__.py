{
    'name': "Books Management",
    'name_vi_VN': "Quản Lý Sách",

    'summary': """
Design Website with SEO
    """,

    'summary_vi_VN': """
Thiết kế Website với chuẩn SEO
    """,

    'description': """
Vu Tuan Hung
Key Features
============

#. Provide information for Schema
#. Remove comment on robots.txt template
#. Add rel options to website editor

Editions Supported
==================
1. Community Edition

    """,

    'description_vi_VN': """
Tính năng chính
===============

#. Cung cấp thông tin cho Schema
#. Bỏ comment trên file mẫu robots.txt
#. Bổ sung thiết lập thuộc tính rel trên trình soạn thảo trang web

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com/apps/app/15.0/viin_website_seo",
    'live_test_url': "https://v15demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v15demo-vn.viindoo.com",
    'support': "apps.support@viindoo.com",
    'category': 'Website',
    'version': '0.1.0',
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/main_views.xml',
        'wizard/edit_name_wizard.xml',
    ],
    'images': [
        'static/description/books.png'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 0.0,
    'currency': 'EUR',
    'license': 'OPL-1',
}
