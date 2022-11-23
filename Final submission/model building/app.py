import numpy as np


from flask import Flask, request, jsonify, render_template


import pickle
#importing the inputScript file used to analyze the URL





app=Flask (__name__) 
model=pickle.load(open('Phishing_Website.pkl', 'rb')) 
#Redirects to the page to give the user iput URl




@app.route('/')

def predict():
    return render_template('index.html')

@app.route('/testing')
def Clickhere ():
    return render_template('testing.html')
#Fetches the URL given by the URL and passes to inputScript
@app.route('/y_predict', methods=['POST'])




def y_predict():

    predict= request.form['testing.html'] 
    checkprediction = inputScript.main(url) 
    prediction = model.predict(checkprediction)
    print(prediction) 
    output=prediction[0] 
    if (output==1): 
        pred="Your are safe!! This is a Legitimate Website."
    else:
        pred="You are on the wrong site. Be cautious!" 
        return render_template('testing.html', prediction_text='{}'.format(pred), url=url)


#Takes the input parameters fetched from the URL by inputScript and returns the predictions 
@app.route('/predict_api',methods=['POST'])


def predict_api():

    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])




    output = prediction[0]

    return jsonify (output)
if __name__ =='__main__': 
    app.run(host='0.0.0.0', debug=True)
