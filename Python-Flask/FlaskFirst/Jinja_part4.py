from flask import Flask , request,render_template

app = Flask(__name__)

@app.route('/macros')
def macros():

    movies_dict={'Sahil':23,
          'nikki':21,
          'Vimal':56,
          'Manju':54,
           'Tayaji':65,
            'Amma':90}
    return render_template('using_macro.html',movies=movies_dict)










if __name__ == '__main__':
    app.run(debug=True)