#this is a sample flask application

from flask import Flask
app= Flask(__name__)
@app.route("/")
def hello():
    return "<h2> hello prasanna</h2><hr/>"
app.run(debug=True,host="0.0.0.0",port=3000) 
