import requests
import pandas as pd
from datetime import datetime

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Government:
    def senate(self, name="", ticker="", date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        data = requests.get(f"{BASE_URL}/government/senate/?name={name}&"
                            f"ticker={ticker}&date_from={date_from}&date_to={date_to}").json()
        return pd.DataFrame(data["senate"])

    def house(self, name="", ticker="", state="", date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        data = requests.get(f"{BASE_URL}/government/house/?name={name}&"
                            f"ticker={ticker}&state={state}&date_from={date_from}&date_to={date_to}").json()
        return pd.DataFrame(data["house"])
