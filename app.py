from flask import Flask

# to create an account to use with testing go to:
# http://flapjack.rudge-lab.org/authentication?initialTab=signup

app = Flask(__name__)

@app.route("/status")
def status():
    return("The Authorisation Test Plugin Flask Server is up and running")


@app.route("/login", methods=["GET"])
def login():
    resp = {}

    # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~~~~
    login_url = "http://flapjack.rudge-lab.org:8000/api/auth/log_in/"
    login_data = {'username':'<username>','password' : '<password>'}
    login_headers = {}
    login_params = {
                    'username': {'type': 'text', 'description': 'This is the username for yoru account', 'options': [], 'default': [], 'restrictions': {}},
                    'password': {'type': 'password', 'description': 'This is your password', 'options': [], 'default': [], 'restrictions': {}}
                   }
    token_params = {'access':"access", 'refresh':'refresh'}
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    resp['login_url'] = login_url
    resp['login_data'] = login_data
    resp['login_headers'] = login_headers
    resp['login_parameters'] = login_params
    resp['token_parameters'] = token_params
    return resp

@app.route("/refresh", methods=["GET"])
def refresh():
    resp = {}

    # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~~~~
    login_url = "http://flapjack.rudge-lab.org:8000/api/auth/refresh/"
    login_data = {'refresh':'<refresh>'}
    login_headers = {}
    token_params = {'access':"access"}
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    resp['login_url'] = login_url
    resp['login_data'] = login_data
    resp['login_headers'] = login_headers
    resp['token_parameters'] = token_params
    return resp