import { Router } from "express";
import { crearPago, notificacionesMercadoPago } from "../controllers/pagos.js";
import { validatorToken } from "../utils/validador.js";

export const pagosRouter = Router()

pagosRouter.post("/crear-pago", validatorToken, crearPago)
pagosRouter.post("/mercado-pago-notificaciones", notificacionesMercadoPago)