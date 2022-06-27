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

// TODO : agregar un button que al hacer click llame el endpoint para devolver-productos

// service
const getProducts = () => {
  return fetch(RUTA_BACK + '/devolver-productos', { 
    method: 'GET'}).then((respuesta) => {
    return respuesta.json()
  })
  .then((data) => {
    console.log(data)
    return data.content
  })
  .catch((error) => {
    console.log(error)
  })
}

// interface
const drawProducts = (products) => {
  const productTable = document.getElementById('productTable')

  let htmlProducts = ''
  
  products.forEach(({nombre, precio}) => {
    let product = `
        <tr>
          <td>${nombre}</td>
          <td>${precio}</td>
        </tr>
    `
    htmlProducts += product
  });
  productTable.innerHTML = htmlProducts
}

// btn event
const btnGetProducts = document.getElementById('btnGetProducts')

btnGetProducts.addEventListener('click', async() => {
  try {
    const productsData = await getProducts()
    console.log(productsData)
    drawProducts(productsData)
  } catch (error) {
    throw error
  }
})   




  
