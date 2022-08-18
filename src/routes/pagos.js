import { Router } from "express";
import { crearPago } from "../controllers/pagos.js";
import { validatorToken } from "../utils/validador.js";

export const pagosRouter = Router()

pagosRouter.post("/crear-pago", validatorToken, crearPago)