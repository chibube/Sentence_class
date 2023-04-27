from flask import Flask, request, render_template
from models import Prediction_pipeline

application=Flask(__name__)

app=application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict_sent():
    if request.method=='GET':
        return render_template('home.html')
    else:
        sentiment_prediction = Prediction_pipeline()
        sentiment = sentiment_prediction.predict(request.form.get('review'))

        return render_template('home.html', sentiment=sentiment)



if __name__ =="__main__":
    app.run(host="0.0.0.0")