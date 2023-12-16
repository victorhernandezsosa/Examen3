import json

data = {"name": "Andres Iniesta", "position": "Centrocampista", "nationality": "Spanish",
        "date_of_birth": "May 11, 1984", "clubs": [
        {
            "name": "FC Barcelona",
            "period": "2002-2018"
        },
        {
            "name": "Vissel Kobe",
            "period": "2018-present"
        }
    ], "honors": [
        "FIFA World Cup winner (2010)",
        "UEFA European Championship winner (2008, 2012)",
        "UEFA Champions League winner (2005-06, 2008-09, 2010-11, 2014-15)"
    ]}

data["position"] = "Nuevo Centrocampista"
data["clubs"][0]["period"] = "2002-2020"
data["clubs"][1]["period"] = "2018-2023"

with open('Examen_Victor.json', 'w') as file:
    json.dump(data, file, indent=4)

print("El Archivo se ha modificado y guardado como 'Examen_Victor.json'.")
