#!/usr/bin/python3
"""
A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    new = State(name="Louisiana")
    with Session(engine) as session:
        session.add(new)
        session.commit()

    state = session.query(State).filter_by(name="Louisiana").first()
    print(state.id)
    session.close()
