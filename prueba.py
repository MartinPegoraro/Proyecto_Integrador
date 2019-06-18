import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import random
import numpy as np

ex=pd.read_excel("E:\Desktop\Proyecto Integrador\Proyecto-Integrador\Tablas-copia.xlsx")
for x in range(562):
    ex.CantHs.T[x]=random.randrange(4, 6)

writer = ExcelWriter('E:\Desktop\Proyecto Integrador\Proyecto-Integrador\Tablas-copia.xlsx')
ex.to_excel(writer,'Materia', index=False)
writer.save()