from flask import Flask , request,render_template

app = Flask(__name__)


@app.route('/website')
def html():
    return render_template('hello.html')    

@app.route('/Movie')
def movies():
    movie_list=['harry potter','pink floyd','Army','Peter gade','kabadi bazaar']
    return render_template('movies.html',movies=movie_list,name='kill')





if __name__ == '__main__':
    app.run(debug=True)