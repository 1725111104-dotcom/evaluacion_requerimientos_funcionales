from flask import Flask, request, jsonify, send_from_directory
import ollama

app = Flask(__name__, static_folder="static")

PARAMETROS = {
    "condicion": {
        "nombre": "Condición",
        "type": "noul",
        "instructions": (
            "¿El requerimiento funcional incluye una situación "
            "que detona el evento que causa todo?"
        ),
        "criteria": {
            "true": "Especifica claramente el evento o situación detonante",
            "false": "No menciona qué acción dispara la acción"
        }
    },
    "condicion_1": {
        "nombre": "Sujeto",
        "type": "noul",
        "instructions": "¿El requerimiento funcional incluye un sujeto?",
        "criteria": {
            "true": "Especifica claramente el sujeto (el sistema) que lo realizará",
            "false": "No menciona al sujeto que realizará el requerimiento"
        }
    },
    "condicion_2": {
        "nombre": "Verbo normativo",
        "type": "noul",
        "instructions": "¿Se encuentra el verbo normativo 'debe' en el requerimiento?",
        "criteria": {
            "true": "Se encuentra claramente escrito el verbo debe",
            "false": "No menciona el verbo"
        }
    },
    "condicion_3": {
        "nombre": "Acción",
        "type": "noul",
        "instructions": "¿Se encuentra la acción que realizará el objeto o entidad?",
        "criteria": {
            "true": "Especifica claramente la acción que hará el objeto o entidad",
            "false": "No menciona la acción que realizará el objeto o entidad"
        }
    },
    "condicion_4": {
        "nombre": "Objeto o entidad",
        "type": "noul",
        "instructions": "¿Se encuentra el objeto o entidad que realizará la acción?",
        "criteria": {
            "true": "Especifica claramente el objeto o entidad que realizará la acción",
            "false": "No menciona el objeto o entidad"
        }
    },
    "condicion_5": {
        "nombre": "Criterio",
        "type": "noul",
        "instructions": (
            "¿Se menciona el criterio cuantitativo o restricción "
            "del requerimiento?"
        ),
        "criteria": {
            "true": "Especifica claramente el criterio que se tomará en cuenta para ese requerimiento",
            "false": "No menciona el criterio"
        }
    }
}


@app.route("/")
def inicio():
    return send_from_directory(".", "index.html")


@app.route("/evaluar", methods=["POST"])
def evaluar():
    try:
        datos = request.get_json(silent=True) or {}
        requerimiento = datos.get("requerimiento", "").strip()

        if not requerimiento:
            return jsonify({
                "error": "Escribe un requerimiento primero."
            }), 400

        print("Requerimiento recibido:", requerimiento)

        # Crear las preguntas para Ollama sin los nombres
        # descriptivos que solo se usan en la página.
        preguntas = {
            clave: {
                "type": parametro["type"],
                "instructions": parametro["instructions"],
                "criteria": parametro["criteria"]
            }
            for clave, parametro in PARAMETROS.items()
        }

        response = ollama.systemone(
            model="d1-omni:600m",
            state=requerimiento,
            questions=preguntas
        )

        resultados = []
        cumplidos = 0

        for clave, parametro in PARAMETROS.items():
            puntuacion = float(
                getattr(response.answers[clave], "noul")
            )

            cumple = puntuacion >= 0.05

            if cumple:
                cumplidos += 1

            resultados.append({
                "nombre": parametro["nombre"],
                "puntuacion": puntuacion,
                "cumple": cumple
            })

        return jsonify({
            "resultados": resultados,
            "cumplidos": cumplidos,
            "total": len(PARAMETROS)
        })

    except Exception as error:
        print("ERROR AL EVALUAR:", repr(error))

        return jsonify({
            "error": str(error)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
