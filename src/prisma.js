import prisma from "@prisma/client";

const { PrismaClient } = prisma

// crear instancia para conectar la DB desde express
export const PrismaConnector = new PrismaClient()