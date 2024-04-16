#flask scikit-learn pandas pickle-mixin
import pandas as pd
import pickle
from  flask import Flask, render_template , request
app = Flask(__name__)
data =pd.read_csv("cleaned.csv")

pipe = pickle.load(open('RidgeModel.pkl', 'rb'))
# Assuming bhk and bath are strings containing numeric values



@app.route('/')
def index():
    locations= sorted(data['location'].unique())
    return render_template('index.html',locations=locations)

@app.route('/predict',methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk= float(request.form.get('bhk'))
    bath= float(request.form.get('Bath'))
    sqft= request.form.get('total_sqft')
    print(location,bhk,bath,sqft)

    input= pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','bhk','bath','sqft'])\
    prediction = pipe.predict(input)[0]

    return str(prediction)

if __name__ == '__main__':
    app.run(debug=True , port=5000)