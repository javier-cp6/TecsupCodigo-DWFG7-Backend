import express from 'express'
// import { PrismaConnector } from './prisma.js';
import cors from "cors";
import { departamentosRouter } from './routes/departamentos.routes.js'
import { trabajadoresRouter } from './routes/trabajadores.routes.js'

const app = express()
const PORT = process.env.PORT

// el método GET siempre podrá ser accedido ya que es utilizado por el navegador

// método 1: Configuring CORS
// declarar origin, methods y headers permitidos
// cors() puede recibir un json de opciones (método 1) o una función (método 2)
app.use(
  cors({
    origin: ["https://www.tecsup.edu.pe"],
    methods: ["GET", "POST"],
    allowedHeaders: ["accept", "authorization", "content-type"]
  })
)

// método 2: Configuring CORS w/ Dynamic Origin
// usa callback

// lista de orígnes permitidos, es decir dominios que  pueden consultar API
/*
const origenesPermitidos = ["http://miaplicacion.com"]; // lista blanca

app.use(
  cors((req, cb) => {
    const corsOptions = { origin: false};

    if (origenesPermitidos.indexOf(req.header("Origin") ?? "") !== -1) {
      corsOptions.origin = true
    }

    cb(null, corsOptions)
  })
)
*/


/*
app.get('/departamentos', async (req, res) => {
  try {
    // SELECT * FROM departamentos
    const resultado = await PrismaConnector.departamento.findMany();
    console.log(resultado);
    console.log('hola');
    return res.json({
      message: "Hola",
    })

  } catch (error) {
    return res.json({
      message: "Algo salió mal",
    })
  }
})
*/
app.use(express.json())

app.use(departamentosRouter)
app.use(trabajadoresRouter)

app.listen(PORT, ()=> {
  console.log(`Servidor corriendo exitosamente en puerto ${PORT}`)
})