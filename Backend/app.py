# Import Flask framework for creating web application
from flask import Flask

# Initialize Flask application instance
app = Flask(__name__)

# Define route for root endpoint


@app.route("/")
def home():
    # Return greeting message from backend API
    return "Hello from Backend API"


# Entry point - run the Flask application
if __name__ == "__main__":
    # Start server on all available interfaces (0.0.0.0) on port 5000
    app.run(host="0.0.0.0", port=5000)
