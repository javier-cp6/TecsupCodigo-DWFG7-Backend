import express from "express";
import mongoose from "mongoose";
import mercadopago from "mercadopago";
// import { productoModel } from "./models/productos.js"
import { productoRouter } from "./routes/productos.js";
import { usuarioRouter } from "./routes/usuarios.js";
import { direccionRouter } from "./routes/direcciones.js"; 
import { carritoRouter } from "./routes/carritos.js";
import { pagosRouter } from "./routes/pagos.js";

// access_token: token que indica a qué negocio pertenece la pasarela de pagos
// integrator_id: identificador del desarrollador que realizó la integración
mercadopago.configure({
  access_token: process.env.MP_ACCESS_TOKEN,
  integrator_id: process.env.MP_INTEGRATOR_ID //opcional
})

const app = express();

// middleware global
app.use(express.json()); // indica que la aplicación de express puede entender y convertir la info que llega del frontend en formato JSON
// app.use(express.urlencoded())

const port = process.env.PORT ?? 3000;

// middleware que agrega ruta a la app
app.use(productoRouter)
app.use(usuarioRouter)
app.use(direccionRouter)
app.use(carritoRouter)
app.use(pagosRouter)

mongoose
  .connect(process.env.MONGO_URL, { 
    serverSelectionTimeoutMS: 3000, 
  })
  .then((value) => {
    console.log('Base de datos conectada correctamente');
    app.listen(port, () => {
      console.log(`Servidor corriendo en el puerto ${port}`);
    });
  }) 
  .catch((error) => {
    console.error("Error al conectarse a la base de datos")
  })

