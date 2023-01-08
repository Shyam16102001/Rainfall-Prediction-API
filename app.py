from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pickle
import json

app = FastAPI()


class model_input(BaseModel):

    day: float
    month: float
    minTemp: float
    maxTemp: float
    rainfall: float
    evaporation: float
    sunshine: float
    windGustSpeed: float
    windSpeed9am: float
    windSpeed3pm: float
    humidity9am: float
    humidity3pm: float
    pressure9am: float
    pressure3pm: float
    temp9am: float
    temp3pm: float
    cloud9am: float
    cloud3pm: float
    location: float
    winddDir9am: float
    winddDir3pm: float
    windGustDir: float
    rainToday: float


model = pickle.load(open("model.pkl", "rb"))

@app.get('/')
def main():
    return {'message': 'Testing'}


@app.post('/predict')
def rainfall_prediction(input_parameters: model_input):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    day = input_dictionary['day']
    month = input_dictionary['month']
    minTemp = input_dictionary['maxTemp']
    maxTemp = input_dictionary['maxTemp']
    rainfall = input_dictionary['rainfall']
    evaporation = input_dictionary['evaporation']
    sunshine = input_dictionary['sunshine']
    windGustSpeed = input_dictionary['windGustSpeed']
    windSpeed9am = input_dictionary['windSpeed9am']
    windSpeed3pm = input_dictionary['windSpeed3pm']
    humidity9am = input_dictionary['humidity9am']
    humidity3pm = input_dictionary['humidity3pm']
    pressure9am = input_dictionary['pressure9am']
    pressure3pm = input_dictionary['pressure3pm']
    temp9am = input_dictionary['temp9am']
    temp3pm = input_dictionary['temp3pm']
    cloud9am = input_dictionary['cloud9am']
    cloud3pm = input_dictionary['cloud3pm']
    location = input_dictionary['location']
    winddDir9am = input_dictionary['winddDir9am']
    winddDir3pm = input_dictionary['winddDir3pm']
    windGustDir = input_dictionary['windGustDir']
    rainToday = input_dictionary['rainToday']

    input_list = [location, minTemp, maxTemp, rainfall, evaporation, sunshine, windGustDir, windGustSpeed, winddDir9am, winddDir3pm,
                  windSpeed9am, windSpeed3pm, humidity9am, humidity3pm, pressure9am, pressure3pm, cloud9am, cloud3pm, temp9am, temp3pm, rainToday, month, day]

    pred = model.predict(input_list)
    output = pred
    if output == 0:
        return 'Sunny'
    else:
        return 'Rain'


if __name__ == "__main__":
    uvicorn.run(app)