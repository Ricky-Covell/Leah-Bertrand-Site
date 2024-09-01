import os

from flask import Flask, render_template, jsonify, request, flash, redirect, session, url_for, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from models import db, connect_db, Work, Performance
from forms import UserAddForm, LoginForm

CURR_USER_KEY = "curr_user"

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql://leah_user:VMrcPl0kd06Lk703K1ohdmSayrI84T7D@dpg-cr9uu056l47c73cv32qg-a/leah'))
    # os.environ.get('DATABASE_URL', 'postgresql:///leah'))

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
    performances = Performance.query.all()
    
    return render_template('landing.html', works=works, performances=performances) 




# # # # # # # # # # # # # # # # WORKS ROUTES # # # # # # # # # # # # # # # # # # # # 
@app.route('/works', methods=["GET"])
def works_index(): 

    works = Work.query.all()
    performances = Performance.query.all()

    return render_template('/works/works-index.html', works=works, performances=performances)




# # # # # # # # # # # # # # # # API ROUTES # # # # # # # # # # # # # # # # # # # # 
@app.route('/api/work/<work_id>', methods=["GET"])
def show_work(work_id): 

    work = Work.query.get_or_404(work_id)
    return jsonify(work=work.serialize())

@app.route('/api/work/<work_id>', methods=["GET"])
def edit_work(work_id): 

    work = Work.query.get_or_404(work_id)
    return jsonify(work=work.serialize())













                                            # # # # # # # # # # # # # # # # FUTURE UPDATES # # # # # # # # # # # # # # # # # # # # 


# # # # # # # # # # # # # # # # ADMIN LOGIN # # # # # # # # # # # # # # # # # # # # 
# @app.before_request
# def add_user_to_g():
#     """If we're logged in, add curr user to Flask global."""

#     if CURR_USER_KEY in session:
#         g.admin = Admin.query.get(session[CURR_USER_KEY])

#     else:
#         g.admin = None


# def do_login(admin):
#     """Log in user."""

#     session[CURR_USER_KEY] = admin.id


# def do_logout():
#     """Logout user."""

#     if CURR_USER_KEY in session:
#         del session[CURR_USER_KEY]


# # # # # # # # # # # # # # # # ADMIN ROUTES # # # # # # # # # # # # # # # # # # # # 
# @app.route('/', subdomain ='admin', methods=["GET"])
# @app.route('/admin/add', methods=["GET", "POST"])
# def admin_page(): 

# @app.route('/admin/add', methods=["GET", "POST"])
# def admin_add(): 

#     form = UserAddForm()

#     if form.validate_on_submit():
#         try:
#             admin = Admin.signup(
#                 username=form.username.data,
#                 password=form.password.data,
#             )
#             db.session.commit()

#         except IntegrityError:
#             flash("Username already taken", 'danger')
#             return render_template('admin-add.html', form=form)

#         do_login(admin)

#         return redirect("/admin")

#     else:
#         return render_template('admin-add.html', form=form)
    


# @app.route('/admin/login', methods=["GET", "POST"])
# def admin_login():
#     """Handle admin login."""
#     if g.admin:
#         return redirect("/admin/edit")

#     form = LoginForm()

#     if form.validate_on_submit():
#         admin = Admin.authenticate(form.username.data,
#                                  form.password.data)

#         if admin:
#             do_login(admin)
#             return redirect("/admin/edit")

#         flash("Invalid credentials.", 'danger')

#     return render_template('admin-login.html', form=form)



# @app.route('/admin/edit', methods=["GET", "POST"])
# def edit_site():
#     """Handle admin login."""
#     if not g.admin:
#         return redirect("/")

#     return render_template('edit-site.html')








   
