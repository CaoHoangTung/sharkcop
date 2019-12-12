from joblib import load

import numpy as np

class Functions():
    def check_vector(vec):
        try:
            vec = np.asarray(vec).reshape(1,-1)
            svclassifier = load('model/pre_model.joblib') 
            
            y_pred_test = svclassifier.predict(vec)
            
            print("X=%s, Predicted=%s" % (vec, y_pred_test[0]))
            # chay model
            res = y_pred_test[0]
            return res
        except Exception as e:
            print(e)
            print("Invalid vector")
            return 2