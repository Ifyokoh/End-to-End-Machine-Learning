from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
import json
from database.database import Database

database = Database()


with open("model.pkl", "rb") as f:
    model = pickle.load(f)


app = Flask(__name__)

filename = 'model.pkl'
model = pickle.load(open(filename, 'rb'))

class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

@app.route("/")
def template():
    return render_template('index.html')

@app.route("/predict", methods = ['POST'])
def predict():
    
    if request.method == "POST":
        bed = int(request.form['bed'])
        bath = int(request.form['bath'])
        toilet = int(request.form['toilet'])
        new = int(request.form['new'])
        furnished = int(request.form['furnished'])
        serviced = int(request.form['serviced'])
        location = int(request.form['location'])

        data = np.array([[bed, bath, toilet, new, furnished, serviced, location]])
        # lis = data.tolist()
        # # output = json.dumps(lis)
        # output = jsonify(lis)
        prediction = model.predict(data)
    # database.insert_record(output, prediction)
    return render_template("index.html", n = prediction )

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    input = json.dumps(data)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    database.insert_record(input, output)
    return jsonify(output)

    
if __name__ == "__main__":
    app.run(debug = True)