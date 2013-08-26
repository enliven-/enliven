from flask import Flask, request, render_template, jsonify
from lib.lib import construct_obj, update_config

app = Flask(__name__)


@app.route('/')
def pie_view():
    return render_template("index.html")

# ---------------------------------pie---------------------------------------------

@app.route('/pieobj')
def pie_obj():
    config = {
                'title.text' : "Language distribution",
                'tooltip.pointFormat' : "{series.name}: <b>{point.percentage:.1f}%</b>",
                'plotOptions.pie.dataLabels.format': "<b>{point.name}</b>: {point.percentage:.1f} %",
                'series': [{
                            'type': 'pie',
                            'name': 'Language share',
                            'data': [
                                        ['Javascript',   45.0],
                                        ['Python',       26.8],
                                        {
                                            'name': 'Ruby',
                                            'y': 12.8,
                                            'sliced': True,
                                            'selected': True
                                        },
                                        ['Java',    8.5],
                                        ['Lua',     6.2],
                                        ['Others',   0.7]
                                    ]
                          }]
            }
    pie_obj = construct_obj(config, 'pie')
    return jsonify(pie_obj)

# -------------------------------------area-----------------------------------------


@app.route('/areaobj')
def area_obj():
    config =    {
                    'title.text'        : "Score over time",
                    'xAxis.categories'  : ["2001", "2002", "2003", "2004", "2005"],
                    'series'            : [{
                                            'name' : "Score",
                                            'data' : [32, 54, 65, 103, 135]
                                          }] 
                }
    area_obj = construct_obj(config, 'area')
    return jsonify(area_obj)

# -----------------------------------bar-------------------------------------------


@app.route('/barobj')
def bar_obj():
    config =    {
                    'title.text' : "Interpreted Characterstics",
                    'xAxis'      : {
                                    'categories' : ["Creativity", "Contributor", "Team-worker", "Honed-Skillset", "Allround-ninja"],
                                   },
                    'series'     : [{
                                        'name' : 'John',
                                        'data' : [107, 31, 635, 203, 2]
                                   }, {
                                        'name' : 'Jessica',
                                        'data' : [133, 156, 947, 408, 6]
                                   }]   
                }
    bar_obj = construct_obj(config, 'bar')
    return jsonify(bar_obj)






# --------------------------------------line----------------------------------------

@app.route('/lineobj')
def line_obj():
    config =    {
                    'title' :   {
                                    'text'  : "Reputation/time over time",
                                    'x'     : -20
                                },
                    'xAxis.categories' : ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                    'series':   [{
                                    'name' : "Stackoverflow",
                                    'data' : [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
                                }, {
                                    'name' : "HackerNews",
                                    'data' : [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
                                }, {
                                    'name' : "Top Coder",
                                    'data' : [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
                                }]
                }
    line_obj = construct_obj(config, 'line')
    return jsonify(line_obj)                





if __name__ == '__main__':
    app.run(debug=True)