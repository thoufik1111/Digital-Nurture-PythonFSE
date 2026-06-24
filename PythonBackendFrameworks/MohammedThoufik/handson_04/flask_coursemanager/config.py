class Config:
    SECRET_KEY = "flask-course-secret"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///courses.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False