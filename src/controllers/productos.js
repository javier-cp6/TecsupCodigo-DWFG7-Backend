import { productoModel } from "../models/productos.js"

export const crearProducto = async (req, res) => {
  try {
    const data = req.body;
    const nuevoProducto = await productoModel.create(data); 
    nuevoProducto.toJSON();// extrae la información de la nueva instancia creada y la convierte a un JSON para que pueda ser legile en el frontend

    return res.status(201).json({
      message: "Producto creado exitosamente",
      result: nuevoProducto.toJSON(),
  })
  } catch (error) {
    return res.status(400).json({
      message: "Error al cargar el producto",
      result: error.message,
    })
  }
} 

export const listarProductos = async (req, res) => {
  console.log(req.query);
  // devolver todos los productos
  // const productos = await productoModel.find(); 

  // devolver productos según condición
  // like %Monitor% > /Monitor/
  // like M% > /^M/
  // like %r > /r$/
  
  const { nombre, precioDesde, precioHasta } = req.query;
  let filtro = {};

  if (nombre) {
    // https://www.mongodb.com/docs/manual/reference/operator/query/regex/
    filtro = { ...filtro, nombre: { $regex: nombre }};
  }
  
  if (precioDesde && precioHasta) {
    filtro = {
      ...filtro,
      $and: [
        { precio: { $gte: precioDesde }},
        { precio: { $lte: precioHasta }},
      ],
    };
  } else {
    if (precioDesde){
      // gte > greater than or equal
      filtro = {...filtro, precio: { $gte: precioDesde}}
    }

    if (precioHasta){
      // lte > less than or equal
      filtro = {...filtro, precio: { $lte: precioHasta}}
    }
  }

  // const productos = await productoModel.find({ nombre: /Monitor/ }); 
  const productos = await productoModel.find(filtro); 
  
  
  
  return res.status(200).json({
    message: null,
    result: productos,
  })
}