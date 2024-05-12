#this is a sample flask application

from flask import Flask
app= Flask(__name__)
@app.route("/")
def hello():
    return "<h2>CI/CD hhh12567</h2><hr/>"
app.run(debug=True,host="192.168.43.154",port=3000) 
