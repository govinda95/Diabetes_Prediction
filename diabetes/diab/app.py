from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('diabetes.pickle', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Glucose = int(request.form['Glucose'])

        BloodPressure = int(request.form['BloodPressure'])

        SkinThickness = int(request.form['SkinThickness'])

        Insulin = int(request.form['Insulin'])

        BMI = float(request.form['BMI'])

        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        
        values = np.array([[Glucose ,BloodPressure, SkinThickness ,Insulin, BMI ,DiabetesPedigreeFunction]])
        prediction = model.predict(values)

        if prediction ==0:
            prediction = 'is not'
        else:
            prediction = 'is'
            
        return render_template('result.html', prediction_text='Patient {} Suffering from Diabetes '.format(prediction))



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
    app.run(debug=True)



