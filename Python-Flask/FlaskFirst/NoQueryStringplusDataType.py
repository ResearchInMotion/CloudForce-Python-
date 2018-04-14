from flask import Flask

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user')
@app.route('/user/<name>')
def no_query(name='nikki'):
    return "hello there ! {}".format(name)



#Strings Only


@app.route('/text/<string:name>')   # here the name is the string type
def working_with_string(name):
    return "hi there is a string "+ name

#Integers Only
@app.route('/number/<int:num>')   # here the num is integer type
def working_with_integer(num):
    return "The salary is "+str(num)

#Multipple Integers
@app.route('/multiple/<int:num1>/<int:num2>')  # here the num is integer type
def more_integer(num1,num2):
    return "the addition is  {} ".format(num1+num2)


#float

@app.route('/float/<float:num1>/<float:num2>')
def floatvalue(num1,num2):
    return "the addition of float is {} ".format(num1+num2)



if __name__ == '__main__':
    app.run()
