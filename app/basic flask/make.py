from flask import Flask , redirect , url_for, render_template
app=Flask(__name__)

@app.route("/")
def index3():
    user = {'username':'Dhiraj'}
    posts = [
        {
            'author': {'username':'Daniel'},
            'body':'Beautiful day in SriLanka'
            },
        {
            'author' :{'username' :'Amar'},
            'body':'Tiger Zinda hey movie was so cool!'
            }
        ]
    return render_template('temp1.html',user=user,posts=posts)





if __name__== "__main__":
    app.run(debug=True) 
