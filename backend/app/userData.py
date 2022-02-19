from app import db


class UserData(db.Model):
    __tablename__ = 'userdata'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    sex = db.Column(db.String)
    weight = db.Column(db.REAL)
    height = db.Column(db.REAL)
    age = db.Column(db.Integer)

    def addUser(firstname, lastname, username, password, sex, weight, height, age):
        for field in [firstname, lastname, username, password, sex, weight, height, age]:
            if field is None:
                raise Exception('fields cannot be null')

        user = UserData(
            firstname=firstname,
            lastname=lastname,
            username=username,
            password=password,
            sex=sex,
            weight=weight,
            height=height,
            age=age
        )
        db.session.add(user)
        db.session.commit()
        print("successfully added user")
        return "success"

    def getUser(id):
        user = UserData.query.get(id)
        if (user is None):
            return None
        else:
            return user.serialize()

    def updateUser(id, firstname, lastname, username, password, sex, weight, height, age):
        if (id is None):
            raise Exception('id cannot be null')

        user = UserData.query.get(id)

        if (firstname is not None):
            user.firstname = firstname
            db.session.commit()
        if (lastname is not None):
            user.lastname = lastname
            db.session.commit()
        if (username is not None):
            user.username = username
            db.session.commit()
        if (password is not None):
            user.password = password
            db.session.commit()
        if (sex is not None):
            user.sex = sex
            db.session.commit()
        if (weight is not None):
            user.weight = weight
            db.session.commit()
        if (height is not None):
            user.height = height
            db.session.commit()
        if (age is not None):
            user.age = age
            db.session.commit()

        return 'success', 201

    def serialize(self):
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'username': self.username,
            'password': self.password,
            'sex': self.sex,
            'weight': self.weight,
            'height': self.height,
            'age': self.age
        }
