from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("message", "").lower()
    
    if "invoice" in user_input:
        response = "Invoice created for this request. [PDF download soon]"
    elif "ledger" in user_input:
        response = "Here’s your vendor/customer ledger summary. [PDF or Table here]"
    elif "payment" in user_input:
        response = "Payment recorded successfully!"
    elif "purchase" in user_input:
        response = "Purchase entry recorded!"
    elif "upload" in user_input or "receipt" in user_input:
        response = "OCR: Detected ₹450 from Vishal Mart on 17 Apr"
    else:
        response = "I didn't understand that. Try commands like 'Add invoice', 'Show ledger', etc."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
