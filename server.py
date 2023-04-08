
import emailss

from flask import Flask, request
app = Flask(__name__)


@app.route("/api/send" , methods=["POST"])
def process_data():
    data = request.json
    sender = request.json["sender"]
    reciever = request.json["reciever"]
    object = request.json["object"]
    message = request.json["message"]

    #process the data
    error = 1
    try:
        emailss.envoyer_mail(sender, reciever , object, message)
    except:
        error = 2

    
    app.logger.info(request.json)
    return{"send" : error}

if __name__ == "__main__":
    app.run(debug=True)

