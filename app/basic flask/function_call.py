from flask import Flask , redirect , url_for, render_template
app=Flask(__name__)

@app.route("/")
def index():
    
    d1 = {100:'v1',101:'v2',102:'v3'}
   

    l1= [4353,2314,2959,3382,9362,3900]

 

    t2= ('4353','2314','2959','3382','9362','3900')

    return render_template('tmp.html',t2=t2,l1=d1,list1=l1)



if __name__== "__main__":
    app.run(debug=True) 

