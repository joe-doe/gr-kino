from flask import render_template, jsonify
import urllib3
import json


class Routes(object):

    def __init__(self, app):
        self.initialize(app)

    def initialize(self, app):
        @app.route('/')
        def index():
            return render_template('index.html')

        @app.route('/latest-result')
        def latest_result():
            return render_template('updated-tableau.html')

        @app.route('/last-draw')
        def last_draw():
            http = urllib3.PoolManager()
            r = http.request('GET', 'http://applications.opap.gr/DrawsRestServices/kino/last.json')
            d = json.loads(r.data)

            draw_data = d['draw']
            draw_no = draw_data['drawNo']
            draw_time = draw_data['drawTime']
            draw_results = draw_data['results']
            draw_bonus = draw_results[-1]

            return jsonify(draw_data)
