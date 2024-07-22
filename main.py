import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from models import Person, Thing, Base
from config import DATABASE_URL
from utils import add_person, add_thing, query_all_things

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    try:
        engine = create_engine(DATABASE_URL, echo=True)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        # Add persons
        add_person(session, 31234, "Anna", "Blue", "f", 40)
        add_person(session, 32423, "Bob", "Blue", "m", 35)
        add_person(session, 45654, "Angela", "Cold", "f", 22)

        # Add things
        add_thing(session, 1, "Car", 31234)
        add_thing(session, 2, "Laptop", 31234)
        add_thing(session, 3, "PS5", 32423)
        add_thing(session, 4, "Tool", 45654)
        add_thing(session, 5, "Book", 45654)

        # Query and print all things with their owners
        results = query_all_things(session)
        for thing, person in results:
            logger.info(f"{thing.name} owned by {person.firstname} {person.lastname}")

    except SQLAlchemyError as e:
        logger.error(f"Error occurred: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
