#!/usr/bin/python3
"""script that creats state California with City San Franscisco"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                          (sys.argv[1], sys.argv[2], sys.argv[3]),
                          pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    n_state = State(name='California')
    n_city = City(name='San Francisco')
    n_state.cities.append(n_city)
    session.add(n_state)
    session.commit()
    session.close()
