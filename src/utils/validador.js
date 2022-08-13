import _ from "lodash";
import jwt from "jsonwebtoken";
import { usuarioModel } from "../models/usuarios.js";

export const validatorToken = async(req, res, next) => {
  // validar que se envíen los headers de autorización
  if (_.isNil(req.headers.authorization)) {
    return res.status(401).json({
      message: "Se necesita un token para realizar esta petición",
      result: null,
    })
  }

  // en el header de autorización llega la siguiente info (token): Bearer xxx.xxx.xxx
  const token = req.headers.authorization.split(" ")[1]
  if(_.isNil(token)) {
    return res.status(401).json({
      message: "Formato de token inválido",
      result: null,
    })
  }
  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET)
    const usuario = await usuarioModel.findById(payload.id) // {id: 'asdasdasd'} 
    // se nombró como "id" del token en el controlador login

    // agregar al request la llave user con el usuario, a fin de que pueda ser utilizada en los controladores siguientes
    req.user = usuario 

    next()
  } catch (error) {
    return res.status(401).json({
      message: "Error al descifrar token",
      result: error.message,
    })
  }
}