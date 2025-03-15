from pydantic import BaseModel
from pydantic import BaseModel, model_validator
from datetime import datetime
from typing import Optional

class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None
    
    @model_validator(mode="before")
    def generate_slug(cls, values):
        if 'title' in values:
            values['slug'] = values.get('title').replace(" ", "-").lower()
        return values

class UpdateBlog(CreateBlog):
    pass

class ResponseBlog(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    slug: str  # Ensure this exists in your ORM model

    class Config:
        from_attributes = True  # Correct way for Pydantic v2
        

