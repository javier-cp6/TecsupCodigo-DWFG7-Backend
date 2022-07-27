import { PrismaConnector } from "../prisma.js"
import { departamentoRequestDTO } from "../dtos/departamentos.dto.js"

export const getDepartamentos = async (req, res) => {
  try {
    const departamentos = await PrismaConnector.departamento.findMany()
    return res.json ({
      result: departamentos,
      message: null,
    })
  } catch (error) {
    console.log(error)
    return res.status(400).json({
      message: "Error al devolver los departamentos",
      result: error,
    })
    
  }
}

export const postDepartamento = async (req, res) => {
  console.log(req.body)
  try {
    const data = departamentoRequestDTO(req.body)
    const result = await PrismaConnector.departamento.create({ data })
    return res.status(201).json({
      message: 'Departamento creado exitosamente',
      result,
    })
  } catch (error) {
    return res.status(400).json({
      message: 'Error al crear departamento',
      result: error.message,
    })
  }
}

export const updateDepartamento = async (req, res) => {
  try {
    const {id} = req.params; // {id: 1}
    const data = departamentoRequestDTO(req.body); // { nombre: "qwert"}
    const result = await PrismaConnector.departamento.update({ data, where: { id: +id}}) //+id para convertir a entero

    return res.json({
      message: "Departamento actualizado exitosamente",
      result,
    })
  } catch (error) {
    return res.status(400).json({
      message: "Error al actualizar el departamento",
      result: error.message // toda instancia de errores será una instancia de la clase Error cuyos atributos son: message, name, stack
    })
  }
}

export const deleteDepartamento = async (req, res) => {
  try {
    const {id} = req.params
    const result = await PrismaConnector.departamento.delete({
      where: {id: +id},
    })
    return res.json({
      message: "Departamento eliminado exitosamente",
      result,
    })
  } catch (error) {
    return res.status(400).json({
      message: "Error al eliminar el departamento",
      result: error.message,
    })
  }
}

export const devolverDepartamento = async (req, res) => {
  try {
    const {id} = req.params
    const result = await PrismaConnector.departamento.findFirstOrThrow({
      where: {id: +id},
    })
    return res.json({
      message: null,
      result,
    })
  } catch (error) {
    return res.status(400).json({
      message: "Error al devolver el departamento",
      result: error.message,
    })
  }
}