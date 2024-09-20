import os

import json
from flask import Flask, render_template, jsonify, request, flash, redirect, session, url_for, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError, NoSuchTableError

from seed import seed_database, seed_db_if_empty
from models import db, connect_db, Work, Performance, Admin, Appearance
from forms import UserAddForm, LoginForm, EditForm



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
     os.environ.get('DATABASE_URL', 'postgresql://leah_user:VMrcPl0kd06Lk703K1ohdmSayrI84T7D@dpg-cr9uu056l47c73cv32qg-a/leah'))
    #  os.environ.get('DATABASE_URL', 'postgresql:///leah'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['FLASK_RUN_HOST'] = os.environ.get('FLASK_RUN_HOST', '0.0.0.0')
app.config['FLASK_RUN_PORT'] = os.environ.get('FLASK_RUN_PORT', '10000')

toolbar = DebugToolbarExtension(app)
CURR_USER_KEY = "curr_user"

app.app_context().push()
connect_db(app)

# reseeds when server is restarted
db.drop_all()  
seed_db_if_empty()

# if __name__ == '__main__':
#       app.run(host='0.0.0.0', port=10000)


# # # # # # # # # # # # # # # # BEFORE # # # # # # # # # # # # # # # # # # # # 
@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.admin = Admin.query.get(session[CURR_USER_KEY])

    else:
        g.admin = None


def do_login(admin):
    """Log in user."""

    session[CURR_USER_KEY] = admin.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]



# # # # # # # # # # # LOGIN ADMIN AUTOMATICALLY FOR HATCHWAY REVIEW # # # # # # # # # # # # # # #  
@app.before_request
def auto_login():
    if not CURR_USER_KEY in session:
        admin = Admin.authenticate('Leah', 'Leah')
        do_login(admin)     # Username&Password = Leah



# # # # # # # # # # # # # # # # GENERAL ROUTES # # # # # # # # # # # # # # # # # # # # 
@app.route('/', methods=["GET"])
def landing(): 

    isAdmin = 'False'
    if (g.admin is not None):
        isAdmin = 'True'


    works = Work.query.all()
    performances = Performance.query.all()
    appearances = Appearance.query.all()
    
    return render_template('landing.html', works=works, performances=performances, appearances=appearances, isAdmin=isAdmin) 




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





# # # # # # # # # # # # # # # # ADMIN ROUTES # # # # # # # # # # # # # # # # # # # # 
@app.route('/login', methods=["GET", "POST"])
def admin_login():
    """Handle admin login."""
    if g.admin:
        return redirect("/edit")

    form = LoginForm()

    if form.validate_on_submit():
        admin = Admin.authenticate(form.username.data,
                                 form.password.data)

        if admin:
            do_login(admin)
            return redirect("/edit")

        flash("Invalid credentials.", 'danger')

    return render_template('admin-login.html', form=form)



@app.route('/logout', methods=["GET", "POST"])
def admin_logout():
    """Handle admin login."""
    if g.admin:
        do_logout()
        return redirect("/")


    return redirect("/")



@app.route('/edit', methods=["GET", "POST"])
def edit_site():
    """Handle admin login."""
    if not g.admin:
        return redirect("/")

    appearances = Appearance.query.all()
    works = Work.query.all()
    form = EditForm()

    if form.validate_on_submit():
        appearances[0].background_color = form.background_color.data
        appearances[0].background_blur = form.background_blur.data
        appearances[0].inset_color = form.inset_color.data
        appearances[0].soundcloud_color = form.soundcloud_color.data
        appearances[0].accent_color = form.accent_color.data
        appearances[0].fluid_color_1 = form.fluid_color_1.data
        appearances[0].fluid_color_2 = form.fluid_color_2.data
        appearances[0].fluid_color_3 = form.fluid_color_3.data
        appearances[0].fluid_color_4 = form.fluid_color_4.data
        appearances[0].fluid_color_5 = form.fluid_color_5.data
        appearances[0].fluid_hue_rotate = form.fluid_hue_rotate.data
        appearances[0].fluid_grayscale = form.fluid_grayscale.data
        appearances[0].fluid_brightness = form.fluid_brightness.data
        appearances[0].fluid_blur = form.fluid_blur.data
        appearances[0].fluid_opacity = form.fluid_opacity.data
        appearances[0].fluid_invert = form.fluid_invert.data

        db.session.commit()
            
        return redirect('/')

    return render_template('edit-site.html', works=works, form=form, appearances=appearances)






   
