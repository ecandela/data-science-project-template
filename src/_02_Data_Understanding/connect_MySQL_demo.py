import pandas as pd
from sqlalchemy import create_engine


def get_engine():
    conx = "mysql+mysqlconnector://usuario:clave$@localhost/test"
    engine = create_engine(conx)
    return engine

cnxn = get_engine()

sql_cab = " SELECT * FROM test.ejemplo "
df_cab = pd.read_sql(sql_cab,cnxn)  

print(df_cab)