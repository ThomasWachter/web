import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

celebra_vencimento=[0,1,2,3,4,5,6,7,8,9,10]
clebra_precio=[14000,10000,9990,9000,8500,8430,8300,8000,7900,5000,4800]
ibuprofeno_precio=[5000,4000,4500,4398,4200,4189,4000,3999,3900,3850,3800]
viadil_precio=[5000,4890,4300,4250,4200,4180,4100,4110,3990,3867,3860]

plt.plot(celebra_vencimento, clebra_precio)
plt.title("precio del producto vs meses de vencimiento")
plt.xlabel("meses de vencimiento")
plt.ylabel("precio")

plt.plot(celebra_vencimento,ibuprofeno_precio)
plt.plot(celebra_vencimento, viadil_precio)

plt.legend(["celebra","ibuprofeno","viadil"])

plt.show()

