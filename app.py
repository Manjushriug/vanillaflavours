from flask_googlemaps import GoogleMaps, Map, icons
from flask import Flask,render_template,request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'testvanillaflavours@gmail.com'
app.config['MAIL_PASSWORD'] = 'Welcome@123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


#Route for Landing page
@app.route("/")
def hello():
    latitude = '37.4300'
    longitude = '-122.1400'
    return render_template("Welcome.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
    print("Send Email")
    msg = Message('Hello',sender ='testvanillaflavours@gmail.com',recipients = ['vanilladream.vd@gmail.com'])
    print(request.form["usrname"])
    msg.body = "Message from" + " "+ request.form["usrname"] + " " + request.form["Email"] + " " + request.form["DateTime"]+ "with a message"+" "+ request.form["Message"]
    mail.send(msg)
    return 'Sent'

if __name__ == "__main__":
    
    GoogleMaps(app)
    #mail = Mail(app)
    
    app.run(debug=True)
    # configuration of mail
    
