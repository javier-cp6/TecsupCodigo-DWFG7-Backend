import { Router } from "express";
import { 
  postTrabajador,
  validarTrabajador,
  cambiarPassword,
  login,
  perfil
 } from "../controllers/trabajadores.controllers.js";

import { 
  verificarToken,
  isGerente,
  isAdmin,
 } from "../validador.js";

export const trabajadoresRouter = Router ()

trabajadoresRouter.post("/registro", verificarToken, isGerente, postTrabajador)
trabajadoresRouter.post("/validar-trabajador", validarTrabajador)
trabajadoresRouter.post("/cambiar-password", cambiarPassword)
trabajadoresRouter.post("/login", login)
trabajadoresRouter.get("/me", verificarToken, perfil )

trabajadoresRouter.post("/registro-admin", isAdmin, postTrabajador)
