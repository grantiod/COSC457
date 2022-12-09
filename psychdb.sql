use psych_office;

SET FOREIGN_KEY_CHECKS = 0;

CREATE TABLE IF NOT EXISTS EMPLOYEE (
    employee_name VARCHAR(20),
    employee_num INT,
    ssn INT,
    dob DATE,
    address VARCHAR(20),
    PRIMARY KEY (employee_name, employee_num, ssn)
);

CREATE TABLE IF NOT EXISTS EMPLOYEE_HEALTH_INSURANCE (
    employee_name VARCHAR(20),
    employee_num INT,
    depend_name VARCHAR(20),
    insur_provided VARCHAR(20),
    PRIMARY KEY (employee_num),
    FOREIGN KEY (employee_name, employee_num) REFERENCES EMPLOYEE (employee_name, employee_num)
);

CREATE TABLE IF NOT EXISTS EMPLOYEE_WORKING_HOURS (
    employee_name VARCHAR(20),
    employee_num INT,
    hours_worked_ytd INT,
    PRIMARY KEY (employee_num),
    FOREIGN KEY (employee_name, employee_num) REFERENCES EMPLOYEE (employee_name, employee_num)
);

CREATE TABLE IF NOT EXISTS EMPLOYEE_VACATION_DAYS (
    employee_name VARCHAR(20),
    employee_num INT,
    dates_off DATE,
    num_days_allotted INT,
    PRIMARY KEY (employee_num),
    FOREIGN KEY (employee_name, employee_num) REFERENCES EMPLOYEE (employee_name, employee_num)
);

CREATE TABLE IF NOT EXISTS EMPLOYEE_SICK_DAYS (
    employee_name VARCHAR(20),
    employee_num INT,
    dates_off DATE,
    num_days_allotted INT,
    PRIMARY KEY (employee_num),
    FOREIGN KEY (employee_name, employee_num) REFERENCES EMPLOYEE (employee_name, employee_num)
);

CREATE TABLE IF NOT EXISTS OFFICE_ROOMS (
    room_id INT,
    address VARCHAR(20),
    room_num INT,
    employee_num INT,
    PRIMARY KEY (room_id),
    FOREIGN KEY (employee_num) REFERENCES EMPLOYEE (employee_num)
);

CREATE TABLE IF NOT EXISTS HEALTHCARE_WORKERS (
	ssn INT,
    role VARCHAR(20),
	address VARCHAR(20),
    employee_num INT,
    number_of_patients INT,
    employee_name VARCHAR(20),
    PRIMARY KEY (employee_num),
    FOREIGN KEY (employee_num) REFERENCES EMPLOYEE (employee_num)
);

CREATE TABLE IF NOT EXISTS DEPENDENTS (
	dependent_name VARCHAR(20),
	address VARCHAR(20),
    employee_num INT,
    dependent_dob DATE,
    relationship VARCHAR(20),
    PRIMARY KEY (employee_num),
    FOREIGN KEY (employee_num) REFERENCES EMPLOYEE (employee_num)
);

CREATE TABLE IF NOT EXISTS PATIENT_BILLS (
	patient_name VARCHAR(20),
	date DATE,
	payment_due DATE,
	cost FLOAT,
	patient_id INT,
	PRIMARY KEY(patient_name, patient_id)
);

CREATE TABLE IF NOT EXISTS APPOINTMENTS (
	appointment_num INT,
	patient_name VARCHAR(20),
	patient_id INT,
	employee_num INT,
	PRIMARY KEY (appointment_num),
    FOREIGN KEY (employee_num) REFERENCES EMPLOYEE (employee_num)
);

CREATE TABLE IF NOT EXISTS PATIENT (
    patient_id INT,
    patient_name VARCHAR(20),
    emrgency_contact_info VARCHAR(20),
    dob DATE,
    phone VARCHAR(10),
    email VARCHAR(20),
    address VARCHAR(20),
	PRIMARY KEY (patient_id, patient_name)
);

CREATE TABLE IF NOT EXISTS PATIENT_ACCOUNT (
	patient_id INT,
	age INT,
	patient_name VARCHAR(20),
	phone VARCHAR(10),
	address VARCHAR(20),
	current_medication VARCHAR(20),
	allergies VARCHAR(20),
	PRIMARY KEY (patient_id)
);

CREATE TABLE IF NOT EXISTS PATIENT_HEALTH_INSURANCE (
	patient_id INT,
	patient_name VARCHAR(20),
	insur_prov VARCHAR(20),
	insur_id INT,
	date_exp DATE,
	PRIMARY KEY(patient_id, patient_name),
	FOREIGN KEY(patient_id) REFERENCES PATIENT (patient_id)
);

