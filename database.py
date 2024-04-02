import os

import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, select
from werkzeug.security import generate_password_hash, check_password_hash

SQLURI = "sqlite:///users"

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(String(16), primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    phone = Column(String(10), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=True)

    def __repr__(self):
        rep = f"{self.id =}, {self.name =}"
        return rep


class Database:
    def __init__(self, echo=False):
        self.engine = sqlalchemy.create_engine(SQLURI, echo=echo)
        self.Base = Base
        self.create_tables()

    def create_tables(self):
        self.Base.metadata.create_all(self.engine)

    def add_new_user(self, userid, name, password, phone, email):
        with Session(self.engine) as sesh:
            hashed_pass = generate_password_hash(password, method="pbkdf2:sha256", salt_length=10)
            new_user = User(id=userid, name=name, password=hashed_pass, phone=phone, email=email)

            sesh.add(new_user)
            sesh.commit()

    def check_user_cred(self, userid, password):
        with Session(self.engine) as sesh:
            sel_user = sesh.execute(select(User).filter_by(id=userid)).scalar_one_or_none()

            if sel_user is None:
                return None

            elif check_password_hash(sel_user.password, password):
                return sel_user

            else:
                return False


if __name__ == '__main__':
    db = Database(echo=False)

    # db.add_new_user("KP0011", "Kartikkk", "asjdflksjdf", phone="9230423234", email="kasdfas@gmail.com")

    with Session(db.engine) as session:
        user = session.execute(select(User).filter_by(id="KP0011")).scalar_one_or_none()
        print(user)
        session.commit()
