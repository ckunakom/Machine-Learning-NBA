from flask import current_app as app
from flask import render_template
from flask import Flask, jsonify, redirect, send_file
import json

# Setup Flask Local Serve
app = Flask(__name__)


@app.route('/')
def home():
    """Landing page."""
    return render_template("index.html",
                           title="NBA Game Predictor",
                           description="Predict matchups from your favorite NBA teams")


# Use the <qid> as the param if needed.  Not sure how many endpoint we will need yet
@app.route('/data_api')
def data_api():
    """Put DocStrings in here"""
    return None


@app.route('/getTeamLogo/<teamName>')
def return_team_icon(teamName):
    """Returns the team logo when called from the javascript file"""
    return send_file(f'icons/{teamName}.gif', mimetype='image/gif')


if __name__ == "__main__":
    app.run(debug=True)
