from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)



# # # # # # # # # # # # # # # # # # # # # MODELS # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
class Work(db.Model):
    """Database Model for Works"""

    __tablename__ = 'works'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    title = db.Column(
        db.Text,
        nullable=False,
    )

    medium = db.Column(
        db.Text,
        nullable=False,
    )

    year = db.Column(
        db.Text,
        nullable=False,
    )

    description1 = db.Column(
        db.Text,
        nullable=False,
    )

    description2 = db.Column(
        db.Text,
        nullable=True,
    )

    image1 = db.Column(
        db.Text,
        nullable=False,
    )

    image2 = db.Column(
        db.Text,
        nullable=True,
    )

    image3 = db.Column(
        db.Text,
        nullable=True,
    )

    image4 = db.Column(
        db.Text,
        nullable=True,
    )

    soundcloud_header = db.Column(
    db.Text,
    nullable=True,
    )

    soundcloud_track_id = db.Column(
    db.Text,
    nullable=True,
    )

    downdload_link = db.Column(
    db.Text,
    nullable=True,
    )

    img_filter = db.Column(
        db.Text,
        nullable=True,
    )

    def serialize(self):
        '''Serialized Cupcake to dict for JSON'''

        return {
            'id': self.id,
            'medium': self.medium,
            'year': self.year,
            'description1': self.description1,
            'description2': self.description2,
            'image1': self.image1,
            'image2': self.image2,
            'image3': self.image3,
            'image4': self.image4,
            'soundcloud_header': self.soundcloud_header,
            'soundcloud_track_id': self.soundcloud_track_id,
            'downdload_link': self.downdload_link,
            'img_filter': self.img_filter,
        }



class Performance(db.Model):
    """Database Model for Performances"""

    __tablename__ = 'performances'


    id = db.Column(
        db.Integer,
        primary_key=True,
    )


