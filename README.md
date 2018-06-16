# Real Estate Price Prediction

A web portal that makes use of machine learning techniques to predict housing prices in Mumbai (Central and Western lines). The prediction is based on actual listings obtained from 99acres.com. The selling prices of properties are predicted based on features like location, area, number of bedrooms, furnishing, parking, etc. In order to select a prediction method, various regression methods were explored and compared. Decision tree regression was chosen as it has the advantages of fast training time, higher accuracy and can handle missing values.

## Deploying the website on https://www.pythonanywhere.com/

Clone the repository:

```
git clone https://github.com/iPrathamKumkar/Real-Estate-Price-Prediction-Flask.git
```

Install the pre-requisite libraries:

```
pip install requirements.txt
```

Edit the adresses on lines 9 and 12 in the main.py file to match the path in your system

```
training_data = '.../data/99acres.csv'
model_directory = '.../model'
```

For more information, visit https://help.pythonanywhere.com/pages/Flask/

## Built With

* [Flask](http://flask.pocoo.org/docs/1.0/) - The web framework used
* [Python](https://www.python.org/doc/) - The scripting language used

## Authors

* **Prathamesh Kumkar** * -(https://github.com/iPrathamKumkar)
* **Ishan Madan** * -(https://github.com/ishanmadan1996)