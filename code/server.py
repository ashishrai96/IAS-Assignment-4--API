
import pickle
import numpy as np
from flask import Flask, request

app = Flask(__name__)

@app.route("/getInfo", methods=["POST"])
def getInfo():
    """
    This fn predicts the survival of the passenger 
    using the preprocessed model.pkl file.

    Expected Request body:
        {
            "data": []
        }
    """
    
    req_body = request.get_json()
    X_test = np.array([req_body['data']])

    model = pickle.load(open("model.pkl", "rb"))
    y_pred = model.predict(X_test)
    return str(y_pred[0])


if __name__=="__main__":
    app.run(port=8090, debug=True)