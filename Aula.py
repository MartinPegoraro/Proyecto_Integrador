import numpy as np
import pandas as pd
from datetime import datetime, date, time, timedelta

import Hora
Hora=Hora.Hora

class Aula:
    def __init__(self, codigo, piso, capacidad, descripcion, franja):
        self.codigo=codigo
        self.piso=piso
        self.capacidad=capacidad
        self.descripcion=descripcion
        self.horas=[]
        self.crearHoras(franja)
        self.aceptaTresModulos=True
        self.aceptaDosModulos=True

    def disponibilidad(self):
        if self.horas[0].asignado==False:
            return time(7, 30)
        elif self.horas[4].asignado==False:
            return time(9, 30)
        else:
            return time(10, 30)

    def crearHoras(self, franja):
        if franja=="Mañana":
            self.horas.append(Hora(time(7, 30)))
            self.horas.append(Hora(time(8)))
            self.horas.append(Hora(time(8, 30)))
            self.horas.append(Hora(time(9)))
            self.horas.append(Hora(time(9, 30)))
            self.horas.append(Hora(time(10)))
            self.horas.append(Hora(time(10, 30)))
            self.horas.append(Hora(time(11)))
            self.horas.append(Hora(time(11, 30)))
            self.horas.append(Hora(time(12)))
        elif franja=="Tarde":
            self.horas.append(Hora(time(12, 30)))
            self.horas.append(Hora(time(13)))
            self.horas.append(Hora(time(13, 30)))
            self.horas.append(Hora(time(14)))
            self.horas.append(Hora(time(14, 30)))
            self.horas.append(Hora(time(15)))
            self.horas.append(Hora(time(15, 30)))
            self.horas.append(Hora(time(16)))
            self.horas.append(Hora(time(16, 30)))
            self.horas.append(Hora(time(17)))
            self.horas.append(Hora(time(17, 30)))
        else:
            self.horas.append(Hora(time(18)))
            self.horas.append(Hora(time(18, 30)))
            self.horas.append(Hora(time(19)))
            self.horas.append(Hora(time(19, 30)))
            self.horas.append(Hora(time(20)))
            self.horas.append(Hora(time(20, 30)))
            self.horas.append(Hora(time(21)))
            self.horas.append(Hora(time(21, 30)))
            self.horas.append(Hora(time(22)))
            self.horas.append(Hora(time(22, 30)))