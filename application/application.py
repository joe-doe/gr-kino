from flask_login import LoginManager


class ApplicationCore(object):

    def __init__(self, app):
        self.initialize_login(app)

    def initialize_login(self, app):
        self.login_manager = LoginManager()
        self.login_manager.init_app(app)
        self.login_manager.login_view = 'login'
