from flask import Flask , request , render_template

app = Flask(__name__)

@app.route('/temp')
def htmlTemplate():
    return render_template('hello.html')


if __name__=='_main_':
    app.run(debug=True)