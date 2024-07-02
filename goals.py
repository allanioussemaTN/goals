from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy 
import psycopg2

app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:deathnote12@localhost:5432/goalsdatabase' # configuration to connect to the data base 
app.config['SQLALCHEMY_DATABASE_URI']='postgres://u9lnbdt2s3ls8j:pe739aa98ee6fa5207113555deb77f8aa3a01f192d432650160277dbb5eaf4b97@ccaml3dimis7eh.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/d80b7tbfvanmun'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # take much resource better disable it 

db=SQLAlchemy(app)
class FavGoals(db.Model):
    __tablename__='Goals' 
    id = db.Column('id',db.Integer,primary_key=True)
    deadline= db.Column('deadline',db.String(30))
    goal = db.Column('goal',db.String(50))

@app.route('/') #route decorator is which URL will trigger the function
def index():
    result= FavGoals.query.all() #fetch all data from the database goals and save it in results
    return render_template('index.html',result=result)



@app.route('/goals') #route decorator is which URL will trigger the function
def goals():
    return render_template('goals.html')

@app.route('/process',methods=['GET','POST']) #route decorator is which URL will trigger the function
def process():
    deadline= request.form['Deadline']
    goal= request.form['goal']
    goaldata=FavGoals(deadline=deadline,goal=goal) #store the data in the class used for the data base 
    db.session.add(goaldata)
    db.session.commit()
    return redirect(url_for('index'))
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
    
