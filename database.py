import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, select, update
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
            hashed_pass = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
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

    def update_password(self, sel_user, newpass):
        newpass_hashed = generate_password_hash(password=newpass, method="pbkdf2:sha256", salt_length=8)

        with Session(self.engine) as sesh:
            sesh.execute(update(User).where(User.id == sel_user.id).values(password=newpass_hashed))
            sesh.commit()

    def get_user_from_info(self, userid, name, mail, phone):
        with Session(self.engine) as sesh:
            sel_user = sesh.execute(select(User).filter_by(id=userid)).scalar_one_or_none()

            if sel_user is None:
                return None
            if sel_user.email != mail and sel_user.phone != phone:
                return "all"
            if sel_user.phone != phone:
                return "phone"
            if sel_user.email != mail:
                return "mail"

            return sel_user


if __name__ == '__main__':
    db = Database(echo=False)

    # db.add_new_user("KP001", "Kartikkk", "kartikcrs", phone="2234232342", email="kasd23423fas@gmail.com")

    with Session(db.engine) as session:
        user = session.execute(select(User).filter_by(id="admin")).scalar_one_or_none()
        # print(user)
        session.commit()

    db.update_password("admin", "1234")
