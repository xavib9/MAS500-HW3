from flask import Flask, render_template
import json
import feedparser
import globalvoices

#Variable to choose the number of stories
numStory = 5

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("stories.html",
        country_list_json_text=json.dumps(globalvoices.country_list())
    )

@app.route("/country/<country>")
def country(country):

    stories = globalvoices.recent_stories_from( country, numStory ) #We send the variable through this function
    return render_template("stories.html",
        country_list_json_text=json.dumps(globalvoices.country_list()),
        country_name=country,
        stories=stories
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
