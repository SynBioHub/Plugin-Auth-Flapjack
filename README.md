# Plugin-Visual-Test
An authorisation plugin for flapjack.

# Install
## Using docker
Run `docker run --publish 8102:5000 --detach --name python-test-plug synbiohub/plugin-auth-flapjack:snapshot`
Check it is up using localhost:8102.  

## Using Python
Run `pip install -r requirements.txt` to install the requirements. Then run `FLASK_APP=app python -m flask run`. A flask module will run at localhost:5000/.
