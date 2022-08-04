import prisma  from "@prisma/client";
import _ from "lodash";
import jwt from "jsonwebtoken";
import { PrismaConnector } from "./prisma.js";

// middleware: ejecuta operaciones previas al controlador final
export const verificarToken = async (req, res, next) => {
  if(_.isNil(req.headers.authorization)){
    // validar que se envíen los headers de authorization
    return res.status(401).json({
      message: "Se necesita un token para realizar esta petición"
    })
  }

  try {
    const token = req.headers.authorization.split(" ")[1] //"Bearer sassafsaf.sasafsf.safsaf"
    if(_.isNil(token)){
      throw new Error("Falta token")
    }
    const payload = jwt.verify(token, process.env.JWT_SECRET);
    console.log(payload)
    const trabajador = await PrismaConnector.trabajador.findFirstOrThrow({
      where: {
        id: payload.id
      }
    })

    // crear nueva llave user
    req.user = trabajador

    next()
  } catch (error) {
    return res.status(400).json({
      message: "Token inválida",
      content: error.message,
    })
  }
}

export const isGerente = async (req, res, next) => {
  if(req.user.rol !== prisma.ROL_TRABAJADOR.GERENTE) {
    return res.status(403).json({
      message: "Usuario no cuenta con los permisos requeridos",
      result: null,
    })
  } else {
    next()
  }
}
