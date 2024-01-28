from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.exc import IntegrityError
from faker import Faker

db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    
    # Validator for name
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name is required.")
        return name
    
    # # Validator for unique name
    # @validates('name')
    # def validate_unique_name(self, key, name):
    #      if Author.query.filter(Author.name == name).first():
    #         raise ValueError('Author with the same name already exists.')
    #     return name
   
    
    # Validator for phone_number
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise ValueError("Phone number must be exactly ten digits.")
        return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Validator for title
    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError("Title is required.")
        return title

    # Validator for content length
    @validates('content')
    def validate_content_length(self, key, content):
        if len(content) < 250:
            raise ValueError("Content must be at least 250 characters long.")
        return content

    # Validator for summary length
    @validates('summary')
    def validate_summary_length(self, key, summary):
        if summary and len(summary) > 250:
            raise ValueError("Summary cannot exceed 250 characters.")
        return summary

    # Validator for category
    @validates('category')
    def validate_category(self, key, category):
        allowed_categories = ['Fiction', 'Non-Fiction']
        if category not in allowed_categories:
            raise ValueError("Invalid category. Choose Fiction or Non-Fiction.")
        return category
