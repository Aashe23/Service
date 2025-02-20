from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/back")
def sendOutput():
    return jsonify({"message": "Good Evening!"})

if __name__ == "__main__":
    app.run(debug=True)
