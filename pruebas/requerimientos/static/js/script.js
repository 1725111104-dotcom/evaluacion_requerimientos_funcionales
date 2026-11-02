async function evaluacion() {
    const requerimiento = document
        .getElementById("requerimientos")
        .value.trim();

    const resultado = document.getElementById("resultado");
    const boton = document.getElementById("evaluacion");

    if (!requerimiento) {
        resultado.textContent = "Escribe un requerimiento primero.";
        return;
    }

    boton.disabled = true;
    resultado.textContent = "Evaluando...";

    try {
        const respuesta = await fetch("/evaluar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                requerimiento: requerimiento
            })
        });

        const datos = await respuesta.json();

        if (!respuesta.ok) {
            throw new Error(datos.error || "Error al evaluar.");
        }

        resultado.replaceChildren();

        const resumen = document.createElement("p");
        resumen.textContent =
            `Cumple ${datos.cumplidos} de ${datos.total} parámetros.`;

        resultado.appendChild(resumen);

        datos.resultados.forEach(item => {
            const linea = document.createElement("p");

            linea.textContent =
                item.nombre + ": " +
                (item.cumple ? "Cumple" : "No cumple");

            resultado.appendChild(linea);
        });

    } catch (error) {
        resultado.textContent =
            "Error: " + error.message;

    } finally {
        boton.disabled = false;
    }
}
