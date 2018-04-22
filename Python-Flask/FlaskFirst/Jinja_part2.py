from flask import Flask , request,render_template

app = Flask(__name__)

@app.route('/table')
def movies_plus():
    movies_dict={'Sahil':23,
          'nikki':21,
          'Vimal':56,
          'Manju':54,
           'Tayaji':65,
            'Amma':90}
    return render_template('table_data.html',movies=movies_dict,name='Sahils family')



if __name__ == '__main__':
    app.run(debug=True)