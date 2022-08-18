import { carritoModel } from "../models/carritos.js";
import { carritoRequestDTO } from "../dtos/carritos.js";
import { productoModel } from "../models/productos.js";

export const crearCarrito = async (req, res) => {
  try {
    const usuario = req.user; // objeto del usuario logueado
    const data = carritoRequestDTO(req.body);

    // buscar si existe el carrito del usuario
    const carrito = await carritoModel.findOne(
      { usuarioId: usuario._id },
      // opcionalmente se puede indicar las columnas a extraer
      { usuarioId: true, detalle: true, _id: true }
    );

    if(carrito) {
      // agregar el nuevo producto al detalle
      carrito.detalle.push(data);
      await carrito.save();

      return res.status(201).json({
        message: "Artículo agregado exitosamente",
        content: carrito,
      })
    } else {
      const nuevoCarrito = await carritoModel.create({
        usuarioId: usuario._id,
        detalle: [data],
      })
      return res.status(201).json({
        message: "Artículo agregado exitosamente",
        content: nuevoCarrito,
      })
    }
  } catch (error) {
    return res.status(400).json({
      message: error.message,
      result: null,
    })
  }
}

export const listarCarrito = async (req, res) => {
  try {
    const { user } = req; 
    const carrito = await carritoModel.findOne(
      { usuarioId: user._id },
    );

    const detalle = await Promise.all(carrito.detalle.map(async (item) => {
      const productoEncontrado = await productoModel.findById(
        item.productoId, 
        {nombre: true, precio: true, foto: true}
      )
      return {
        productoId: item.productoId,
        nombre: productoEncontrado.nombre,
        precio: productoEncontrado.precio,
        foto: productoEncontrado.foto,
        cantidad: item.cantidad,
      }
    })
    )
    // console.log(carrito)
    // console.log(detalle)

    return res.json({
      message:  null,
      // content: carrito,
      // content: {...carrito},
      result: {...carrito.toJSON(), detalle}, // reeplazar con nuevo "detalle" que contiene info de los productos
    })
    
  } catch (error) {
    return res.status(400).json({
      message: error.message,
      result: null,
    })
  }
}