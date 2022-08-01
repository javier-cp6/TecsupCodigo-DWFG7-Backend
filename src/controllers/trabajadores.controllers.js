import cryptoJs from "crypto-js"
import bcryptjs from "bcryptjs"
import { PrismaConnector} from "../prisma.js"
import { cambiarPasswordRequestDTO, trabajadoresRequestDTO } from "../dtos/trabajadores.dto.js";
import { validarCorreo, notificarNuevoPassword } from "../utils/correos.js";

export const postTrabajador = async (req, res) => {
 try {
    // const data = trabajadoresRequestDTO(req.body);
    const {password, ...data} = trabajadoresRequestDTO(req.body);
    const password_encriptada = bcryptjs.hashSync(password, 10)
    console.log(password_encriptada)
    const result = await PrismaConnector.trabajador.create({ data: { ...data, password: password_encriptada} }) 

    const horaActual = new Date()

    const token = cryptoJs.AES.encrypt(
      JSON.stringify({
        id: result.id,
        caducidad: new Date(
          horaActual.getFullYear(), 
          horaActual.getMonth(), 
          horaActual.getDate(), 
          horaActual.getHours() + 2 
        ),
      }), 
      process.env.LLAVE_ENCRIPTACION
    ).toString()

    await validarCorreo({
      destinatario: result.email, 
      nombre: result.nombre,
      token,
    })

  return res.json({
    message: "Usuario registrado exitosamente",
    result,
  })
 } catch (error) {
  return res.status(400).json({
    message: "Error al crear el usuario",
    result: error.message
  })
 } 
}

export const validarTrabajador = async (req, res) => {
  const {token} = req.body

  try {
    const data = cryptoJs.AES.decrypt(
      token, 
      process.env.LLAVE_ENCRIPTACION
      ).toString(cryptoJs.enc.Utf8);
    console.log(data)

    // desencriptación: si token es inválida, retorna null. se fuerza el error con el siguiente if
    if(!data) {
      throw new Error("Token inválida")
    }

    const infoToken = JSON.parse(data);
    console.log(infoToken)
    if(infoToken.caducidad < new Date())
      throw new Error("Token vencida")

    // buscar trabajador
    const trabajador = await PrismaConnector.trabajador.findUniqueOrThrow({
      where: { id: infoToken.id},
    })

    // verificar que no esté validado
    if(trabajador.validado) {
      throw new Error("Usuario ya fue validado")
    }

    // validar
    await PrismaConnector.trabajador.update({
      data: {validado: true},
      where: { id: infoToken.id}
    })

    return res.json({
      message: "Trabajador validado exitosamente",
      result: null,
    })
  } catch (error) {
    return res.status(400).json({
      message: "Error al validar token",
      result: error.message
    })
    
  }
 }
export const cambiarPassword = async (req, res) => {

  try {
    const data = cambiarPasswordRequestDTO(req.body);
    const trabajador = await PrismaConnector.trabajador.findUniqueOrThrow({
      where: {email: data.email}
    })
    // TODO: la nueva contraseña no puede ser igual a la anterior
    if (bcryptjs.compareSync(data.oldPassword, trabajador.password) && bcryptjs.compareSync(data.newPassword, trabajador.password)) {
      throw new Error("Nueva contraseña debe ser distinta a la anterior")
    }

    if (bcryptjs.compareSync(data.oldPassword, trabajador.password)) {
      const newPassword = bcryptjs.hashSync(data.newPassword)

      await PrismaConnector.trabajador.update({
        data: {
          password: newPassword,
        },
        where: {
          email: data.email
        }, 
      })

      await notificarNuevoPassword({
        destinatario: trabajador.email,
        nombre: trabajador.nombre,
      })
      return res.json({
        message: "Contraseña actualizada correctamente",
        result: null,
      })
    } else {
      throw new Error("La contraseña es incorrecta")
    }
  } catch (error) {
    return res.json({
      message: "Error al actualizar el password",
      result: error.message
    })
  }
}