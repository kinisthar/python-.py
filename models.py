from flask_login import UserMixin
from verkzeug.security import generate_password_has, check_password_hash

class user(UserMixin):

    def__init__(self, id, name, email, password, is_admin=False)
       self.id = id
       self.name = name
       self.email = email
       self.password = generate_password_has(password)
       self.is_admin = is_admin
    def set_password (self, passsword):
         self.password = generate_password_has(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return <'User { }'>.format(self.email)

        users = []
        def  get_user(email-any):
            for user in users:
                if user.email. == email:
                    return user
                return None

