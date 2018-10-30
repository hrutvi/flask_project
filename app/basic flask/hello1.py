from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
     return "Hello World!"

#url variable name and function parameter should be same

@app.route("/hi/<name>")
def hello_name(name):
     return "Hello %s!" %name   #string

@app.route("/hi/<int:name>")
def hello_name2(name):
     return "Hello %d!" %name   #integer

@app.route("/hi/<int:name>")
def hello_name1(name):
     return "Hello %f!" %name     #float


if __name__== "__main__":
    app.run(debug=True) 
