import { Router } from "express";
import { crearDireccion, listarDirecciones } from "../controllers/direcciones.js";
import { validatorToken } from "../utils/validador.js";

export const direccionRouter = Router()

direccionRouter
  .route("/direccion")
  .post(validatorToken, crearDireccion)
  .get(validatorToken, listarDirecciones)
  
  // TODO editar y eliiminar direccion
  // Dado que se require el id de la dirección, es necesario modificar direccionSchema para volver a generar el _id