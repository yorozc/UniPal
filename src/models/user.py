from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, doc):
        self.doc = doc or {}
        self.id = str(self.doc.get("_id"))

    @property
    def is_active(self):
        return bool(self.doc.get("is_active", True))
    
    @property 
    def is_anonymous(self):
        return False
    
    @property 
    def is_authenticated(self):
        return True
    
    @property 
    def email(self):
        return self.doc.get("email")
    
    @property 
    def name(self):
        return str(self.doc.get("first_name")) + " " + str(self.doc.get("last_name"))