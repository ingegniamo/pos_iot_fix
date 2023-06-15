# -*- coding: utf-8 -*-
{
    'name': "POS IOT FIX on scale not available",
    
    'summary': "",
  
    'license': 'OPL-1',

    'author': "STeSI Consulting",

    'category': '',
  
    'version': '16.0.0.1',
  
    'website': "http://www.stesi.consulting",

    # any module necessary for this one to work correctly
    'depends': ['pos_iot'],
    'assets': {
        'point_of_sale.assets': [
            'pos_iot_fix/static/src/js/**/*.js',
        ]
    },
    # always loaded
    'data': [],

    'application': False,
}
