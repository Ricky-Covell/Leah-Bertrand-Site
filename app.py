import os

from flask import Flask, render_template, jsonify, request, flash, redirect, session, url_for, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

# from seed import seed_database
from models import db, connect_db, Work, Performance
from forms import UserAddForm, LoginForm

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=10000)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    # os.environ.get('DATABASE_URL', 'postgresql://leah_user:VMrcPl0kd06Lk703K1ohdmSayrI84T7D@dpg-cr9uu056l47c73cv32qg-a/leah'))
    os.environ.get('DATABASE_URL', 'postgresql:///leah'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")


toolbar = DebugToolbarExtension(app)


app.app_context().push()
connect_db(app)

db.drop_all()
db.create_all()

work1 = Work(
        title='The wet centre is bottomless', 
        medium='ambisonic fixed media', 
        year='2019', 
        description1='Assembled from field recordings, extracted and synthesized frog advertisement calls, and hybridized and invented species, the work attempts to get at the decentered perspective of an environment. The piece was written alongside a paper for the journal Organised Sound. Higher-order ambisonics (HOA) files available upon request.', 
        description2='', 
        image1='/static/wetCenterSwamp1.jpeg', 
        image2='/static/wetCenterSwamp2.jpg', 
        image3='/static/wetCenterMsp1.png', 
        image4='', 
        soundcloud_header='Stereo Mix', 
        soundcloud_track_id='744445654', 
        downdload_link='',
        img_filter=''
    )
    
work2 = Work(
        title=' Almost an Ocean', 
        medium='stereo fixed media', 
        year='2019', 
        description1='All sounds recorded January 2019 along the south shore of Lake Superior, on travel funded by grants from Oberlin Conservatory and Oberlin Environmental Studies. Produced in collaboration with Isaac Shalit. Image taken on South Bay in Munising, MI. The work is constructed along morphological affinities between the sounds encountered, and its form explores the simultaneous diversity and unity of the little places we came across in this vast soundscape. Over small changes in time or location, the dynamics of ice and water are completely transformed but underlying this stunning diversity are shared tides and conditions.', 
        description2='', 
        image1='/static/almostAnOcean1.jpeg', 
        image2='', 
        image3='', 
        image4='', 
        soundcloud_header='Stereo Mix', 
        soundcloud_track_id='583136832', 
        downdload_link='',
        img_filter=''
    )
    
work3 = Work(
        title='The Big Lamp', 
        medium='installation/performance', 
        year='2018', 
        description1='The Big Lamp was an interdisciplinary, collaborative installation and performance in an empty racquetball court at Oberlin College in Ohio. It used cloth, metal, sine tones, bodies, a chord organ, fluorescent lights, a trombone, and various other soundmakers to convey a sense of concealed and emerging immensity.', 
        description2='', 
        image1='/static/bigLamp1.png', 
        image2='', 
        image3='', 
        image4='', 
        soundcloud_header='', 
        soundcloud_track_id='', 
        downdload_link='',
        img_filter='filter-off'
    )
    
work4 = Work(
        title='Dregs-Magic', 
        medium='audiovisual fixed media', 
        year='2017', 
        description1='Sound recorded by Leah Bertrand and Ricky Covell; audio created by Leah Bertrand and video created by Ricky Covell in Fall 2017. A thematization of residue, dregs-magic functions like a microscope,  revealing streams of subterranean texture and movement, freeing some  ordinary metal to reveal its internal world. Unlike the microscope,  however, the work does not purport to depict a viewer-independent world –  rather, it is the residue of the encounter itself which is interrogated  – the bumping of the microphone, the texture of the chalk and charcoal.  Its microscope is one of nakedness, its object, vision. Dregs-Magic has been programmed at the 2018 MFA Media Arts Annual,  National Students in Electronic Music Event (NSEME) 2019, and the  Society for Electroacoustic Music in the United States (SEAMUS) 2019.', 
        description2='', 
        image1='/static/dregsMagic1.png', 
        image2='', 
        image3='', 
        image4='', 
        soundcloud_header='', 
        soundcloud_track_id='', 
        downdload_link='',
        img_filter='filter-off'
    )
    
performance1 = Performance(
        title='Beg’d',
        medium='performance',
        year='2018',
        description1='Beg’d was a free improvisation ensemble formed in the spring of 2018. The instrumentation consisted of bowed metals, melodica, midi guitar, toy synthesizer, ocarina, and enough whirlies to go around. Audio excerpts above, full video below.',
        description2='', 
        image1='/static/Begd.jpeg',
        image2='',
        image3='',
        image4='', 
        soundcloud_header='Stereo Mix',
        soundcloud_track_id='415367730',
        downdload_link='',
        img_filter='filter-off'
    )
    
db.session.add_all([work1, work2, work3, work4, performance1])
db.session.commit()

# seed_database()

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








   
