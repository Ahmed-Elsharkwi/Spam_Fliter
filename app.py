#!/usr/bin/python3
"""
the main module of the app
"""
from backend_code.database.data_operations import close_session, get_data_with_email
from backend_code.word_fliter import words_filter
from flask import Flask, make_response, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/spam_filter", strict_slashes=False, methods=['POST'])
def filter_content():
    """ filter the content and decide if the email is spam or ham """
    dict = {}
    result = ""
    output = None
    for item in request.json:
        dict[item] = request.json[item]
    
    result = words_filter(dict["content"], dict["email"])

    if result != "Spam Email":
        output = get_data_with_email(dict["email"])
        if output is not None:
            result = "Spam Email"
    return result

@app.teardown_appcontext
def teardown(exc):
    """ hanle teardown_qppcontext """
    close_session()

@app.errorhandler(404)
def not_found(error):
    """ handler for 404 errors """
    return make_response(jsonify({'error': 'Not found'}), 404)


app.run(host='0.0.0.0', port=5000, threaded=True)

