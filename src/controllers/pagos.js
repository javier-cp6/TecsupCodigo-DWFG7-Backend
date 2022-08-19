import axios from "axios";
import mercadopago from "mercadopago";
import { carritoModel } from "../models/carritos.js";
import {productoModel} from '../models/productos.js'

export const crearPago = async (req, res) => {
  const { user } = req
  const carrito = await carritoModel.findOne({ usuarioId: user._id})

  const items = await Promise.all(
    carrito.detalle.map(async(detalle)=> {
      const producto = await productoModel.findById(detalle.productoId)
      return {
        id: producto._id,
        title: producto.nombre,
        picture_url: producto.foto,
        quantity: detalle.cantidad,
        currency_id: "PEN",
        unit_price: +producto.precio.toString(),
      }
    })
  )

  const preferencia = await mercadopago.preferences.create({
    auto_return: "approved", // rediccionará automáticamente cuando el pago sea aprobado
    back_urls: {
      // url a redireccionar de acuerdo a status del pago (success, failure, pending)
      success: "http://www.google.com", 
      failure: "http://www.tecsup.edu.pe",
      pending: "http://www.bbc.com"
    },
    payer: {
      name: user.nombre,
      surname: user.apellido,
      // user.email: usar correo y token para pruebas (certificación). Importante: Solamente usar un correo de usuario junto a una token real que no sea la de certificación 
      email: "test_user_63274575@testuser.com", 
      address: {
        // opcional
        street_name: user.direcciones[0]?.calle,
        street_number: +user.direcciones[0]?.numero,
        zip_code: "04002",
      },
    }, 
    // información de la persona que va a pagar
    items,
    // items: [
    //   {
    //     id: "",
    //     title: "",
    //     picture_url: "",
    //     quantity: "",
    //     currency_id: "PEN",
    //     unit_price: "",
    //   }
    // ],

    // url a la cual MP enviará la información de la preferencia en tiempo real. MP la conoce como IPN (Instant Payment Notification)
    // notification_url: 'localhost:3000/mercado-pago-notificaciones'
    notification_url: 'https://fa62-2001-1388-13a7-3fc2-488-ae8d-52d5-a119.sa.ngrok.io/mercado-pago-notificaciones'
  })
  console.log(carrito)
  console.log(preferencia)

  /*
  // limpieza de carrito: una vez creada la preferencia, limpiar los items del carrito
  carrito.detalle = []
  await carrito.save()

  // método básico
  let total = 0
  items.forEach((item)=> {
    total += item.quantity * item.unit_price
  })

  // método reduce
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce
  total = items.reduce((prevVal, curVal) => {
    return prevVal + curVal.quantity * curVal.unit_price;
  }, 0);

  // creación de pedido
  await pedidoModel.create({
    fecha: preferencia.body.date_created,
    total,
    estado: 'CREADO',
    preferenceId: preferencia.body.id,
    usuarioId: user._id,
  })
  */

  return res.json({
    message: "el link es",
    result: preferencia,
  })
}

export const notificacionesMercadoPago = async (req, res) => {
  console.log("el body es:");
  console.log(req.body);
  console.log("los parametros son:");
  console.log(req.params);
  console.log("los query params son:");
  console.log(req.query);

  return res.status(200).send();
};