from flask import Flask, request, jsonify

import ddbb

app = Flask(__name__)

@app.route('/createSaurio', methods=['POST'])
def createSaurio():
    response = {"code_response":0,
                "message":""}
    jsonsaurio = request.get_json()
    print(jsonsaurio)
    try:
        ok_insertar = ddbb.createSaurio(jsonsaurio)
        if not ok_insertar:
            response["code_response"] = 1
            response["message"] = "Fallo de conexion"
        else:
            response["code_response"]=0
            response["message"]="Dinosaurio insertado correctamente"

    except Exception as e:
        print(e)
        response["code_response"] = 2
        response["message"] = "El dinosaruio ya existe"


    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)