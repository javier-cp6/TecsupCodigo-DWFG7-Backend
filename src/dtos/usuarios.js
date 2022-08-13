import _ from "lodash";
import validator from "validator";

export const usuarioRequestDTO = (data) => {
  const errores = []
  if(_.isNil(data.email)){
    errores.push("Falta el email");
  }
  if(_.isNil(data.password)){
    errores.push("Falta el password");
  }
  if(!validator.isEmail(data.email)){
    errores.push("Email inválido");
  }
  if(_.isNil(data.nacionalidad)){
    errores.push("Falta la nacionalidada");
  }
  if(errores.length !== 0){
    throw new Error(errores);
  } else {
    return data;
  }
}

export const loginRequestDTO = (data) => {
  const errores = [];

  if (_.isNil(data.email)){
    errores.push("Falta el email");
  }
  if (_.isNil(data.password)){
    errores.push("Falta el password");
  }
  if (!validator.isEmail(data.email)){
    errores.push("Email inválido");
  }
  
  if (errores.length !== 0){
    throw new Error(errores);
  } else {
    return data
  }
}