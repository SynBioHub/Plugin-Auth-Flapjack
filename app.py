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
    token_params = {'access':'access', 'refresh':'refresh'}
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
    refresh_exists = True
    refresh_url = "http://flapjack.rudge-lab.org:8000/api/auth/refresh/"
    refresh_data = {'refresh_token':'<refresh>'}
    refresh_headers = {}
    refresh_token_name = 'refresh'
    token_params = {'access':"access"}
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if refresh_exists:
        resp['refresh_url'] = refresh_url
        resp['refresh_data'] = refresh_data
        resp['refresh_headers'] = refresh_headers
        resp['refresh_token_name'] = refresh_token_name
        resp['token_parameters'] = token_params
        return resp
    else:
        return 'This login does not provide refresh tokens', 503


@app.route("/logout", methods=["GET"])
def logout():
    resp = {}

    # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~~~~
    logout_exists = False
    # logout_url = "https://authtesting.synbiohub.org/logoutAPI"
    # logout_data = {'login_token':'<login_token>'}
    # logout_headers = {}
    # login_token_name = 'login_token'
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if logout_exists:
        resp['logout_url'] = logout_url
        resp['logout_data'] = logout_data
        resp['logout_headers'] = logout_headers
        resp['login_token_name'] = login_token_name
        return resp
    else:
        return 'This login does not provide a logout endpoint', 503