import bcryptjs from "bcryptjs"
import { usuarioModel } from "../models/usuarios.js";
import { usuarioRequestDTO, loginRequestDTO } from "../dtos/usuarios.js";

export const crearUsuario = async (req, res) => {
  try {
    const data = usuarioRequestDTO(req.body);
    // método 2 para guardar registro: usando un constructor de clase. Permite realizar modificaciones antes de guardar

    // contruir objeto usuario con new
    const nuevoUsuario = new usuarioModel(data)
    
    // modificar objeto
    // nuevoUsuario.nombre = "blablabla"

    // guardar en db (se genera el _id). devuelve una promesa
    await nuevoUsuario.save() 

    const { password, ...resultado } = nuevoUsuario.toJSON();

    return res.status(201).json({
      message: "Usuario creado exitosamente",
      // result: nuevoUsuario,
      result: resultado,
    })
    
  } catch (error) {
    return res.status(400).json({
      message: error.message,
      result: null,
    })
  }
}

export const login = async (req, res) => {
  try {
    const data = loginRequestDTO(req.body);
    const usuarioEncontrado = await usuarioModel.findOne({ email: data.email })

    if (!usuarioEncontrado) {
      return res.status(200).json({
        message: "Usuario o contraseña inválidos",
        result: null,
      });
    } else {
      if (bcryptjs.compareSync(data.password, usuarioEncontrado.password))

      return res.status(200).json({
        message: "Usuario existe",
        result: null,
      });    }
  } catch (error) {
    return res.status(400).json({
      message: error.message,
      result: null,
    });
  }
}