from flask import Flask, request,render_template

from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)

# app.config.update(
#
#     SECRET_KEY='root',
#     SQLALCHEMY_DATABASE_URI='postgresql://postgres:root@localhost/catalog_db',
#     SQLAlchemy_TRACK_NOTIFICATION=False
#
# )


app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:root@localhost/catalog_db'

db=SQLAlchemy(app)



class Publication(db.Model):
    __tablename__: 'publication'



    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80), nullable=False)


    def __init__(self,id,name):
        self.id=id
        self.name=name

    def __repr__(self):
        return 'The id is {} , Name is {} '.format(self.id,self.name)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)