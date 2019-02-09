from app import db
from ..model import BaseModel


class User(BaseModel):
    id = db.Column(db.String(20), primary_key=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    name = db.Column(db.String(20), nullable=False)
    keywords = db.Column(db.Text, nullable=True)
    description = db.Column(db.String(100), nullable=True)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()


class UserSocialLogin(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(20), db.ForeignKey('user.id'))
    api_id = db.Column(db.String(100), nullable=False)
    api_kind = db.Column(db.String(100), nullable=False)

    class ApiKind(type):
        FACEBOOK = 'facebook'
        GOOGLE = 'google'

    @classmethod
    def find_by_api_id_and_kind(cls, api_id, api_kind):
        return cls.query.filter_by(
            api_id=api_id,
            api_kind=api_kind,
        ).first()
