from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np


with open("model.pkl", "rb") as f:
    model = pickle.load(f)


app = Flask(__name__)

filename = 'model.pkl'
model = pickle.load(open(filename, 'rb'))

@app.route("/")
def template():
    return render_template('index.html')

@app.route("/predict", methods = ['POST'])
def predict():
    
    if request.method == "POST":
        bed = request.form['bed']
        bath = request.form['bath']
        toilet = request.form['toilet']
        new = request.form['new']
        furnished = request.form['furnished']
        serviced = request.form['serviced']
        location = request.form['location']

        result = np.array([[bed, bath, toilet, new, furnished, serviced, location]])
        prediction = model.predict(result)

    return render_template("index.html", n = prediction )

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

    
if __name__ == "__main__":
    app.run(debug = True)