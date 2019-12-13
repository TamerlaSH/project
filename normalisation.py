import pandas as pd
import numpy as np

features_data = pd.read_csv('features_data_with_churned')
del features_data[list(features_data.columns)[0]]
columns = list(features_data.columns)


normal = {"risk_tolerance":
{"low_risk_tolerance":-1,"med_risk_tolerance":0,"high_risk_tolerance":1},
          "investment_experience":
{"no_investment_exp":-1,"good_investment_exp":0,"limited_investment_exp":1,"extensive_investment_exp":2},
          "liquidity_needs":
{"not_important_liq_need":-1,"somewhat_important_liq_need":0,"very_important_liq_need":1},
          "platform":
{"Android":-1,"both":0,"iOS":1},
          "instrument_type_first_traded":
{"wrt":-1,"0":0,"stock":1,"mlp":2,"etp":3,"reit":4,"adr":5,"rlt":6,"tracking":7,"lp":8,"cef":9},
          "time_horizon":
{"short_time_horizon":-1,"med_time_horizon":0,"long_time_horizon":1}}



for column in columns:
    if column in normal:
        features_data[column].replace(normal[column], inplace = True)
features_data.to_csv('normalisations.csv', index = False)