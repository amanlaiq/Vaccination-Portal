
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, backref

db = SQLAlchemy()

class Note(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class user(db.Model, UserMixin):
    _tablename_ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    role_id=  db.Column(db.Integer, db.ForeignKey('user_role.role_id'))
    notes = db.relationship('Note')
    nurse = db.relationship('nurse',  backref=backref('nurse', uselist=False, cascade='all, delete-orphan'))
    patient = db.relationship('patient', back_populates='user')
    


class user_role(db.Model):
    _tablename_ = 'user_role'
    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_type= db.Column(db.String(100), unique=True, nullable=False)

class vaccine(db.Model):
    _tablename_ = 'vaccine'

    vaccine_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(130))
    description = db.Column(db.String(255))
    quantity= db.Column(db.Integer, default=0)
    on_hold_count = db.Column(db.Integer, default=0)
    doses_required = db.Column(db.Integer, nullable=False)
    

# Define the Nurse model.
class nurse(db.Model):
    _tablename_ = 'nurse'

    nurse_id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(20))
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(15))
    phone_number = db.Column(db.String(10))
    address = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship('user')
    nurse_schedule = db.relationship('nurse_schedule', back_populates='nurse')
    nurse_vaccination_records= db.relationship('vaccination_record', back_populates='nurse')

# Define the TimeSlot model.
class time_slot(db.Model):
    _tablename_ = 'time_slot'

    t_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    max_patient_capacity=db.Column(db.Integer, nullable=False,default=0)
    nurse_count=db.Column(db.Integer, nullable=False,default=0)
# maxpatient-patients scheduled
    
    
 

# Define the Patient model.
class patient(db.Model):
    _tablename_ = 'patient'
    
    ssn = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    middle_name= db.Column(db.String(1))
    last_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    race = db.Column(db.String(30))
    occupation_class = db.Column(db.String(50))
    medical_history_description = db.Column(db.String(255))
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship('user')
    vaccine_schedules = db.relationship('vaccination_schedule', back_populates='patient')
    
# show the schedules for that time slot, when she selects 
# Define the VaccinationRecord model.
class vaccination_record(db.Model):
    _tablename_ = 'vaccination_record'

    record_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.ssn'))
    dose_number= db.Column(db.Integer, nullable=False)
    vaccination_time = db.Column(db.DateTime)
    nurse_id = db.Column(db.Integer, db.ForeignKey('nurse.nurse_id'))
    vaccine_id = db.Column(db.Integer, db.ForeignKey('vaccine.vaccine_id'))

    patient = relationship('patient')
    nurse = relationship('nurse')
    vaccine = relationship('vaccine')


# Define the NurseSchedule model.
class nurse_schedule(db.Model):
    _tablename_ = 'nurse_schedule'

    schedule_id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_slot_id = db.Column(db.Integer, db.ForeignKey('time_slot.t_id'))
    nurse_employee_id= db.Column(db.Integer, db.ForeignKey('nurse.nurse_id'))

    nurse = relationship('nurse')
    time_slot = relationship('time_slot')
    

# Define the VaccinationSchedule model.
class vaccination_schedule(db.Model):
    _tablename_ = 'vaccination_schedule'

    schedule_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id= db.Column(db.Integer, db.ForeignKey('patient.ssn'))
    vaccine_id = db.Column(db.Integer, db.ForeignKey('vaccine.vaccine_id'))
    time_slot_id = db.Column(db.Integer, db.ForeignKey('time_slot.t_id'))
    status = db.Column(db.Enum('Scheduled', 'Cancelled', 'Completed'))
    dose_no=db.Column(db.Integer,default=0)

    patient = relationship('patient')
    vaccine = relationship('vaccine')
    time_slot = relationship('time_slot')