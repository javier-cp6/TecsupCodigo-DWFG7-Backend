import mongoose from "mongoose";

// Las configuraciones de una colección que se declaren solamente servirán para mongoose (dado que es una db no relacional), por lo tanto, es recomendable no manipular directamente la DB
const unidadMedidaValores = ["litros", "kilos", "N/A", "onzas"]

const detalleProductoSchema = new mongoose.Schema({
  tallas: [mongoose.Schema.Types.String],
  unidadMedida: {
    alias: 'unidad_medida',
    type: mongoose.Schema.Types.String,
    enum: unidadMedidaValores, // solamente sirve para crear una instancia más no al actualizar o modificar
    default: "N/A",
    set: (valor) => {
      console.log(valor)
      if (unidadMedidaValores.includes(valor)) {
        return valor
      } else {
        throw new Error();
      }
    }
  },
})

const productoSchema = new mongoose.Schema({
  nombre: {
    type: mongoose.Schema.Types.String, //parámetro obligatorio
    required: true,
  },
  precio: {
    type: mongoose.Schema.Types.Decimal128,
    required: true,
    min: 0.0,
    // alias: "precio_venta",
    get: (valor) => {
      console.log(valor);
      return +valor.toString()
    }
  },
  cantidad : {
    type: mongoose.Schema.Types.Number,
    required: true,
    min: 0,
  },
  descripcion: mongoose.Schema.Types.String,
  foto: mongoose.Schema.Types.String,

  // relación 1:1 en una DB no relacional. El objeto detalleProductoSchema pertenece a un determimnado producto (productoSchema)
  detalleProducto: {
    type: detalleProductoSchema,
  },
});

// genera la relación de la colección con la DB, de acuedo al schema previemente definido
export const productoModel = mongoose.model('productos', productoSchema);

// setear (modificar) el comportamiento del método .toJSON: convierte la información de la llave precio y elimina la llave __v
productoSchema.set("toJSON", {
  getters: true,
  // transform: (doc, prod) => {
  //   if (prod.precio) {
  //     prod.precio = +prod.precio.toString();
  //   }
  //   delete prod.__v;
  //   return prod;
  // }
})