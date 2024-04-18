import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, select, update, Integer, PrimaryKeyConstraint
from werkzeug.security import generate_password_hash, check_password_hash

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

PASSWORD = "rcsn hkmg iqsr qdyy"

SQLURI = "sqlite:///traffix_db"

Base = declarative_base()


class User(Base):
    __tablename__ = "traffix_db"

    id = Column(String(16), primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    phone = Column(String(10), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=True)

    def __repr__(self):
        rep = f"{self.id =}, {self.name =}"
        return rep


class AllotmentInfo(Base):
    __tablename__ = "allotment_info"

    instance_id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    id = Column(Integer, nullable=False)
    lane_num = Column(String(8), nullable=False)
    allotment_time = Column(Integer, nullable=False)

    def __repr__(self):
        rep = f"{self.id =}, {self.lane_num =}, {self.allotment_time =}"
        return rep


class Database:
    def __init__(self, echo=False):
        self.engine = sqlalchemy.create_engine(SQLURI, echo=echo)
        self.Base = Base

        self.curr_instance_id = self.get_current_instance_id()
        self.curr_cycle_id = 0

        self.source_mail = "traffix95@gmail.com"

        self.create_tables()

    def get_current_instance_id(self):
        with Session(self.engine) as sesh:
            result = sesh.execute(select(AllotmentInfo.instance_id).order_by(AllotmentInfo.instance_id.desc())).scalar()

            if result is None:
                return 0
            else:
                return result + 1

    # def insert

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

    def send_mail(self, dest_email, userid):
        now = datetime.datetime.now()
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            message = MIMEMultipart("alt")
            message["Subject"] = f"Password Update On Traffixx on {now.strftime("%d %b, %y")}"
            message["From"] = "traffix95@gmail.com"
            message["To"] = self.source_mail

            msg = f"""
            <h1>Your Traffixx Account - Password Updated Updated </h1>

            <br>
            <h3> Dear User {userid}, </h3>

            <p>This email was generated because new password was updated on Traffixx account with user id <b>{userid}</b> on {now.strftime("%B %d, %Y")}.<br>
            If you did not request this change, please contact our support team immediately at {self.source_mail} to secure your account.</p>
            

            <p>We recommend keeping your password confidential and avoiding the use of the same password across multiple accounts. Additionally, using a mix of letters, numbers, and symbols can help improve the security of your password.</p>
            
            <p>Thank you for your attention to this matter. If you have any questions or concerns, please do not hesitate to reach out.</p>
            
            <p>Best regards,</p>
            
            <p>Omkar Jadhav<br>
            Customer Support Representative<br>
            Traffixx</p>
            """

            message.attach(MIMEText(msg, "html"))

            connection.starttls()
            connection.login(user="traffixx95@gmail.com", password=PASSWORD)
            connection.sendmail("traffix95@gmail.com", dest_email, message.as_string())


if __name__ == '__main__':
    db = Database(echo=False)

    # db.add_new_user("KP001", "Kartikkk", "kartikcrs", phone="2234232342", email="kasd23423fas@gmail.com")

    with Session(db.engine) as session:
        # user = session.execute(select(User).filter_by(id="admin")).scalar_one_or_none()
        # # print(user)
        i_id = db.get_current_instance_id()
        alt = AllotmentInfo(instance_id=i_id, id=1, lane_num=3, allotment_time=69)

        # session.add(alt)

        session.commit()

    # db.send_mail("kartikcr750@gmail.com", "KP0010")

    # print(db.get_current_instance_id())  # print(db.get_current_instance_id())

    # db.update_password("admin", "1234")
