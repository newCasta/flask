import json
import os
from flask import Flask
from flask_cors import CORS, cross_origin

from data.gastronomic_industria_dataframe import get_restaurants_obj

app = Flask(__name__)

CORS(app)


@cross_origin
@app.route("/restaurants")
def get_restaurants():
    restaurants = get_restaurants_obj()

    return {"restaurants": restaurants}


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
