from app import db
from app.model import BaseModel


class Plan(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(20), db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    category = db.Column(db.Integer, nullable=False, default=0)

    class Category(type):
        ETC = 0
        MOUNTAIN = 1
        SEA = 2
        VALLEY = 3
        ISLAND = 4
        HOTPLE = 5
        CITYTOUR = 6
        LANDMARK = 7
        FOOD = 8


class PlanImage(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)
    image_url = db.Column(db.Text, nullable=False)

    @classmethod
    def find_by_plan_id(cls, plan_id):
        return cls.query.filter_by(plan_id=plan_id).all()
