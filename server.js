// forma con ECMAscript
import express from 'express';

// forma con CommonJs
// const express = require("express") 
import dotenv from 'dotenv';

dotenv.config()

const servidor = express()
const PORT = process.env.PORT

servidor.use(express.json());

const categories = [
  {
    name: "Zapatos",
    description: "para hombres, damas y niños"
  }
];

// req y res son obligatorios
servidor.get("/", (req, res) => {
  res.status(200).json({
    message: "Bienvenido a primera API"
  })
})

servidor
  .route("/categories")
  .get((req, res) => {
  // servidor.get("/categories", (req, res) => {
    return res.status(200).json({categories})
  })

  .post((req, res) => {
  // servidor.post('/categories', (req, res) => {
    // console.log(req.body)
    const category = req.body;
    categories.push(category);

    return res.status(201).json({
      message: "Category created successfully",
      content: category,
    })
})

servidor.route("/categories/:id").get((req, res) => {
  console.log(req.params);
  // const id = req.params.id
  const {id}  = req.params

  if (categories[id] !== undefined) {
    return res.json({
      message: "La categoría es",
      content: categories[id]
    });
  }else {
    return res.status(400).json({
      message: "La categoría no existe",
      content: null,
    })
  }
})

servidor.listen(PORT, ()=>{
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`)
})