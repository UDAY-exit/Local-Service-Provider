

from flask import Flask, render_template, request, redirect, session,jsonify
import mysql.connector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'uday@12345' 
bcrypt = Bcrypt(app)

# ===> Function to get a fresh DB connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="uday@12345",
        database="loco_web"
    )

@app.route('/')
def index():
    return render_template('loginForm.html')

# ✅ Login Route
@app.route("/loginHandle", methods=["POST"])
def loginHandle():
    email = request.form['email']
    password = request.form['password']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        stored_password = user[3]  # assuming (id, name, email, password)
        if bcrypt.check_password_hash(stored_password, password):
            session['user'] = user[1]  # name
            return redirect('/home')
        else:
            return render_template("loginForm.html", alert="Incorrect password.")
    else:
        return render_template("loginForm.html", alert="User does not exist.")

@app.route('/signup')
def showSignupForm():
    return render_template("signupForm.html")

@app.route("/signupHandle", methods=['POST'])
def signupHandle():
    
    name = request.form["username"]
    email = request.form['email']
    password = request.form['pass']
    hashPassword = bcrypt.generate_password_hash(password).decode('utf-8')

    conn = get_connection()  # ✅ NEW connection for each request
    cursor = conn.cursor()

    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return "User already exists. Please login or use a different email."

    # Insert new user
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, hashPassword)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/send_enquiry', methods=['POST'])
def send_enquiry():
    service = request.form['property']
    name = request.form['name']
    phoneNo = request.form['mobile']



    if service and name and phoneNo:
        conn = get_connection()
        cursor = conn.cursor()

        
        cursor.execute(
            "INSERT INTO send_enquiry (service, name, phoneNo) VALUES (%s, %s, %s)",
            (service, name, phoneNo)
        )

        conn.commit()
        cursor.close()
        conn.close()

    return redirect('/home')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/contact_service", methods=['POST'])
def contact_service():
    name = request.form['name']
    email = request.form['email']
    service = request.form['service']
    message = request.form['message']
    

    if name and email and service and message:
        conn = get_connection()
        cursor = conn.cursor()

        
        cursor.execute(
            "INSERT INTO contact_service   (name,email,service,message) VALUES (%s, %s, %s, %s)",
            (name,email,service,message)
        )

        conn.commit()
        cursor.close()
        conn.close()

    return redirect('/contact')


@app.route("/cleaning")
def cleaning_service():
    return render_template("cleaning-ser.html")

@app.route("/cleaning_enquiry", methods=['POST'])
def cleaning_enquiry():
    bookingName = request.form['bookingName']
    bookingPhone = request.form['bookingPhone']
    bookingAddress = request.form['bookingAddress']
    bookingService = request.form['bookingService']
    bookingPrice = request.form['bookingPrice']

    if bookingName and bookingPhone and bookingAddress and bookingService and bookingPrice:
        conn = get_connection()
        cursor = conn.cursor()

        
        cursor.execute(
            "INSERT INTO  cleaning_service (name,phoneNo,address,service,price_Per_Hour) VALUES (%s, %s, %s, %s, %s)",
            (bookingName,bookingPhone,bookingAddress,bookingService,bookingPrice)
        )

        conn.commit()
        cursor.close()
        conn.close()

    return redirect('/cleaning')

@app.route("/plumbing")
def plumbing_service():
    return render_template("plumbing-ser.html")


@app.route("/plumbing_enquiry", methods=['POST'])
def plumbing_enquiry():
    bookingName = request.form['bookingName']
    bookingPhone = request.form['bookingPhone']
    bookingAddress = request.form['bookingAddress']
    bookingService = request.form['bookingService']
    bookingPrice = request.form['bookingPrice']

    if bookingName and bookingPhone and bookingAddress and bookingService and bookingPrice:
        conn = get_connection()
        cursor = conn.cursor()

        
        cursor.execute(
            "INSERT INTO plumbing_service(name,phoneNo,address,service,price_Per_Hour) VALUES (%s, %s, %s, %s, %s)",
            (bookingName,bookingPhone,bookingAddress,bookingService,bookingPrice)
        )

        conn.commit()
        cursor.close()
        conn.close()

    return redirect('/plumbing')



@app.route("/Electrical")
def electrical_service():
    return render_template("Electrical-ser.html")

@app.route("/electrical_enquiry", methods=['POST'])
def electrical_enquiry():
    bookingName = request.form['bookingName']
    bookingPhone = request.form['bookingPhone']
    bookingAddress = request.form['bookingAddress']
    bookingService = request.form['bookingService']
    bookingPrice = request.form['bookingPrice']

    if bookingName and bookingPhone and bookingAddress and bookingService and bookingPrice:
        conn = get_connection()
        cursor = conn.cursor()

        
        cursor.execute(
            "INSERT INTO   electrical_service  (name,phoneNo,address,service,price_Per_Hour) VALUES (%s, %s, %s, %s, %s)",
            (bookingName,bookingPhone,bookingAddress,bookingService,bookingPrice)
        )

        conn.commit()
        cursor.close()
        conn.close()

    return redirect('/Electrical')


@app.route("/home_repair")
def home_repair_service():
    return render_template("Home_Repair-ser.html")


@app.route("/homeRepair_service", methods=['POST'])
def homeRepair_service():
    bookingName = request.form['bookingName']
    bookingPhone = request.form['bookingPhone']
    bookingAddress = request.form['bookingAddress']
    bookingService = request.form['bookingService']
    bookingPrice = request.form['bookingPrice']

    if bookingName and bookingPhone and bookingAddress and bookingService and bookingPrice:
        conn = get_connection()
        cursor = conn.cursor()

        
        cursor.execute(
            "INSERT INTO  homerepair_service  (name,phoneNo,address,service,price_Per_Hour) VALUES (%s, %s, %s, %s, %s)",
            (bookingName,bookingPhone,bookingAddress,bookingService,bookingPrice)
        )

        conn.commit()
        cursor.close()
        conn.close()

    return redirect('/home_repair')


@app.route("/product")
def product():
    return render_template("product.html")



@app.route('/submit_order', methods=['POST'])
def submit_order():
    data = request.get_json()
    items = data.get('items', [])

    if not items:
        return jsonify({'error': 'No items to submit'}), 400

    conn = get_connection()
    cursor = conn.cursor()

    for item in items:
        name = item['name']
        price = item['price']
        quantity = item['quantity']
        total = item['total']

        cursor.execute("""
            INSERT INTO orders (name, price, quantity, total)
            VALUES (%s, %s, %s, %s)
        """, (name, price, quantity, total))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
