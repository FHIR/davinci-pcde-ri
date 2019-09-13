from flask import *
import requests
import os

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)
@app.route('/Patient')
def patient(name=None):
    return render_template('patient.html', name=name)

@app.route('/Bundle')
def bundle(name=None):
    return render_template('bundle.html', name=name)

@app.route('/getpatient')
def get_patient():
    headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
    given = request.args.get('given')
    family = request.args.get('family')
    bdate = request.args.get('birthdate')
    url = 'https://davinci-pcde-ri.logicahealth.org/fhir/Patient?given='+given+'&family='+family+'&birthdate='+bdate
    r = requests.get(url, headers=headers, verify=False)
    print (r)
    json_data = json.loads(r.text)
    return jsonify(**json_data)
@app.route('/getbundle')
def get_bundle():
    headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
    id = request.args.get('id')
    url = 'https://davinci-pcde-ri.logicahealth.org/fhir/Bundle/' + id
    r = requests.get(url, headers=headers, verify=False)
    print (r)
    json_data = json.loads(r.text)
    return jsonify(**json_data)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
if __name__ == "__main__":
    app.run(ssl_context='adhoc')
