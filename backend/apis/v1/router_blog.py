from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBlog, ResponseBlog
from db.repository.blog import create_new_blog, get_blog_by_id, get_all_blogs, update_blog_by_id
from typing import List

router = APIRouter()

@router.post("/",response_model= ResponseBlog, status_code= status.HTTP_201_CREATED)

def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return ResponseBlog.model_validate(blog)


# ✅ GET API - Fetch a single blog by ID
@router.get("/{id}")
def get_blog(id: int, db: Session = Depends(get_db)):
    print("print id")
    blog = get_blog_by_id(blog_id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found wtih {id}")
    return ResponseBlog.model_validate(blog)

# ✅ GET API - Fetch all blogs
@router.get("/", response_model=List[ResponseBlog])
def get_all_blogs_list(db: Session = Depends(get_db)):
    print("print id")
    blogs = get_all_blogs(db=db)
    return [ResponseBlog.model_validate(blog) for blog in blogs]

@router.put("/{id}", response_model=ResponseBlog)
def update_blog(id: int, update_blog: CreateBlog, db: Session = Depends(get_db)):
    blog = update_blog_by_id(blog_id=id, blog_data=update_blog, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} not found")
    return ResponseBlog.model_validate(blog)