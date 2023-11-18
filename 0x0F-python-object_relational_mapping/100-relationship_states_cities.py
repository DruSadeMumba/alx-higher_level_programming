#!/usr/bin/python3
"""
A script that adds the State object “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        new_state = State(name="California")
        session.add(new_state)
        session.commit()

        new_city = City(name="San Francisco", state_id=new_state.id)
        session.add(new_city)
        session.commit()
    session.close()
