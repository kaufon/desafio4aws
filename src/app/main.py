from flask import Flask, render_template, request,redirect
import mysql.connector  

app = Flask(__name__, template_folder='../ui/templates', static_folder='../ui/static')

db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'jean',
    'database': 'jean'
}
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=["POST"])
def send_message():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        add_data = ("INSERT INTO EMAIL (name, email, subject, message) VALUES (%s, %s, %s, %s)")
        data = (name, email, subject, message)
        cursor.execute(add_data, data)
        conn.commit()
        cursor.close()
        
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
