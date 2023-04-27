import pickle
import os

class Prediction_pipeline():
    def __init__(self):
        pass

    def predict(self, review):
        '''
        this function unpickles the model vectorizer and classifier and uses it to predict the sentiment of our review
        '''
        classifier_path = os.path.join("artifacts","classifier.pickle")
        model_path = os.path.join("artifacts","tfidfm.pickle")

        with open(classifier_path, 'rb') as f:
            classifier = pickle.load(f)

        with open(model_path, 'rb') as f:
            model = pickle.load(f)

        prediction = classifier.predict(model.transform([review]))
        
        return prediction.item()