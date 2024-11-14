from flask import Flask, request, render_template
from Attractions_API_FINAL import get_attractions  # Adjust import as needed
from Restaraunt_API_FINAL import get_restaurants  # Adjust import as needed
from Weather_API_FINAL import get_weather  # Adjust import as needed

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        city = request.form['city']
        state = request.form['state']
        area_km = request.form['area_km']

        # Call the functions from your API files to get data
        weather = get_weather(city, state)
        attractions = get_attractions(city, state, area_km)
        restaurants = get_restaurants(city, state, area_km)

        return render_template('results.html', 
                               city=city, state=state, 
                               weather=weather, 
                               attractions=attractions, 
                               restaurants=restaurants)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs on EC2 with public access
