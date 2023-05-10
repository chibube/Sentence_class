import pickle
import os

class Prediction_pipeline():
    def __init__(self):
        pass

    def predict(self, review):
        '''
        this function unpickles the model vectorizer and classifier and uses it to predict the sentiment of our review
        '''
        classifier_path = os.path.join("artifacts","New","model_spc.pickle")
        vectorizer_path = os.path.join("artifacts","New","spacy_vec.pickle")
        scaler_path = os.path.join("artifacts","New", "mm_scaler.pickle")

        with open(classifier_path, 'rb') as f:
            classifier = pickle.load(f)

        with open(vectorizer_path, 'rb') as f:
            vectorizer = pickle.load(f)

        with open(scaler_path, 'rb') as f:
            scaler = pickle.load(f)

        prediction = classifier.predict(scaler.transform(vectorizer(str(review)).vector.reshape(1,300)))

        if prediction.item() == 1:
            result = "positive"
        else:
            result = "negative"
        
        return result