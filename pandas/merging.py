import pandas as pd

df1 = pd.DataFrame({'Year':[2001,2002,2003,2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]})
 
df3 = pd.DataFrame({'Year':[2001,2003,2004,2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]})



merged= pd.merge(df1,df3,on='Year',how='left')

merged.set_index('Year',inplace=True)
print "Left join \n",merged

merged= pd.merge(df1,df3,on='Year',how='right')
print "Right join \n", merged

merged= pd.merge(df1,df3,on='Year',how='outer')
print "Outer join \n", merged

merged= pd.merge(df1,df3,on='Year',how='inner')



print "Inner join \n" ,merged

