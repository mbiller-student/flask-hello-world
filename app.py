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


