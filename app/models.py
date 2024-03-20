from . import db

class Property(db.Model):
    __tablename__ = 'Property'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.String(100))
    location = db.Column(db.String(100))
    price = db.Column(db.String(100))
    type = db.Column(db.String(100))
    description = db.Column(db.String(100))
    photo = db.Column(db.String(100))

    def __init__(self, title, bedrooms, bathrooms, location, price, type, description, photo):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.photo = photo

    # def __repr__(self):
    #     return '<Property %r>' % self.title

    # def is_authenticated(self):
    #     return True

    # def is_active(self):
    #     return True

    # def is_anonymous(self):
    #     return False

    # def get_id(self):
    #     try:
    #         return str(self.id)  # python 2 support
    #     except NameError:
    #         return str(self.id)  # python 3 support


