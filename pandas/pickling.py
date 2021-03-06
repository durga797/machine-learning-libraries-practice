import quandl
import pandas as pd
import pickle

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
        if main_df.empty:
            main_df = df
        
        else:
            main_df = main_df.join(df)
     
    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()        


data = grab_initial_state_data()
HPI_data = pd.read_pickle('fiddy_states.pickle')