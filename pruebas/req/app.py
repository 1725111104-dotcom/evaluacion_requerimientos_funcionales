import ollama

requerimiento = (
    "El alumno ingresa a su autoevaluación en el sistema de calificaciones, al ingresar "
    "debe asignarse una calificación, la cual será guardada en la base de datos "
    "en la tabla de calificaciones, la cual estará basada en una escala del 100% "
    "del porcentaje, el cual se repartirá en sus hard skills."
)

response = ollama.systemone(
    model="d1-omni:600m",
    state=requerimiento,
    questions={
        "condicion": {
            "type": "noul",
            "instructions": "¿El requerimiento funcional incluye una situación que detona el evento que causa todo?",
            "criteria": {
                "true": "Especifica claramente el evento o situación detonante",
                "false": "No menciona qué acción dispara la acción",
            },
        },
        "condicion_1": {
            "type": "noul",
            "instructions": "¿El requerimiento funcional incluye un sujeto?",
            "criteria": {
                "true": "Especifica claramente el sujeto (el sistema) que lo realizará",
                "false": "No menciona al sujeto que realizará el requerimiento",
            },        
        },
        "condicion_2": {
            "type": "noul",
            "instructions": "¿Se encuentra el verbo normativo <debe> en el reuqerimiento?",
            "criteria": {
                "true": "Se encuentra claramente esscrito el verbo debe",
                "false": "No menciona el verbo",
            },        
        }, 
        "condicion_3": {
            "type": "noul",
            "instructions": "¿Se encuentra la acción que realizará el objeto o entidad?",
            "criteria": {
                "true": "Especifica claramente la acción que hará el objeto o entidad",
                "false": "No menciona la acción que realizará el objeto o entidad",
            },        
        }, 
        "condicion_4": {
            "type": "noul",
            "instructions": "¿Se encuentra el objeto o entidad que realizará la acción?",
            "criteria": {
                "true": "Especifica claramente el objeto o entidad que realizará la acción",
                "false": "No menciona el objeto o entidad",
            },        
        }, 
        "condicion_5": {
            "type": "noul",
            "instructions": "¿Se menciona el criterio (Cuantitativo/Restricción) de dicho requerimiento?",
            "criteria": {
                "true": "Especifica claramente el criterio que se tomará en cuenta para ese requerimiento",
                "false": "No menciona el criterio",
            },        
        }, 
    },
)

condicion = response.answers["condicion"].noul
condicion_1 = response.answers["condicion_1"].noul
condicion_2 = response.answers["condicion_2"].noul
condicion_3 = response.answers["condicion_3"].noul
condicion_4 = response.answers["condicion_4"].noul
condicion_5 = response.answers["condicion_5"].noul

if condicion >= 0.05:
    print(f"1. Cumple con la condición: {condicion}")
else:
    print(f"2. No cumple con la condición {condicion}")

if condicion_1 >= 0.05:
    print(f"1. Cumple con la condición: {condicion_1}")
else:
    print(f"2. No cumple con la condición {condicion_1}")

if condicion_2 >= 0.05:
    print(f"1. Cumple con la condición: {condicion_2}")
else:
    print(f"2. No cumple con la condición {condicion_2}")

if condicion_3 >= 0.05:
    print(f"1. Cumple con la condición: {condicion_3}")
else:
    print(f"2. No cumple con la condición {condicion_3}")

if condicion_4 >= 0.05:
    print(f"1. Cumple con la condición: {condicion_4}")
else:
    print(f"2. No cumple con la condición {condicion_4}")

if condicion_5 >= 0.05:
    print(f"1. Cumple con la condición: {condicion_5}")
else:
    print(f"2. No cumple con la condición {condicion_5}")
