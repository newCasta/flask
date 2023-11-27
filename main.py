import json
import os
from flask import Flask

# from data.gastronomic_industria_dataframe import restaurants_json

app = Flask(__name__)


@app.route("/restaurants")
def get_restaurants():
    # return {"restaurants": json.loads(restaurants_json)}
    return "a"


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
