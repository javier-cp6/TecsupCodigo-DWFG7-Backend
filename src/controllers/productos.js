import { ProductoModel } from "../models/productos.js";

export const crearProducto = async (req, res) => {
  try {
    const data = req.body;
  // TODO crear DTO
  const nuevoProducto = await ProductoModel.create(data);

  return res.status(201).json({
    message: "Producto creado exitosamente",
    result: nuevoProducto,
  });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el producto",
      result: error.message,
    })
  }
}