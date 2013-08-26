import json
from area_chart import *
from line_chart import *
from pie_chart  import *
from bar_chart  import *


# sample area_chart_config
# { 'title': "Sample Area Chart", 'xAxis.categories': ["Key1", "Key2", "Key3"], 'series': }

def set_val(json_obj, raw_key, val):
    traversable_key_list = raw_key.strip().split('.')
    scope = json_obj
    for index, sub_key in enumerate(traversable_key_list):
        if index == len(traversable_key_list)-1:
            scope[sub_key] = val
            continue
        if sub_key in scope:
            scope = scope[sub_key]
        else:
            scope[sub_key] = {}
    return json_obj



options =   {
                'line': line_chart,
                'area': area_chart,
                'pie' : pie_chart,
                'bar' : bar_chart
            }

data = { 'title': "Sample Area Chart", 'xAxis.categories': ["Key1", "Key2", "Key3"], 'series': [1, 2, 3]}


def construct_obj(config_data, chart_type):
    formed_obj = template = options[chart_type]
    for key in config_data:
        formed_obj = set_val(formed_obj, key, config_data[key])
    return formed_obj


