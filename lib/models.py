from sqlalchemy import (Column, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Specialty(Base):
    # linking a table to the class
    __tablename__ = "specialties"

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    engine = create_engine('sqlite:///lib/db/clinic.db')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
