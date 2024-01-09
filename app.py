from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model_filename = 'HousingPrice.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = []
        for key in request.form:
            value = request.form[key]

            features.append(int(value))

        prediction = model.predict([features])
        predicted_price = prediction[0]

        return render_template('result.html', prediction=f'Predicted Price: {predicted_price:.2f}')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
