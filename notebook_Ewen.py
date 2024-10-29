# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import numpy as np
df = pd.read_csv('donnees.csv', header= 96)
df

# %%
mask = df['disc_year'] < 2000
df[mask]

# %%
mask = (df['discoverymethod'] == 'Radial Velocity') & (df['disc_year'] > 2015)
mask.value_counts()

# %%
by_station = df.groupby(by= 'disc_facility')
len(by_station)

# %%
by_station.size()

# %%
max(by_station.size())

# %%
mask = (df['disc_facility'] == 'Multiple Observatories')
mask.value_counts()

# %%
mask = (df['disc_facility'] == 'Okayama Astrophysical Observatory')
mask.value_counts()

# %%
df.pivot_table(values = 'disc_year', index = 'disc_facility', columns = 'sy_pnum', aggfunc = max)

# %%
df.pivot_table(values = 'disc_year', index = 'disc_facility', columns = 'sy_pnum', aggfunc = min)

# %%
