from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Your SQL Server connection string
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-GRIC9MQ;"
    "DATABASE=master;"
    "Trusted_Connection=yes;"
)

@app.route('/')
def index():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Passenger")
    passengers = cursor.fetchall()
    conn.close()
    return render_template('index.html', passengers=passengers)

@app.route('/create', methods=['POST'])
def create_passenger():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    # Get data from form
    # Ensure you handle exceptions and validate input data appropriately
    cursor.execute("""
        INSERT INTO Passenger (Passenger_ID,FirstName, LastName, Email, PhoneNumber, Address, Gender, DateOfBirth, City, State, Zipcode, Country)
        VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        request.form['passenger_id'],
        request.form['first_name'],
        request.form['last_name'],
        request.form['email'],
        request.form['phone_number'],
        request.form['address'],
        request.form['gender'],
        request.form['date_of_birth'],
        request.form['city'],
        request.form['state'],
        request.form['zipcode'],
        request.form['country']
    ))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:passenger_id>', methods=['POST'])
def delete_passenger(passenger_id):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Passenger WHERE Passenger_ID = ?", (passenger_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Placeholder for the update passenger endpoint
@app.route('/update/<int:passenger_id>', methods=['GET', 'POST'])
def update_passenger(passenger_id):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    if request.method == 'POST':
        # Again, ensure proper validation and error handling
        cursor.execute("""
            UPDATE Passenger SET
            FirstName = ?,
            LastName = ?,
            Email = ?,
            PhoneNumber = ?,
            Address = ?,
            Gender = ?,
            DateOfBirth = ?,
            City = ?,
            State = ?,
            Zipcode = ?,
            Country = ?
            WHERE Passenger_ID = ?
        """, (
            request.form['first_name'],
            request.form['last_name'],
            request.form['email'],
            request.form['phone_number'],
            request.form['address'],
            request.form['gender'],
            request.form['date_of_birth'],
            request.form['city'],
            request.form['state'],
            request.form['zipcode'],
            request.form['country'],
            passenger_id
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        cursor.execute("SELECT * FROM Passenger WHERE Passenger_ID = ?", (passenger_id,))
        passenger = cursor.fetchone()
        conn.close()
        return render_template('update.html', passenger=passenger)
    
@app.route('/flights', methods=['GET'])
def flights():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Flight")
    flights = cursor.fetchall()
    conn.close()
    return render_template('flights.html', flights=flights)

@app.route('/flight/delete/<int:flight_id>', methods=['POST'])
def delete_flight(flight_id):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Flight WHERE Flight_Id = ?", (flight_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('flights'))

    


if __name__ == '__main__':
    app.run(debug=True)
