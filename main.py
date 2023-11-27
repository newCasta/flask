import os
from flask import Flask, jsonify
from data.gastronomic_industria_dataframe import restaurant_json

app = Flask(__name__)


@app.route("/restaurants")
def get_restaurants():
    return restaurant_json


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
