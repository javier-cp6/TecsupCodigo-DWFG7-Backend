import { Router } from "express";
import { 
  crearCarrito,
  listarCarrito,
} from "../controllers/carritos.js";
import { validatorToken } from "../utils/validador.js";

export const carritoRouter = Router ()

carritoRouter.route('/carrito')
  .all(validatorToken)
  .post(crearCarrito)
  .get(listarCarrito)
  // .put(crearCarrito)
  // .delete(crearCarrito)