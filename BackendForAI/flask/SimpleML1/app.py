import numpy as np
from flask import Flask, request ,render_template
import pickle
import math


app=Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    predction=model.predict(final_features)
    output=round(predction[0])
    return render_template('index.html',prediction_text='Number of Weekly Rides Should Be {}'.format(output))





if __name__=='__main__':
    app.run(debug=True)