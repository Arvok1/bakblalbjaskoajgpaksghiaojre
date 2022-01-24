from app.models import BaseModel, db
from flask import Blueprint 

user_api = Blueprint('user_api', __name__)

class User(BaseModel):
    
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(70))
    email = db.Column(db.String(70), unique=True, index=True)
    
    pedidos = db.relationship("Item")
    
    def json(self):
        return {
            "cpf":self.cpf,
            "name":self.name,
            "email":self.email
        }