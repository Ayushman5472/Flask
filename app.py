from logging import debug
from flask import Flask, json, jsonify, request
app = Flask(__name__)
cars = [{"id":1, "model": "Audi"}, {"id": 2, "model": "BMW"}, {"id": 3, "model": "Ferrari"}]
@app.route('/')
def home():
    return("Home Page")
@app.route('/addData', methods = ["POST"])
def carsPage():
    if not request.json:
        return jsonify({
            "status": "error", 
            "message": "data is not present"  
        },400)
    getData = {"id": cars[-1]["id"]+1,
    "model": request.json.get("model", "")}
    cars.append(getData)
    return jsonify({
        "status":"success",
        "message": "A New Model is added"
    })
@app.route('/CarModels')
def CarsDisplay():
    return jsonify({
        "data":cars
    })
if (__name__=='__main__'):
    app.run(debug = True)