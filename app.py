#!/usr/bin/python3
"""
the main module of the app
"""
from backend_code.database.data_operations import close_session, get_data_with_email, get_data, insert_data
from backend_code.word_fliter import words_filter
from flask import Flask, make_response, jsonify, request, render_template, make_response
from flask_cors import CORS
import re
from validate import validate


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/spam_filter", strict_slashes=False, methods=['GET'])
def reder_main_page():
    """ reder the main page of spam filter """
    return render_template("spam_filter.html")

@app.route("/spam_filter/check", strict_slashes=False, methods=['POST'])
def filter_content():
    """ filter the content and decide if the email is spam or ham """
    valid = validate(request.json["email"], request.json["content"])
    if (valid != "okay"):
        return jsonify({"state": valid})
    dict = {}
    result = ""
    output = None
    for item in request.json:
        dict[item] = request.json[item]
    
    result, ham, spam = words_filter(dict["content"], dict["email"])

    if result != "Spam Email":
        output = get_data_with_email(dict["email"])
        if output is not None:
            result = "Spam Email"

    return jsonify({"state": result, "spam": spam, "ham": ham})

@app.route("/spam_filter/add_email", strict_slashes=False, methods=['POST'])
def add_email():
    """ add email in case the user doesn't expect to get emails from this email address"""
    email = request.json["email"]
    pattern = r"[\w-]{5,}(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}"
    result = re.match(pattern, email)

    if email is not None and result:
        insert_data(email)
    else:
            return jsonify({"state": "bad_request"})
    return jsonify({"state": "okay"})

@app.route("/spam_filter/get_data", strict_slashes=False, methods=['GET'])
def retieve_data():
    """ get all data from the database """
    return jsonify(get_data())

@app.teardown_appcontext
def teardown(exc):
    """ hanle teardown_qppcontext """
    close_session()

@app.errorhandler(404)
def not_found(error):
    """ handler for 404 errors """
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)

