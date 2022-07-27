import express from 'express'
// import { PrismaConnector } from './prisma.js';
import { departamentosRouter } from './routes/departamentos.routes.js'

const app = express()
const PORT = process.env.PORT
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

app.listen(PORT, ()=> {
  console.log(`Servidor corriendo exitosamente en puerto ${PORT}`)
})