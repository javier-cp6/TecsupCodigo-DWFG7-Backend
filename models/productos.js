import mongoose from "mongoose";

// Las configuraciones de una colección que se declaren solamente servirán para mongoose (dado que es una db no relacional), por lo tanto, es recomendable no manipular directamente la DB

const detalleProductoSchema = new mongoose.Schema({
  tallas: [mongoose.Schema.Types.String],
  unidadMedida: {
    alias: 'unidad_medida',
    type: mongoose.Schema.Types.String,
    enum: ["litros", "kilos", "N/A", "onzas"],
    default: "N/A",
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
    alias: "precio_venta",
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