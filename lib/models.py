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

#     surgeon = Specialty("Surgeon")
#     oncologist = Specialty("Oncologist")
#     cardiologist = Specialty("Cardiologist")
#     gastroenterologist = Specialty("Gastroenterologist")
#     nephrologist = Specialty("Nephrologist")
#     pulmonologist = Specialty("Pulmonologist")
#     nephrologist = Specialty("Nephrologist")

# Add all at once using bulk_save_objects
# session.bulk_save_objects([
#     surgeon,
#     oncologist,
#     cardiologist,
#     gastroenterologist,
#     pulmonologist,
#     nephrologist
# ])

# Commit the transaction
# session.commit()

# # Print the ID of the newly created 'surgeon' specialty
# # print(f"The new specialty ID is {surgeon.id}")

    specialties = session.query(Specialty).all()
    print([specialty.name for specialty in specialties])
    session.commit()
    

    session.query(Specialty).filter(Specialty.id ==4).update(
    {Specialty.name:"dentist"}
    )
    session.commit()



# session.query(Specialty).where(Specialty.id ==2).delete()
# session.commit()
