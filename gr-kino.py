from flask import Flask
from controllers.routes import Routes
from application.application import ApplicationCore

app = Flask(__name__,
            template_folder='view/web-assets/templates',
            static_folder='view/web-assets/static'
            )

app.secret_key = 'secret'
app.config.from_pyfile('config.py')

app_core = ApplicationCore(app)
routes = Routes(app)

if __name__ == '__main__':
    app.run(debug=True)
