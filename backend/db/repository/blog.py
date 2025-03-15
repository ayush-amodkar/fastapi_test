from sqlalchemy.orm import Session
from schemas.blog import CreateBlog
from db.models.blog import Blog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1):
    blog = Blog(title=blog.title, 
                content=blog.content, 
                slug=blog.slug, 
                author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def get_blog_by_id(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def get_all_blogs(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def update_blog_by_id(id: int, blog_data: CreateBlog, db: Session, author_id: int = 1):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return None  # If blog doesn't exist, return None

    # Update fields
    blog_in_db.title = blog_data.title
    blog_in_db.content = blog_data.content
    blog_in_db.slug = blog_data.slug

    db.commit()
    db.refresh(blog_in_db)
    return blog_in_db