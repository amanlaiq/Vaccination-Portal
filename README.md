# VACCINATION-PORTAL

**Description:**
This project is a database system developed to manage vaccination processes and scheduling. It follows a two-tier architecture with a back-end database and a front-end application. The system handles vaccine information, nurse scheduling, patient registration, appointment scheduling, vaccination records.

**Key Features:**
- User authentication with roles (admin, nurse, patient)
- Admin functionalities include nurse and vaccine management
- Nurse functionalities include scheduling appointments and recording vaccinations
- Patient functionalities include registration, appointment scheduling, and viewing vaccination history
- Libraries/Frameworks/ORM- Flask, Angular, SQLAlchemy

**Functionalities**:

- Login: Users can log in with a username/password and select their role (admin, nurse, patient).

Admin:
- Register Nurse: Admins can register nurses with a username and password.
- Update Nurse Info: Admins update nurse info except phone# and address.
- Delete Nurse: Admins remove nurses from the database.
- Add Vaccine: Admins update vaccine doses.
- Update Vaccine: Admins adjust vaccine quantities.
- View Nurse Info: Admins view nurse details and schedules.
- View Patient Info: Admins see patient details, schedules, and vaccination history.

Nurse:
- Update Info: Nurses update their contact details.
- Schedule Time: Nurses book available time slots.
- Cancel Time: Nurses delete scheduled slots.
- View Info: Nurses check their schedules and details.
- Record Vaccination: Nurses record vaccinations.

Patient:
- Register: Patients sign up with a username/password.
- Update Info: Patients update their details.
- Schedule Vaccination: Patients book vaccination slots.
- Cancel Schedule: Patients delete booked slots.
- View Info: Patients see their details, schedules, and vaccination history.

**Guidelines and Setup:**
- Clone the application- git clone git@github.com:jagriti1406/COVID-VACCINATION-PORTAL.git
- Go to the backend folder and perform the following flask commands
- Go to the front end folder and perform the commands listed in angular section below

**Database setup**-
- In case you are using xampp to access the database, you can visit http://localhost/phpmyadmin/ after running the servers.
- Add a database with the naming of your choice and configure the same in flask file. In the project, the database name is vaccinesystem.

**Flask Commands**

 
- Create a virtual env​: pip install virtualenv
- Install Flask: pip install Flask
- Create a Virtual Environment: python -m venv myenv
- Check the packages installed: pip freeze
- Activate a Virtual Environment: .\myenv\Scripts\Activate.ps1
- Run the flask application: flask run –debug 
- Initialize and create the migration repository:flask db init
- Create an initial migration: flask db migrate -m “initial migration”
- Apply migration to create the tables: flask db upgrade

**Angular Setup**

- Install node modules: npm i
- Run the application: ng serve

Access the application in your web browser on localhost:4200 and log in with admin, nurse, or patient credentials to test different functionalities


**ERD**



<img width="664" alt="image" src="">


**Relational Schema**



<img width="769" alt="image" src="">



