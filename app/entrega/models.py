from app.models import BaseModel, db
from flask import Blueprint 

entrega_api = Blueprint('entrega_api', __name__)

class Entrega(BaseModel):
    __tablename__ = 'entregas'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pedidos = db.relationship("StatusEntrega")
    
class StatusEntrega(BaseModel):
    __tablename__ = 'statusentregas'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    entrega_id = db.Column(db.ForeignKey('entregas.id'))
    item_id = db.Column(db.ForeignKey('item.id'))
    
    entregou = db.Column(db.Boolean)
    
    item = db.relationship("Item")
    
    
    
 