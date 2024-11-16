# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan
# lentokentän nimen ja kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä
# lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan 
# muodossa: http://127.0.0.1:3000/kenttä/EFHK. 
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

import mysql.connector
from flask import Flask, Response, request
import json

app = Flask(__name__)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         autocommit=True
         )

@app.route('/kenttä/<icao>')
def hae_lentokentta_icao_koodilla(icao):
    sql = f"SELECT ident, name, municipality FROM airport WHERE ident = %s"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    kenttä = kursori.fetchone()
    
    vastaus = {
        "ICAO" : kenttä["ident"],
        "Name" : kenttä["name"],
        "Municipality" : kenttä["municipality"]
    }

    json_vastaus = json.dumps(vastaus)
    return Response(response=json_vastaus, mimetype='application/json')

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)