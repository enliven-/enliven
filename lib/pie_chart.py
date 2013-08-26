pie_chart = {
                'chart': {
                    'plotBackgroundColor': None,
                    'plotBorderWidth': None,
                    'plotShadow': False
                },
                'title': {
                    'text': None
                },
                'tooltip': {
                    'pointFormat': None #'{series.name'}:' <b>{point.'percentage':.1f}%</b>'
                },
                'plotOptions': {
                    'pie': {
                        'allowPointSelect': True,
                        'cursor': 'pointer',
                        'dataLabels': {
                            'enabled': True,
                            'color': '#000000',
                            'connectorColor': '#000000',
                            'format': None #'<b>{point.name}</b'>:' {point.'percentage':.1f} %'
                        }
                    }
                },
                'series': [{
                    'type': 'pie',
                    'name': None,
                    'data': None # []
                }]
            }