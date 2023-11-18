#!/usr/bin/python3
"""
A script that lists all City objects
from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, joinedload
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        for state in session.query(State):
            for city in state.cities:
                print(f"{city.id}: {city.name} -> {state.name}")
