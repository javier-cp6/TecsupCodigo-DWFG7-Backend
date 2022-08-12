import express from "express";
import mongoose from "mongoose";
// import { productoModel } from "./models/productos.js"
import { productoRouter } from "./routes/productos.js";

const app = express();

// middleware global
app.use(express.json()); // indica que la aplicación de express puede entender y convertir la info que llega del frontend en formato JSON

const port = process.env.PORT ?? 3000;

// se puede decir que es la declaración de otro middleware
app.use(productoRouter)

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

