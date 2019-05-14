import pandas as pd
import numpy as np
from datetime import date 
from dateutil.relativedelta import relativedelta

df = pd.read_csv("episode_data.csv")

df['Service date'] = pd.to_datetime(df['Service date'])

e1 = df.loc[df['patient_id'] == 1]

print(e1.sample(3))

codes = ["o1", "bw", "xr", "hs", "ip", "pt"]

e11 = df.loc[(df['patient_id'] == 1) & (df['Service code'] == "hs")]

e13 = df["Service date"].loc[(df['patient_id'] == 1) & (df['Service code'] == "hs")]

print(e13.iloc[0])
print(e11)

e12 = df.loc[(df['patient_id'] == 1) & (df['Service code'].isin(codes)) \
    & ((e13.iloc[0] + relativedelta(months=-3) <= df['Service date'])) &\
    (df['Service date'] <= (e13.iloc[0] + relativedelta(months=+1)))]

print(e12)