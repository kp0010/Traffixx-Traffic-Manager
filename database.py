import os

import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String

SQLURI = os.environ.get('engine_URL', "sqlite:///users")
engine = sqlalchemy.create_engine(SQLURI, echo=True)

base = declarative_base()


class User(base):
    __tablename__ = "users"

    id = Column(String(16), primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    phone = Column(String(10), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=True)


base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    with Session(engine) as session:
        kp = User(id="KP0010", name="Kartik Parab", password="kartikcrs", phone="987654321",
                  email="kartikcr750@gmail.com")

        session.add(kp)
        session.commit()
