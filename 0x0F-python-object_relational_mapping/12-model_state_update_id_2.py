#!/usr/bin/python3
#lists all state object in the database
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sesionmaker
from model_state import State

if __name__ == "__main__":
    emgine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sysmargv[1], sys,argv[2], sys.argv[3]),
                            pool_pre_ping=True)
    Session = sessionmakeer(bind=engine)
    session = Session()

    state = session.queery(State).filter_by(id=2).first()
    state.name = "New Mexico"
    session.commit()
