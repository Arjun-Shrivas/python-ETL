from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the database connection
def get_db_engine():
    return create_engine("mysql+mysqlconnector://root:pass123@localhost:3306/hr")

def get_session():
    engine = get_db_engine()
    Session = sessionmaker(bind=engine)
    return Session()
