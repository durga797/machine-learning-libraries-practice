import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# Not necessary, I just do this so I do not show my API key.
api_key = 'C5CcQ3dSfsx9Nsk_khsf'
def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]
    
def mortage_30y():
    df = quandl.get('FMAC/MORTG',trim_start='1975-01-01',authtoken=api_key)
    df['Value'] = (df['Value']-df['Value'][0])/df['Value'][0] * 100
    df = df.resample('D')
    df = df.resample('M')
    df.columns=['mor_30']
    return df


def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.columns = [str(abbv)]
        df[abbv] = ((df[abbv]-df[abbv][0])/df[abbv][0])*100 
        print(query)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
            
    pickle_out = open('fiddy_states3.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()   

def HPI_benchmark():
    df= quandl.get('FMAC/HPI_USA', authtoken=api_key)
    df.columns = ['United_States']
    df['United_States'] = ((df['United_States']-df['United_States'][0])/df['United_States'][0])*100
    return df

mor_30 = mortage_30y()

HPI_data = pd.read_pickle('fiddy_states3.pickle')
HPI_bench = HPI_benchmark()
HPI_m30 = HPI_data.join(mor_30)


print HPI_m30.corr()['mor_30'].describe()