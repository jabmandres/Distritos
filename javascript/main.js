import { tabla } from "./tabla.js"

const formulario = document.getElementById('form')

const getData = (event) => {
    //Evita que se actualice la pagina
    event.preventDefault()
    //Tomo la data del formulario
    const { caudal, tempEntrada, tempSalida, servicio, chillerCentrifugo, cantChillerCentrifugo, chillerAbsorcion, cantChillerAbsorcion } = event.target
    
    // Calculo chiller por cantidad
    const potenciaChillerCentrifugo = Number(chillerCentrifugo.value * cantChillerCentrifugo.value)
    const potenciaChillerAbsorcion = Number(chillerAbsorcion.value * cantChillerAbsorcion.value)
    
    // sumo ambos resultados
    const totalChiller = potenciaChillerCentrifugo + potenciaChillerAbsorcion

    //Tamaño del DT
    const tamanioDT = Number(caudal.value * (tempEntrada.value - tempSalida.value) * servicio.value * 1000 * 0.0003069)
    
    // Validacion tamaño maximo (por hacer)
    const tMax = tamanioDT + (tamanioDT * 0.5)

    // Envio los totales a la tabla
    tabla(potenciaChillerCentrifugo, potenciaChillerAbsorcion)

}

// Capturo el evento submit del formulario al hacer click en el boton y ejecuto la funcion getData
formulario.addEventListener('submit', getData)