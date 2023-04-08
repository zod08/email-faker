
import emailss

from flask import Flask, request
from flask_cors import CORS
from flask_cors import cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "https://stellar-marshmallow-3b21c9.netlify.app"}})


@app.route("/api/send" , methods=["GET","POST"])
@cross_origin()
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

