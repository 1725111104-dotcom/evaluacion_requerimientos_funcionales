import ollama

requerimiento = "El alumno al ingresar a su autoevaluación en el sistema de calificaciones debe asignarse una calificación, la cual será guardada en la base de datos en la tabla de calificaciones, la cual estará basada en una escala del 100% del porcentaje, el cual se repartirá en sus hard skills.."

response = ollama.systemone(
    model = "d1-omni:600m",
    state = requerimiento,
    questions = {
        'condicion': {
            'type' : 'noul',
            'instructions' : '¿El requerimiento funcional incluye una situación que detona el evento?',
            'criteria' : {
                'true' : 'Especifica claramente el evento o situación detonante',
                'false' : 'No menciona qué acción dispara la acción'
                },
        'condicion': {
            'type' : 'noul',
            'instructions' : '¿El requerimiento funcional incluye un sujeto?'
            'criteria' : {
                'true' : 'Especifica claramente el sujeto (el sistema) que lo realizará'
                'false' : 'No menciona al sujeto que realizará el requerimiento'
            },
        },
    },
)

condicion = response.answers['condicion'].noul

if condicion >= 0.05:
    print(f"1. Cumple con la condición: {condicion}")
else:
    print(f"2. No cumple con la condición {condicion}")