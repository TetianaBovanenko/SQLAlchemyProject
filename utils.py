from sqlalchemy.orm import Session
from models import Person, Thing

def add_person(session: Session, ssn: int, firstname: str, lastname: str, gender: str, age: int):
    person = Person(ssn=ssn, firstname=firstname, lastname=lastname, gender=gender, age=age)
    session.add(person)
    session.commit()

def add_thing(session: Session, id: int, name: str, owner_ssn: int):
    thing = Thing(id=id, name=name, owner=owner_ssn)
    session.add(thing)
    session.commit()

def query_all_things(session: Session):
    return session.query(Thing, Person).filter(Thing.owner == Person.ssn).all()
