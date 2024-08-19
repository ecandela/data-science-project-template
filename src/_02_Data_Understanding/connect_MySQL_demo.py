import pandas as pd
from sqlalchemy import create_engine


def get_engine():
    conx = "mysql+mysqlconnector://root:Windows2019!$@localhost/sia_22"
    engine = create_engine(conx)
    return engine

cnxn = get_engine()

sql_cab = " SELECT * FROM sia_22.cd_aspecto "
df_cab = pd.read_sql(sql_cab,cnxn)  

print(df_cab)