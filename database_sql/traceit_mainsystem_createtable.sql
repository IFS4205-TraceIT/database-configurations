DROP table if exists CloseContacts, Notifications, InfectionHistory, VaccinationHistory, BuildingAccess, Users, Buildings, VaccinationTypes, ContactTracers;

create table Users(
	id serial primary key,
	nric text UNIQUE not NULL,
	name text not null,
	dob date not null,
	email text,
	phone INTEGER not null,
	gender CHAR(1) not null,
	address text not null,
	zip_code integer not null
);

create table Buildings(
	id serial primary key,
	name text not null,
	location integer not null
);

create table BuildingAccess(
	user_id integer references Users(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	building_id integer references Buildings(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	access_timestamp TIMESTAMP not null,
	primary key(user_id, building_id, access_timestamp)
);

create table VaccinationTypes(
	id serial primary key,
	name text not null,
	start_date date not null
);

create table VaccinationHistory(
	user_id integer references Users(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	vaccination_id integer references VaccinationTypes(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	date_taken date not null,
	primary key(user_id, vaccination_id, date_taken)
);

create table InfectionHistory(
	user_id integer references Users(id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	recorded_timestamp TIMESTAMP not null,
	has_uploaded boolean DEFAULT FALSE,
	primary key(user_id, recorded_timestamp)
);

create table ContactTracers(
	uuid integer primary key
);

create table Notifications(
	id serial primary key,
	due_date date,
	start_date date,
	tracer_id integer references ContactTracers(uuid)
		ON DELETE SET NULL
		ON UPDATE CASCADE,
	infected_user_id integer references Users(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	status boolean default FALSE
);

create table CloseContacts(
	infected_user_id integer references Users(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	contacted_user_id integer references Users(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	contact_timestamp timestamp not null,
	rssi numeric not null,
	primary key(infected_user_id, contacted_user_id, contact_timestamp),
	constraint different_user check(
		infected_user_id <> contacted_user_id
	)
);






