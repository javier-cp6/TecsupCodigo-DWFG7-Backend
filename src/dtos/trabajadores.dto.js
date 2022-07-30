import prisma from '@prisma/client';
import _ from 'lodash'
import validator from 'validator'

export const trabajadoresRequestDTO = (data) => {
  const errores = []

  if (_.isNil(data.nombre)){
    errores.push("Falta el nombre")
  }
  if (_.isNil(data.apellido)){
    errores.push("Falta el apellido")
  }
  if (_.isNil(data.email)){
    errores.push("Falta el email")
  }
  if (!_.isNil(data.email) && !validator.isEmail(data.email)){
    errores.push("Email inválido")
  }
  if (_.isNil(data.password)){
    errores.push("Falta el password")
  }
  if (_.isNil(data.rol)) {
    errores.push("Falta el rol");
  }

  // opción 1
  /*
  if (!_.isNil(data.rol) && data.rol !== ROL_TRABAJADOR.GERENTE ||
  data.rol !== ROL_TRABAJADOR.OBRERO ||
  data.rol !== ROL_TRABAJADOR.PRACTICANTE ||
  data.rol !== ROL_TRABAJADOR.SUPERVISOR ||
  ){
    errores.push("Rol incorrecto, los valores admitidos son 'GERENTE', 'OBRERO', 'PRACTICANTE, 'SUPERVISOR'")
  }
  */
  // opción 2
  if (!_.isNil(data.rol)) { 
    const roles = Object.values(prisma.ROL_TRABAJADOR);
    // const roles2 = [ 
    //   prisma.ROL_TRABAJADOR.GERENTE, 
    //   prisma.ROL_TRABAJADOR.OBRERO, 
    //   prisma.ROL_TRABAJADOR.PRACTICANTE, 
    //   prisma.ROL_TRABAJADOR.SUPERVISOR, 
    // ]; 
    const filtro = roles.filter((rol) => rol === data.rol); if (filtro.length === 0) { 
      let mensaje = "Rol incorrecto, los valores admitidos son: ";
      roles.forEach((rol) => {
        mensaje += `'${rol}'`;
      });
      errores.push(mensaje)
    } 
  }
  if (errores.length !== 0) {
    throw new Error(errores);
  } else {
    return data
  }
}

export const cambiarPasswordRequestDTO = (data) => {
  // validar que se reciba {email: "...", oldPassword: "...", newPassword: "..."}
  // validar correo
  const errores = []
  if (_.isNil(data.email)) {
    errores.push("Falta el email")
  } 
  if (_.isNil(data.oldPassword)) {
    errores.push("Falta el oldPassword")
  } 
  if (_.isNil(data.newPassword)) {
    errores.push("Falta el newPassword")
  } 
  if (_.isNil(data.email) && !validator.isEmail(data.email)) {
    errores.push("Email inválido")
  } 
  if (errores.length !== 0) {
    throw new Error(errores)
  } else {
    return data
  }
}