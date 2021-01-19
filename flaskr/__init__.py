from flask import Flask

def create_app(test_config=None):
    # creates & configures app
    app = Flask(__name__, instance_relative_config=True)
    
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello World!'

    return app
