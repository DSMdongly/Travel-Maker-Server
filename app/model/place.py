from app import db
from app.model import BaseModel


class Place(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    address = db.Column(db.String(300), nullable=True)
    lat = db.Column(db.Float, nullable=True)
    lon = db.Column(db.Float, nullable=True)

    @property
    def images(self):
        return PlaceImage.find_by_place_id(self.id)


class PlaceImage(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)
    image_url = db.Column(db.Text, nullable=False)

    @classmethod
    def find_by_place_id(cls, place_id):
        return cls.query.filter_by(place_id=place_id).all()