async function evaluacion() { 
    try { 

        const uri = "https://noxious-spooky-fishsticks-r7rgrjq56q443ppqv-11434.app.github.dev/v1/systemone"; 
        const requerimiento = "El alumno al ingresar a su autoevaluación en el sistema de calificaciones."; 
        const data = { 
            model: "d1-omni:600m", 
            state: requerimiento, 
            questions: { 
                condicion: { 
                    type: "noul", 
                    instructions: "¿El requerimiento funcional incluye una situación que detona el evento?", 
                    criterio: { 
                        true: "Especifica claramente el evento o situación detonante", 
                        false: "No menciona qué acción dispara la acción" 
                    } 
                } 
            } 
        }; 

        const response = await fetch(uri, { 
            method: "POST", 
            headers: { 
                "Content-Type": "application/json" 
            }, 
            body: JSON.stringify(data) 
        }
    ); 

        const resultado = await response.json(); 
        
        console.log("Conexión con la API exitosa", resultado); 
        console.log("Criterio:", resultado.answers.criterio.noul); 

    } catch (error) { 
        console.log("Ups, algo falló", error.message); 
        throw error; 
    } 
}
