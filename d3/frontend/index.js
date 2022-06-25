const RUTA_BACK='http://127.0.0.1:5000'

fetch(RUTA_BACK + '/estado', { 
  method: 'GET'}).then((respuesta) => {
  return respuesta.json()
})
.then((data) => {
  console.log(data)
})
.catch((error) => {
  console.log(error)
})


fetch(RUTA_BACK + '/producto', {
  method: 'POST',
  body: JSON.stringify({
    nombre: 'Zanahoria',
    precio: 4.5,
  }),
  headers: {
    'Content-type': 'application/json'
  }
}).then((respuesta) => {
    return respuesta.json()
  })
  .then((data) => {
    console.log(data)
  })
  .catch((error) => {
    console.log(error)
  })

// TODO : hacer un button que cuando se haga click se mande a llamar el endpoint para devolver-productos

  fetch(RUTA_BACK + '/devolver-productos', { 
    method: 'GET'}).then((respuesta) => {
    return respuesta.json()
  })
  .then((data) => {
    console.log(data)
  })
  .catch((error) => {
    console.log(error)
  })
