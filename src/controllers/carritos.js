import { carritoModel } from "../models/carritos.js";
import { carritoRequestDTO } from "../dtos/carritos.js";

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

    return res.status(201).json({
      message:  null,
      content: carrito,
    })
    
  } catch (error) {
    return res.status(400).json({
      message: error.message,
      result: null,
    })
  }
}