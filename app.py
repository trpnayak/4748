#this is a sample flask application

from flask import Flask
app= Flask(__name__)
@app.route("/")
def hello():
    return "<h2> hello prasanna</h2><hr/>"
app.run(debug=True,host="192.168.43.175",port=3000) 
