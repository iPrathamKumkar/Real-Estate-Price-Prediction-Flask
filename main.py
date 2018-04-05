import traceback
from flask import Flask, request, jsonify, render_template, redirect, url_for
import pandas as pd
from sklearn.externals import joblib
global predicted_value
predicted_value = 0.0
app = Flask(__name__)
# Inputs
training_data = '/home/RealEstatePrice/price/data/99acres.csv'
include = ['Carpet_Area', 'Floor_Number', 'Parking', 'Furnishing', 'Location', 'Bathrooms', 'Bedrooms','Price']
dependent_variable = include[-1]
model_directory = '/home/RealEstatePrice/price/model'
model_file_name = '%s/model.pkl' % model_directory
model_columns_file_name = '%s/model_columns.pkl' % model_directory
# These will be populated at training time
model_columns = None
clf = None
# Home page
@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        if clf:
            try:
                json_ = request.get_json(silent=True)
                query = pd.get_dummies(pd.DataFrame(json_))
                query = query.reindex(columns=model_columns, fill_value=0)
                prediction = list(clf.predict(query))
                global predicted_value
                predicted_value = prediction[0]
                return 'Success'
            except Exception as e:
                return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    predicted_price = predicted_value
    predicted_price1 = 0.93*predicted_price/100
    predicted_price2 = 1.07*predicted_price/100
    predicted_price1 = round(predicted_price1, 2)
    predicted_price2 = round(predicted_price2, 2)
    predicted_value = 0.0
    return render_template('index.html', val1 = predicted_price1, val2 = predicted_price2)
# Train the model
@app.route('/train', methods=['GET'])
def train():
    # Training the data using Random Forest algorithm
    from sklearn.ensemble import RandomForestRegressor as rf
    df = pd.read_csv(training_data)
    df_ = df[include]
    # One-hot encoding categorical variables
    categoricals = []
    for col, col_type in df_.dtypes.iteritems():
        if col_type == 'O':
            categoricals.append(col)
        else:
            # Fill NaNs with 0
            df_[col].fillna(0, inplace=True)
    # get_dummies() effectively creates one-hot encoded variables
    df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)
    x = df_ohe[df_ohe.columns.difference([dependent_variable])]
    y = df_ohe[dependent_variable]
    # Capture a list of columns that will be used for prediction
    global model_columns
    model_columns = list(x.columns)
    joblib.dump(model_columns, model_columns_file_name)
    global clf
    clf = rf()
    clf.fit(x, y)
    joblib.dump(clf, model_file_name)
    return redirect(url_for('main'))