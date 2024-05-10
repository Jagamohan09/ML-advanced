from flask import Flask,request,jsonify
import joblib
import pandas as pd

# CREATE A FLASK APPLICATION
app = Flask(__name__)



#CONNECT POST API CALL ---> PREDICT_FUNCTION()  https://localhost:5000/predict
@app.route('/predict',methods=['POST'])
def predict():
    
    # GET JSON REQUEST
    feat_data = request.json
        
    # CONVERT JSON TO PANDAS DATAFRAME (mk sure that the col name matches)
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns = col_name)
    
    #PREDICT
    prediction = list(model.predict(df))
    
    
    return  jsonify({'prediction':str(prediction)})  #PREDICTION


# LOAD MY MODEL and LOAD COLUMN NAME
if __name__ =='__main__':
    model = joblib.load('final_model.pkl')
    col_name = joblib.load('column_names.pkl')
    
    app.run(debug=True)