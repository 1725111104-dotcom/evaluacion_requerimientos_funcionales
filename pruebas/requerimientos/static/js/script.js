async function evaluacion() {
    try{

        const uri = 'http://localhost:11434/v1/systemone';
        const requerimiento = 'El alumno al ingresar a su autoevaluación en el sistema de calificaciones debe asignarse una calificación, la cual será guardada en la base de datos en la tabla de calificaciones, la cual estará basada en una escala del 100% del porcentaje, el cual se repartirá en sus hard skills.';

        const data = {
            model : 'd1-omni:600m',
            state : requerimiento,
            questions : {
            'condicion': {
                'type' : 'noul',
                'instructions' : '¿El requerimiento funcional incluye una situación que detona el evento?',
                'criteria' : {
                    'true' : 'Especifica claramente el evento o situación detonante',
                    'false' : 'No menciona qué acción dispara la acción'
                    }
                }
            }
        }

        const response = await fetch(
            uri, 
            {
                method:'POST',
                headers: {
                    'Content-Type' : 'application/json'
                },
                body: JSON.stringify(data)
            }
        );

        const resultado = await response.json();

        console.log('Conexión con la API exitosa', resultado);
        console.log('Criterio: ', resultado.answers.criterio.noul);

    } catch (error){
        console.log('Ups, algo falló', error.message);
    }
    
}