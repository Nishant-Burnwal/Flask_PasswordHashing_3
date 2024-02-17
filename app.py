# import Flask and Bcrypt
# pip install flask flask-bcrypt
from flask import Flask
from flask_bcrypt import Bcrypt

# making object of Flask and Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

# creating app route
@app.route('/')
def index():
    # Hashing the password using Python_decode('utf-8)
    # (Unicode Transformation Format-8) A format in the Unicode coding system that uses from one to four bytes. When coding the English language, only one byte is used per character like regular ASCII encoding.
    password = 'password'
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # verify a password
    is_valid = bcrypt.check_password_hash(hashed_password, password)
    return f"Password: {password}<br>Hashed Password: {hashed_password}<br>Is valid: {is_valid}" 

if __name__ == "__main__":
    app.run(debug=True)