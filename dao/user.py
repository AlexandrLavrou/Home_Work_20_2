from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, user_id):
        return self.session.query(User).get(user_id)

    def create(self,data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()

        return user

    def get_all(self):
        return self.session.query(User).all()

    def update(self, user):

        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, user_id):
        user = self.get_one(user_id)

        self.session.delete(user)
        self.session.commit()

    def get_by_role(self,role):
        users = self.session.query(User).filter(User.role == role).first()
        return users

    def get_by_name(self, username):
        user = self.session.query(User).filter(User.username == username).first()
        return user