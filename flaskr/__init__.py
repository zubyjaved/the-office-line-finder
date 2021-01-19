from flask import Flask, render_template, request

def create_app(test_config=None):
    # creates & configures app
    app = Flask(__name__, instance_relative_config=True)
    
    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/results', methods=['POST'])
    def results():
        return request.form['inputTxt']

    return app
