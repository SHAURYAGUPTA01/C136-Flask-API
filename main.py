from flask import Flask,jsonify,request
from data import data

obj = Flask(__name__)

@obj.route("/")
def add_data():
    return jsonify({"data": data,"message" : "success"}),200

@obj.route("/planet")
def planet():
    name = request.args.get("name")
    pdata = next(item for item in data if item["name"] == name )

    return jsonify({"data": pdata,"message" : "success"}),200


if __name__ == "__main__":
    obj.run(debug = True)
#http://127.0.0.1:5000/planet?name=ComaeBerenicesb