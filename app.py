from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# ---------- SAFE MATH ENGINE ----------
def calculate(expression):
    expression = expression.replace("^", "**")

    # Allow only numbers and math operators
    if not re.fullmatch(r"[0-9+\-*/().\s**]+", expression):
        return "❌ Invalid math expression"

    try:
        result = eval(expression, {"__builtins__": {}})
        return result
    except:
        return "❌ Error in calculation"

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"].strip()

    # Greetings
    if user.lower() in ["hi", "hello", "yo", "hey"]:
        return jsonify(reply="👋 I’m MathPro. Send me a math problem.")

    # Math detection
    if any(op in user for op in "+-*/^()"):
        return jsonify(reply=str(calculate(user)))

    return jsonify(reply="🧮 I only solve math. Example: (5+3)^2")

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True, threaded=True)
    if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)