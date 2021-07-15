from flask import Flask, app, json, request, jsonify, render_template, url_for
app = Flask(__name__,template_folder="static")
import util


@app.route("/")
def home():
    return render_template("app.html")

@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    print('Locations Requested')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bedrooms = float(request.form['bedrooms'])
    bath = float(request.form['bath'])
    balcony = float(request.form['balcony'])
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bath, balcony, bedrooms)
    })

    response.headers.add('Access Control Allow Origin', '*')
    print('Prediction Ready')

    return response


if __name__ == "__main__":
    print('--------------------                         --------------------')
    print('--------------------   starting the server   --------------------')
    print('--------------------                         --------------------')
    util.load_saved_artifacts()
    app.run()