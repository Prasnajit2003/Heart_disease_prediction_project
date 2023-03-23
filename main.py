from flask import Flask, render_template, request
import pickle
import numpy as np


model = pickle.load(open('Healthcare_Analysis_on_Heart_Disease.pkl','rb'))

app = Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    age = request.form.get('age')
    sex = request.form.get('sex')
    cp = request.form.get('cp')
    trestbps = request.form.get('trestbps')
    chol = request.form.get('chol')
    fbs = request.form.get('fbs')
    restecg = request.form.get('restecg')
    thalach = request.form.get('thalach')
    exang = request.form.get('exang')
    oldpeak = request.form.get('oldpeak')
    slope = request.form.get('slope')
    ca = request.form.get('ca')
    thal = request.form.get('thal')

    res = model.predict(np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, 13))
    if res[0] == 1:
        res = 'affected'
    else:
        res = 'not affected'

    return res

if __name__ == "__main__":
    app.run(debug= True)
