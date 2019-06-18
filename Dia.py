import numpy as np
import pandas as pd
from datetime import datetime, date, time, timedelta

import Aula
Aula=Aula.Aula

class Dia:
    def __init__(self, nombre, franja):
        self.nombre=nombre
        self.aulas=[]
        self.crearAulas(franja)

    def crearAulas(self, franja):
        excelAula=pd.read_excel("E:\Desktop\Proyecto Integrador\Proyecto-Integrador\Tablas.xlsx", "Aula")
        for x in excelAula.CodigoAula:
            self.aulas.append(Aula(excelAula.CodigoAula[x], excelAula.Piso[x], excelAula.Capacidad[x], excelAula.Descripcion[x], franja))
    