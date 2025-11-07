from flask import Flask
app = Flask(__name__)

import psycopg2

@app.route('/')
def hello_world():
    return 'Hello World from Matt Biller -- in 3308!'

@app.route('/db_test')
def testing():
	con = psycopg2.connect("postgresql://matt_postgressql_database_user:NvvhlXi6zQslJ1WpTR1FK7cSxjFouHsU@dpg-d46m656mcj7s73e8su5g-a/matt_postgressql_database")
	con.close()
	return "Database Connection Successful"


@app.route('/db_create')
def creating():
	con = psycopg2.connect("postgresql://matt_postgressql_database_user:NvvhlXi6zQslJ1WpTR1FK7cSxjFouHsU@dpg-d46m656mcj7s73e8su5g-a/matt_postgressql_database")

	cur = con.cursor()
	cur.execute('''
		CREATE TABLE IF NOT EXISTS Basketball (
		First varchar(255),
		Last varchar(255),
		City varchar(255),
		Name varchar(255),
		Number int
		);
	''')

	con.commit()
	con.close()
	return "Basketball Tabel successfully created!"


@app.route('/db_insert')
def inserting():
	con = psycopg2.connect("postgresql://matt_postgressql_database_user:NvvhlXi6zQslJ1WpTR1FK7cSxjFouHsU@dpg-d46m656mcj7s73e8su5g-a/matt_postgressql_database")

	cur = con.cursor()
	cur.execute('''
		INSERT INTO Basketball (First, Last, City, Name, Number)
		Values
		('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
		('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
		('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
		('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
	''')

	con.commit()
	con.close()
	return "Basketball Table successfully populated!"


@app.route('/db_select')
def selecting():
	con = psycopg2.connect("postgresql://matt_postgressql_database_user:NvvhlXi6zQslJ1WpTR1FK7cSxjFouHsU@dpg-d46m656mcj7s73e8su5g-a/matt_postgressql_database")

	cur = con.cursor()
	cur.execute('''
		SELECT * FROM Basketball;
	''')
	records = cur.fetchall()
	con.close()
	response_string = ""
	response_string += "<table>"

	for player in records:
		response_string += "<tr>"
		for info in player:
			response_string += "<td>{}</td>".format(info)
		response_string += "</tr>"
	response_string += "</table>"
	return response_string
		


