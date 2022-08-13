import mongoose from "mongoose";
import bcryptjs from "bcryptjs" 

const nacionalidad = ["PERUANO", "VENEZOLANO", "BOLIVIANO"]

const direccionSchema = new mongoose.Schema(
  {
    calle: {
      required: true,
      type: mongoose.Schema.Types.String,
    },
    numero: {
      required: true,
      type: mongoose.Schema.Types.String,
    },
    referencia: {
      required: true,
      type: mongoose.Schema.Types.String,
    },
    adicional: {
      required: true,
      type: mongoose.Schema.Types.String,
    },
  },
  // Mongoose options
  {
    _id: false,
    timestamps: {
      // permite utilizar en el schema los campos de timestamp de manera automática, por ejemplo, fecha de creación y actualización 
      createdAt: "fecha_creacion",
      updatedAt: false
    }
  }
)

const usuarioSchema = new mongoose.Schema({
  email: {
    type: mongoose.Schema.Types.String,
    required: true,
    index: true, // debe aplicarse cuando la colección no tiene data
    unique: true, // solamente funciona con las columnas que son índices
  },
  password: {
    type: mongoose.Schema.Types.String,
    required: true,
    set: (valor) => bcryptjs.hashSync(valor, 10),
    // select: false,
  },
  nombre: {
    type: mongoose.Schema.Types.String,
    required: true,
  },
  apellido: {
    type: mongoose.Schema.Types.String,
    required: true,
  },
  nacionalidad: {
    type: mongoose.Schema.Types.String,
    enum: nacionalidad,
    default: "PERUANO",
  },
  fechaNacimiento: {
    // name cambia el nombre de la columna en la DB
    name: "fecha_nacimiento", 
    type: mongoose.Schema.Types.Date,
  },
  // relación 1:n un usuario puede tener varias direcciones
  direcciones: {
    type: [direccionSchema],
  }
})



export const usuarioModel = mongoose.model('usuarios', usuarioSchema);
