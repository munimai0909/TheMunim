from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_cors import CORS
from logic import invoice, ledger, ocr, drive
from login.auth import register_user, login_user
from login.session import set_user_session, get_user_from_session, clear_session

app = Flask(__name__)
app.secret_key = 'munim-ai-secret'
CORS(app)

@app.route('/')
def home():
    if 'session_id' in session:
        return redirect(url_for('chat_ui'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if register_user(uname, pwd):
            return redirect(url_for('login'))
        else:
            return "User already exists."
    return '''
        <form method="POST">
            <input name="username" placeholder="Username"><br>
            <input name="password" type="password" placeholder="Password"><br>
            <button type="submit">Register</button>
        </form>
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if login_user(uname, pwd):
            session['session_id'] = uname
            set_user_session(uname, uname)
            return redirect(url_for('chat_ui'))
        else:
            return "Login failed. Try again."
    return '''
        <form method="POST">
            <input name="username" placeholder="Username"><br>
            <input name="password" type="password" placeholder="Password"><br>
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/logout')
def logout():
    sid = session.get('session_id')
    if sid:
        clear_session(sid)
    session.clear()
    return redirect(url_for('home'))

@app.route('/chat_ui')
def chat_ui():
    if 'session_id' not in session:
        return redirect(url_for('login'))
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    if 'session_id' not in session:
        return jsonify({"response": "Please log in first."})
    
    username = get_user_from_session(session['session_id'])
    user_input = request.form.get("message", "").lower()

    if "invoice" in user_input:
        response = f"Invoice created for {username}"
    elif "ledger" in user_input:
        response = f"Here is your ledger, {username}"
    elif "payment" in user_input:
        response = "Payment recorded."
    elif "purchase" in user_input:
        response = "Purchase entry recorded."
    elif "upload" in user_input or "receipt" in user_input:
        response = "OCR processed: ₹450 from Vishal Mart"
    else:
        response = "Sorry, I didn’t get that. Try 'Add invoice', 'Show ledger' etc."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
