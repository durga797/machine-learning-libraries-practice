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



#grab_initial_state_data()

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
HPI_data = pd.read_pickle('fiddy_states3.pickle')

HPI_data['TX1yr'] = HPI_data['TX'].resample('A',how='mean')
#TX1yr = HPI_data['TX'].resample('A',how='ohlc')
print HPI_data[['TX','TX1yr']].head()
#HPI_data.dropna(inplace=True)
#HPI_data.fillna(method='bfill',inplace=True)
#HPI_data.fillna(method='ffill',inplace=True)
HPI_data.fillna(value=-99999,limit=10,inplace=True)

#print HPI_data[['TX','TX1yr']]

print HPI_data.isnull().values.sum()

HPI_data[['TX','TX1yr']].plot(ax=ax1,label='monthly HPI_TX')

plt.legend(loc=4)

plt.show()
