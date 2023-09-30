from app import db
from uuid import uuid4
from datetime import datetime

def generate_uuid():
    return uuid4().hex


class Videos(db.Model):
    __tablename__ = "videos"

    id = db.Column(
        db.String(60),
        nullable=False,
        primary_key=True,
        unique=True,
        default=generate_uuid
    )
    name = db.Column(db.String(60), nullable=False, unique=True)
    data = db.Column(db.LargeBinary(length=(2**32)-1), nullable=False)
    created_at = db.Column(db.DateTime(), default=datetime.now, nullable=False)
    updated_at = db.Column(db.DateTime(), default=datetime.now, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "id: {}, name: {}, created_at: {},\
              updated_at: {}".format(self.id, self.name, self.created_at,
                                     self.updated_at)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        """Return a dictionary representation of the User object"""
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
