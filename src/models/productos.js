import mongoose from "mongoose";

const productoSchema = new mongoose.Schema({
  nombre: {
    type: mongoose.Schema.Types.String,
    required: true,
  },
  precio: {
    type: mongoose.Schema.Types.Decimal128,
    required: true,
    get: (valor) => +valor.toString(),
  },
  foto: {
    type: mongoose.Schema.Types.String,
  },
},
{
  // propiedad configurada por mongoose al crear cada documento y que contiene el valor interno de la revisión. el nombre por defecto es '__v' y puede ser modificado
  versionKey: false,
})

export const ProductoModel = mongoose.model("productos", productoSchema)

productoSchema.set("toJSON", { getters: true });