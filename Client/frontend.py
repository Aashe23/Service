from flask import Flask
import requests

app = Flask(__name__)

@app.route("/wish")
def display():
    # Logic to connect to backend via backend-service
    response= requests.get("http://backend-service:9090/back")
    output = response.json()
    print(response.json)

if __name__ == "__main__":
    app.run("host=0.0.0.0", port = 5000)
