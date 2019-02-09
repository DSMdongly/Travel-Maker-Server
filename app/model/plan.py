from app import db
from app.model import BaseModel, User


class Plan(BaseModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(20), db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(100), nullable=True)
    category = db.Column(db.Integer, nullable=False, default=0)
    location = db.Column(db.Integer, nullable=True)
    schedules = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.Text, nullable=True)

    @property
    def user(self):
        return User.find_by_id(self.user_id)

    class Location(type):
        SEOUL = 1
        BUSAN = 2
        GWANGJU = 3
        DAEJEON = 4
        ULSAN = 5
        INCHEON = 6
        JEONRA = 7
        CHUNGCHEONG = 8
        GYEONGI = 9
        GYEONSANG = 10
        GANGWON = 11
        JEJU = 12

    LOCATION_NAMES = {
        Location.SEOUL: '서울',
        Location.BUSAN: '부산',
        Location.GWANGJU: '광주',
        Location.DAEJEON: '대전',
        Location.ULSAN: '울산',
        Location.INCHEON: '인천',
        Location.JEONRA: '전라도',
        Location.CHUNGCHEONG: '충청도',
        Location.GYEONGI: '경기도',
        Location.GYEONSANG: '경상도',
        Location.GANGWON: '강원도',
        Location.JEJU: '제주도',
    }

    @classmethod
    def get_location_name(cls, location):
        return cls.LOCATION_NAMES.get(location, '')

    @property
    def location_name(self):
        return self.get_location_name(self.location)

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

    CATEGORY_NAMES = {
        Category.ETC: '기타',
        Category.MOUNTAIN: '산',
        Category.SEA: '바다',
        Category.VALLEY: '계곡',
        Category.ISLAND: '섬',
        Category.HOTPLE: '핫플레이스',
        Category.CITYTOUR: '시티투어',
        Category.LANDMARK: '랜드마크',
        Category.FOOD: '맛집',
    }

    @classmethod
    def get_category_name(cls, category):
        return Plan.CATEGORY_NAMES.get(category, '')

    @property
    def category_name(self):
        return self.get_category_name(self.category)

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def to_dict(self):
        return {
            **super(Plan, self).to_dict(),
            'category_name': self.category_name,
            'location_name': self.location_name,
            'user_name': self.user.name,
        }
