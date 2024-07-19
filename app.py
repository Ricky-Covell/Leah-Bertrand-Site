import os

from flask import Flask, render_template, jsonify, request, flash, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from models import db, connect_db, Work

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///leah'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

app.app_context().push()
connect_db(app)



# # # # # # # # # # # # # # # # GENERAL ROUTES # # # # # # # # # # # # # # # # # # # # 
@app.route('/', methods=["GET"])
def landing(): 

    works = Work.query.all()

    return render_template('landing.html', works=works) 


@app.route('/about', methods=["GET"])
def about(): 

    return render_template('about.html') 



# # # # # # # # # # # # # # # # WORKS ROUTES # # # # # # # # # # # # # # # # # # # # 
@app.route('/works', methods=["GET"])
def works_index(): 

    works = Work.query.all()

    return render_template('/works/works-index.html', works=works)




# # # # # # # # # # # # # # # # API ROUTES # # # # # # # # # # # # # # # # # # # # 
@app.route('/api/work/<work_id>', methods=["GET"])
def show_work(work_id): 

    work = Work.query.get_or_404(work_id)
    return jsonify(work=work.serialize())




# # # # # # # # # # # # # # # # ADMIN ROUTES # # # # # # # # # # # # # # # # # # # # 

















                                    # PRE API PLAN

# @app.route('/works/<title>', methods=["GET"])
# def show_work(title): 
#     work = Work.query.filter(Work.title == title).one()

#     return render_template('/works/show-work.html', work=work)



# # # # # # # # # # # # # # # # # PERFORMANCE ROUTES # # # # # # # # # # # # # # # # # # # # 
# @app.route('/performances', methods=["GET"])
# def performances_index(): 

#     return render_template('/performances/performances-index.html')


# @app.route('/performances/<title>', methods=["GET"])
# def show_performance(title): 

#     return render_template('/performances/show-performance.html')




   