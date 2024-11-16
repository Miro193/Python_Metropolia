# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. 
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. 
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. 
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

import json
from flask import Flask, request, Response

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
	alkuluku = True
	luku = int(luku)
	tulos = 'true'

	for numero in range(2, luku):
		if luku % numero == 0:
			alkuluku = False
	
	if alkuluku:
		vastaus = {
			"Number" : luku, 
			"isPrime" : tulos
		}

	if not alkuluku:
		tulos = 'false'
		vastaus = {
			"Number" : luku, 
			"isPrime" : tulos
		}
	
	json_vastaus = json.dumps(vastaus)
	return Response(response=json_vastaus, mimetype='application/json')

if __name__== '__main__':
	app.run(use_reloader=True, host='127.0.0.1', port=3000)