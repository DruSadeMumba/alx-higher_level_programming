#!/usr/bin/python3
"""A script that prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        for state, city in session.query(State, City).join(City).all():
            print(f"{state.name}: ({city.id}) {city.name}")
