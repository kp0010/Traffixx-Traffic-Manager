import sqlalchemy
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, select, update, Integer, PrimaryKeyConstraint
from werkzeug.security import generate_password_hash, check_password_hash
import pandas

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

PASSWORD = "rcsn hkmg iqsr qdyy"

SQLURI = "sqlite:///traffix_db"

base = declarative_base()


class User(base):
    __tablename__ = "users"

    id = Column(String(16), primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    phone = Column(String(10), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=True)

    def __repr__(self):
        rep = f"{self.id =}, {self.name =}"
        return rep


class AllotmentInfo(base):
    __tablename__ = "allotment_info"

    instance_id = Column(Integer, nullable=False)
    cycle_id = Column(Integer, nullable=False)
    lane_num = Column(Integer, nullable=False)
    allotment_time = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint(
            instance_id, cycle_id, lane_num), {})

    def __repr__(self):
        rep = f"{self.cycle_id =}, {self.lane_num =}, {self.allotment_time =}"
        return rep


class Database:
    def __init__(self, echo=False):
        self.engine = sqlalchemy.create_engine(SQLURI, echo=echo)
        self.Base = base
        self.create_tables()

        self.curr_instance_id = self.get_current_instance_id()
        self.curr_cycle_id = 0

        self.source_mail = "traffix95@gmail.com"

    def create_tables(self):
        self.Base.metadata.create_all(self.engine)

    def get_current_instance_id(self):
        with Session(self.engine) as sesh:
            result = sesh.execute(select(AllotmentInfo.instance_id).order_by(AllotmentInfo.instance_id.desc())).scalar()

            if result is None:
                return 0
            else:
                return result + 1

    def insert_current_cycle_info(self, cycle_allotment_info):
        with Session(self.engine) as sesh:
            for idx, info in enumerate(cycle_allotment_info):
                cur_allt_info = AllotmentInfo(instance_id=self.curr_instance_id, cycle_id=self.curr_cycle_id,
                                              lane_num=idx, allotment_time=info)

                sesh.add(cur_allt_info)

            self.curr_cycle_id = self.curr_cycle_id + 1

            self.current_instance_info()
            sesh.commit()

    def current_instance_info(self):
        with Session(self.engine) as sesh:
            result = sesh.execute(select(AllotmentInfo).filter_by(instance_id=self.curr_instance_id)).scalars()

            result_formatted = [(element.cycle_id, element.lane_num, element.allotment_time) for element in result]

            result_df = pandas.DataFrame(result_formatted, columns=["cycle_num", "lane_num", "time_alloted"])

            df_lane_1_2 = result_df[(result_df["lane_num"] == 0) | (result_df["lane_num"] == 1)]
            df_lane_3_4 = result_df[(result_df["lane_num"] == 2) | (result_df["lane_num"] == 3)]

            return df_lane_1_2, df_lane_3_4

    def add_new_user(self, userid, name, password, phone, email):
        with Session(self.engine) as sesh:
            hashed_pass = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
            try:
                new_user = User(id=userid, name=name, password=hashed_pass, phone=phone, email=email)
                sesh.add(new_user)
                sesh.commit()
            except Exception as e:
                error = e.args[0].split(" ")[-1][6:]
                return error
            else:
                return True

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
            <img src="https://i.ibb.co/gSXx0tm/WlogoF.png">
            <br>
            <h1>Your Traffixx Account - Password Updated </h1>
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

            try:
                connection.starttls()
                connection.login(user="traffixx95@gmail.com", password=PASSWORD)
                connection.sendmail("traffix95@gmail.com", dest_email, message.as_string())
            except Exception as e:
                print(e.args[0])


if __name__ == '__main__':
    db = Database(echo=False)
    db.create_tables()

    with Session(db.engine) as session:

        session.commit()
