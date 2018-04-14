from flask import Flask , request,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/new/')
def query_string(day='all days'):
    query_val=request.args.get('day',day)
    return " <h1>The day is wonderful : {0} </h1>".format(query_val)





if __name__ == '__main__':
    app.run()
