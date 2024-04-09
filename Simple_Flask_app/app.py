from flask import Flask, render_template
from helper import countries, summaries, activities, facts, languages, currencies

app = Flask(__name__)


@app.route("/home")
def index():
    return render_template("index.html", template_countries=countries)


@app.route("/country/<string:country_id>")
def country(country_id):
    return render_template(
        "country.html",
        template_country=countries[country_id],
        template_summary=summaries[country_id],
        template_activity=activities[country_id],
        template_fact=facts[country_id],
        template_language=languages[country_id],
        template_currency=currencies[country_id],
    )
