from flask import render_template


class Routes(object):

    def __init__(self, app):
        self.initialize(app)

    def initialize(self, app):
        @app.route('/')
        def index():
            return render_template('index.html')
