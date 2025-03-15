from sqlalchemy.orm import Session
from schemas.user import UserCreate
from db.models.default_user import User
# from core.hashing import Hasher

def create_new_user(user: UserCreate, db: Session):
    user = User(
        email=user.email, 
        password=(user.password),  
        is_active=True, 
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user