import express from "express";
import mongoose from "mongoose";
import { productoRouter } from "./routes/productos.js";

const app = express();

app.use(express.json());

app.use(productoRouter)

const { PORT } = process.env ?? 3000;

mongoose
  .connect(process.env.MONGO_URL)
  .then(()=>{
    console.log("Base de datos conectada exitosamente 🌱")
    app.listen(PORT, () => {
      console.log(`Server corriendo exitosamente en el puerto ${PORT} 💻`)
    })
  })
  .catch(()=>{
    console.log("Error al conectarse a la base de datos 💀")
  })


