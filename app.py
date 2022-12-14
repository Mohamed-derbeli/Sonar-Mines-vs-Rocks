#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %load predict.py
# import important modules



import numpy as np
from flask import Flask, request, render_template
import pickle5
from waitress import serve

#Create an app object using the Flask class.
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle5.load(open('models/model.pkl', 'rb'))
pca = pickle5.load(open('models/pca.pkl', 'rb'))
# model = pickle.load(open('../Sonar-Mines-Rocks/models/model.pkl','rb'))

#Define the route to be home.
#The decorator below links the relative route of the URL to the function it is decorating.
#Here, home function is with '/', our root directory.
#Running the app sends us to index.html.

#Note that render_template means it looks for the file in the templates folder.

#use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def home():
    return render_template('index.html')

#You can use the methods argument of the route() decorator to handle different HTTP methods.
#GET: A GET message is send, and the server returns data
#POST: Used to send HTML form data to the server.
#Add Post method to the decorator to allow for form submission.
#Redirect to /predict page with the output
@app.route('/predict',methods=['POST'])
def predict():


    text= request.form['Input']  #.values()
    text=text.replace(" ", "")
    text= text.split(",")
    print(text)


    # request.form.values()

    int_features = [float(x) for x in text] #Convert string inputs to float.
    features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
    pca_features= pca.transform(features)
    prediction = model.predict(pca_features)  # features Must be in the form [[a, b]]

    output = round(prediction[0], 2)
    detect=" "
    if output>0.5:
        detect= 'Mine'
    else:
        detect= "Rock"

    return render_template('index.html', prediction_text='Detection: {}'.format(detect))

#When the Python interpreter reads a source file, it first defines a few special variables.
#For now, we care about the __name__ variable.
#If we execute our code in the main program, like in our case here, it assigns
# __main__ as the name (__name__).
#So if we want to run our code right here, we can check if __name__ == __main__
#if so, execute it here.
#If we import this file (module) to another file then __name__ == app (which is the name of this python file).

if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=8855)
    app.debug=True
    app.run()


# app.run(host="0.0.0.0")
