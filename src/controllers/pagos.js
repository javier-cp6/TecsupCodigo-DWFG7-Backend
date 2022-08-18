import axios from "axios";
import mercadopago from "mercadopago";
import { carritoModel } from "../models/carritos.js";

export const crearPago = async (req, res) => {
  const { user } = req
  const carrito = await carritoModel.findOne({ usuarioId: user._id})
  console.log(carrito)

  return res.json({
    message: "el link es",
    result: null
  })
}