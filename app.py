from flask import Flask, render_template
import requests
import fontawesome as fa

app = Flask(__name__)


@app.route("/")
def home():
    covid = requests.get('https://disease.sh/v3/covid-19/all')
    covidData= covid.json()
    return render_template ("home.html", covid=covidData)

if __name__ == '__main__':
  app.run(debug=True)