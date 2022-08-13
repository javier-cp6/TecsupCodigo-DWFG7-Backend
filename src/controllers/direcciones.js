import { usuarioModel } from "../models/usuarios.js";
import { direccionRequestDTO } from "../dtos/direcciones.js";

export const crearDireccion = async (req, res) => {
  try {
    console.log(req.user);
    const data = direccionRequestDTO(req.body);
    req.user.direcciones.push(data);
    // guardar los cambios realizados de una instancia de cualquier coleción de la DB
    await req.user.save()
    return res.status(201).json({
      message: "Dirección agregada exitosamente",
      result: req.user.direcciones,
    })
  } catch (error) {
    return res.status(400).json({
      message: error.message,
      result:null,
    })
  }
}

export const listarDirecciones = async (req, res) => {
  return res.json({
    message: null,
    result: req.user.direcciones,
  });
}