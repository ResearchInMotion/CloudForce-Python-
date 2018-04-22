from flask import Flask , request,render_template

app = Flask(__name__)

@app.route('/filters')
def filter_data():
    movies_dict={'Sahil':23.098,
          'nikki':21.563,
          'Vimal':56.675,
          'Manju':54.675,
           'Tayaji':65.7363,
            'Amma':90.3432}
    return render_template('filter_data.html',movies=movies_dict,name=None,film='a christmes carol')



if __name__ == '__main__':
    app.run(debug=True)