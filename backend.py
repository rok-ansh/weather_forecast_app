import requests

API_KEY = "99b2ab7af929ec4d409b702fdad82cb6"


def get_data(place, forecast_day):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    filtered_data = filtered_data[:8*forecast_day]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Mumbai", forecast_day=3))
