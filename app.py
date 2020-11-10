from flask import Flask, redirect, render_template
from flask_pymongo import PyMongo
import infoscrape
import pymongo

# Create an instance of Flask app
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/marsapp"
mongo = PyMongo(app)


@app.route("/")
def home():

    mars_info = mongo.db.mars_info.find_one()

    return render_template("index.html", mars_info=mars_info)

@app.route("/scrape")
def scrape():

    mars_info = mongo.db.mars_info
    mars_data = infoscrape.infoscrape_news()
    mars_data = infoscrape.infoscrape_image()
    mars_data = infoscrape.infoscrape_facts()
    mars_data = infoscrape.infoscrape_hemispheres()
    mars_info.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug= True)
