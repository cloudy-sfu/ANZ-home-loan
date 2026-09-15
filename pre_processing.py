import os

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import MultiTaskLassoCV, LinearRegression
from sklearn.metrics import r2_score
from sqlalchemy import create_engine, text

from postgresql_upsert import upsert_dataframe

# %% Load data.
engine = create_engine(os.environ['NEON_DB'], pool_recycle=300)
with open("sqls/resample_ins_mortgage_rate.sql") as f:
    sql_ins = f.read()
with open("sqls/resample_ocr.sql") as f:
    sql_ocr = f.read()
with open("sqls/resample_wholesale_swap_rate.sql") as f:
    sql_swap = f.read()
with engine.connect() as c:
    anz_standard_known = pd.read_sql(text(sql_ins), c, params={
        'bank': 'ANZ',
        'special': False
    })
    anz_special_known = pd.read_sql(text(sql_ins), c, params={
        'bank': 'ANZ',
        'special': True
    })
    ocr = pd.read_sql(text(sql_ocr), c)
    swap = pd.read_sql(text(sql_swap), c)
    anz_pred = pd.read_sql_table("ins_mortgage_rate_pred", c)

pass
