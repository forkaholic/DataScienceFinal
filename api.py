from flask import Flask, render_template, flash, request
import pandas as pd
import numpy as np
from joblib import load

model = load('Static/followers_prediction.joblib')

# an awesome password
secret = "SUPERSECRET"

app = Flask(__name__, template_folder='Templates')
app.config.from_mapping(
        SECRET_KEY=secret)

# Helper for check
# If form is valid, generate result page using joblib
def create_result(form):
    form[4] = 1 if form[4] == "on" else 0
    form[5] = 1 if form[5] == "on" else 0
    x = np.array([form[0],form[1],form[2],form[3],form[4],form[5]])
    return f"""
    <html>
    <body>
        Watch Time: {str(form[0])} <br/><br/>
        Stream Time: {str(form[1])} <br/><br/>
        Average Viewers: {str(form[2])} <br/><br/>
        Follower Count: {str(form[3])} <br/><br/>
        Partnered: {str(form[4])} <br/><br/>
        Mature Content: {str(form[5])} <br/><br/>
        Predicted Yearly Followers Gained: {str(model.predict(x.reshape(1,-1))[0])} <br/><br/>
        NOTE: The predicted follower count is only accurate to a point <br/> 
        for users with an already substantial following <br/><br/>
        <a href="/">Return to form</a>
    </body>

</html>
    """

# Default path on ip
# Only serves base template for form entry
@app.route("/")
def index():
    return render_template("index.html")

# Takes input from user
# Serves a flash or result
@app.route("/check", methods=["POST"])
def check():
    req = request.form
    print(str(req))
    form = [int(req["watch"]), int(req["stream"]), int(req["avg"]),
            int(req["follow"]), req["part"], req["mat"]]
    return create_result(form)

if __name__ == "__main__":
    # real ip is 73.60.142.217
    app.run(debug=True, host='10.0.0.119', port=5000)