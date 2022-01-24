
from app.models import BaseModel, db
from flask import Blueprint

item_api = Blueprint('item_api', __name__)

class Item(BaseModel):
    __tablename__ = 'item'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(15))
    
    
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def json(self):
        return {
            "id":self.id,
            "nome":self.nome
        }
    
