import _ from "lodash";
import jwt from "jsonwebtoken";

// middleware: ejecuta operaciones previas al controlador final
export const verificarToken = (req, res, next) => {
  if(_.isNil(req.headers.authorization)){
    // validar que se envíen los headers de authorization
    return res.status(401).json({
      message: "Se necesita un token para realizar esta petición"
    })
  }

  try {
    const token = req.headers.authorization.split(" ")[1] //"Bearer sassafsaf.sasafsf.safsaf"
    if(_.isNil(token)){
      throw new Error("Falta token")
    }
    const payload = jwt.verify(token, process.env.JWT_SECRET);
    console.log(payload)

    next()
  } catch (error) {
    return res.status(400).json({
      message: "Token inválida",
      content: error.message,
    })
  }
}
