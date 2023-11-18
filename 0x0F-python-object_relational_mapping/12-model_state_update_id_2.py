#!/usr/bin/python3
"""
A script that changes the name of State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    new_name = "New Mexico"
    id_update = 2
    with Session(engine) as session:
        state = session.query(State).filter_by(id=id_update).first()
        state.name = new_name
        session.commit()
