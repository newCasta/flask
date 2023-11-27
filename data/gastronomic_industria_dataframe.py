import json
import uuid
import pandas as pd
import numpy as np

LOCATION_ROW = "location"
AVERAGE_CLIENT_PER_DAY = "average_client_day"
AVERAGE_EARNINGS_PER_DAY = "average_earnings_day"
MY_COLUMNS = {
    "NOMBRE": "name",
    "TELEFONO": "phone",
    "EMAIL": "email",
    "DIRECCION": "direction",
    "TIPO DE ESTABLECIMIENTO": "type_establishment",
    "LOACION": LOCATION_ROW,
    "PROMEDIO DE GANANCIAS POR DIA": AVERAGE_EARNINGS_PER_DAY,
    "PROMEDIO DE CLIENTES POR DIA": AVERAGE_CLIENT_PER_DAY,
}
MY_COLUMNS_TYPES = {
    "name": "string",
    "phone": "string",
    "email": "string",
    "direction": "string",
    "type_establishment": "string",
    LOCATION_ROW: "string",
    AVERAGE_CLIENT_PER_DAY: "int",
    AVERAGE_EARNINGS_PER_DAY: "int",
}

r_df = pd.read_csv("./data/industria_gastronomica.csv")
r_df = r_df.rename(columns=MY_COLUMNS)
r_df = r_df.astype(MY_COLUMNS_TYPES)  # type: ignore
r_df = r_df.replace(np.nan, "n/a")

r_df["name"] = r_df["name"].str.lower()
r_df["direction"] = r_df["direction"].str.lower()
r_df["type_establishment"] = r_df["type_establishment"].str.lower()
r_df["type_establishment"] = r_df["type_establishment"].apply(
    lambda x: x.replace("á", "a")
)
r_df = r_df[r_df["type_establishment"].str.contains("restaurante")]
r_df["phone"] = r_df["phone"].apply(lambda x: x.replace(".0", ""))
r_df["email"] = r_df["email"].apply(lambda x: x.replace("NO", "N/A"))


def get_restaurants_obj():
    restaurants_json = json.loads(r_df.to_json(orient="records"))
    restaurants = []

    for restaurant in restaurants_json:
        id = str(uuid.uuid4())

        restaurant["id"] = id

        restaurants.append(restaurant)

    return restaurants
