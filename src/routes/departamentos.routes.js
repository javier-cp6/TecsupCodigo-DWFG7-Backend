import { Router } from "express";
import { 
  getDepartamentos, 
  postDepartamento, 
  updateDepartamento, 
  deleteDepartamento, 
  devolverDepartamento 
} from "../controllers/departamentos.controllers.js";

export const departamentosRouter = Router()

// departamentosRouter.get("/departamentos", getDepartamentos)
// departamentosRouter.post("/departamentos", postDepartamento)

departamentosRouter
  .route("/departamentos")
  .get(getDepartamentos)
  .post(postDepartamento)

departamentosRouter
  .route("/departamento/:id")
  .put(updateDepartamento)
  .delete(deleteDepartamento)
  .get(devolverDepartamento)