CREATE TABLE IF NOT EXISTS OPERATIONS (
	operation_type VARCHAR(20),
	patient_id INT,
	operation_date DATE,
	employee_num INT,
	operation_cost FLOAT,
	PRIMARY KEY (operation_type),
	FOREIGN KEY (patient_id) REFERENCES PATIENT (patient_id),
	FOREIGN KEY (employee_num) REFERENCES EMPLOYEE (employee_num)
);

CREATE TABLE IF NOT EXISTS MEDICATIONS (
	medication_id INT,
	manufacturer VARCHAR(20),
	prescription_amount INT,
	prescription_date DATE,
	employee_num INT,
	patient_name VARCHAR(20),
	patient_id INT,
	PRIMARY KEY(medication_id),
	FOREIGN KEY(patient_id) REFERENCES PATIENT (patient_id)
);

CREATE TABLE IF NOT EXISTS EQUIPMENT (
	asset_id INT,
	estimated_value INT,
	contact_on_file VARCHAR(20),
	employee_num INT,
	PRIMARY KEY(asset_id)
);

alter table EMPLOYEE
add foreign key (employee_num) references STUDENTS (employee_num);

CREATE TABLE IF NOT EXISTS STUDENTS (
	student_id INT,
	student_name VARCHAR(20),
	employee_num INT,
	PRIMARY KEY(student_id),
	FOREIGN KEY(employee_num) REFERENCES EMPLOYEE (employee_num)
);

CREATE TABLE IF NOT EXISTS K_PLAN (
	account_num INT,
	invest_percentage FLOAT,
	employer_contribution_percentage FLOAT,
	pay_ytd FLOAT,
	employee_num INT,
    PRIMARY KEY (account_num),
	FOREIGN KEY (employee_num) REFERENCES EMPLOYEE (employee_num)
);

CREATE TABLE IF NOT EXISTS REFERRALS (
	address VARCHAR(20),
	phone VARCHAR(10),
	accepted_insurances VARCHAR(20),
	availability VARCHAR(20),
	practice VARCHAR(20),
	telehealth_offered VARCHAR(20),
	patient_id INT,
	employee_num INT,
	PRIMARY KEY(address),
	FOREIGN KEY(patient_id) REFERENCES PATIENT (patient_id),
	FOREIGN KEY(employee_num) REFERENCES EMPLOYEE (employee_num)
);

CREATE TABLE IF NOT EXISTS INVENTORY (
    items VARCHAR(10),
    stock INT,
    supplier_address VARCHAR(20),
    supplier_contact VARCHAR(20),
    inventory_location VARCHAR(20),
    branch_num INT,
    PRIMARY KEY (items),
    FOREIGN KEY (branch_num) REFERENCES BRANCHES (branch_num)
);

CREATE TABLE IF NOT EXISTS BRANCHES (
    branch_num INT,
    branch_name VARCHAR(20),
    state VARCHAR(2),
    address VARCHAR(20),
    contact VARCHAR(20),
    PRIMARY KEY (branch_num)
);

CREATE TABLE IF NOT EXISTS BUSINESS_ACCOUNTS (
    account_id INT,
    company_name VARCHAR(20),
    contact VARCHAR(20),
    address VARCHAR(20),
    service VARCHAR(10),
    PRIMARY KEY (account_id)
);

CREATE TABLE IF NOT EXISTS OFFICE_BILLS (
    bill_num INT,
    branch_num INT,
    issue_date DATE,
    issuer VARCHAR(20),
    payment_date DATE,
    charge FLOAT,
    PRIMARY KEY (bill_num),
    FOREIGN KEY (branch_num) REFERENCES BRANCHES (branch_num)
);

CREATE TABLE IF NOT EXISTS PROCEDURES (
    procedure_num INT,
    procedure_type VARCHAR(10),
    procedure_criteria VARCHAR(20),
    branch_num INT,
    PRIMARY KEY (procedure_num),
    FOREIGN KEY (branch_num) REFERENCES BRANCHES (branch_num)
);

CREATE TABLE IF NOT EXISTS PHARMACY (
	pharmacy_id INT,
    pharmacy_name VARCHAR(20),
    owner VARCHAR(20),
    contact VARCHAR(20),
    address VARCHAR(20),
    medication_id INT,
    PRIMARY KEY (pharmacy_id),
    FOREIGN KEY (medication_id) REFERENCES MEDICATIONS (medication_id)
);

SET FOREIGN_KEY_CHECKS = 1;