import pandas as pd
import numpy as np
from datetime import datetime, timedelta
np.random.seed(42)
df = pd.DataFrame({
    'id': range(1,10001),
    'cliente': ['Cliente_'+str(np.random.randint(1,501)) for _ in range(10000)],
    'categoria': np.random.choice(['Facturación','Técnico','Cuenta','Producto','Entrega'],10000),
    'prioridad': np.random.choice(['Baja','Media','Alta','Crítica'],10000, p=[0.3,0.4,0.2,0.1]),
    'agente': np.random.choice(['Fernanda P.','Carlos M.','Ana L.'],10000),
    'tiempo_resolucion_horas': np.random.randint(1,73,10000),
    'satisfaccion': np.random.randint(1,6,10000),
    'estado': np.random.choice(['Resuelto','Abierto','En espera','Escalado'],10000, p=[0.7,0.1,0.1,0.1]),
    'fecha': [(datetime(2024,1,1)+timedelta(days=int(x))).date().isoformat() for x in np.random.randint(0,600,10000)]
})
df.to_csv('tickets_10k.csv', index=False)