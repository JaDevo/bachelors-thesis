
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
import csv

def pltlongterm():
    ltus = pd.read_csv("usgby.csv", parse_dates=["DATE"], index_col="DATE")
    ltde = pd.read_csv("grmn10.csv", parse_dates=["DATE"], index_col="DATE")
    eur = pd.read_csv("euro99.csv", parse_dates=["DATE"], index_col="DATE")
    plt.plot(ltde,label='de')
    plt.plot(eur,label='eur')
    plt.plot(ltus,label='ltus')
    plt.title("Long_term interest rates")
    plt.xlabel("Years")
    plt.ylabel("% Return")
    plt.legend()
    plt.show()
# pltlongterm()
diff = pd.read_csv("lt_diff.csv", parse_dates=["DATE"], index_col="DATE")
def pltlongtermnew():
    ltus = pd.read_csv("DGS10.csv", parse_dates=["DATE"], index_col="DATE")
    eur = pd.read_csv("IRLTLT01EZM156N.csv", parse_dates=["DATE"], index_col="DATE")
    diff = pd.read_csv("lt_diff.csv", parse_dates=["DATE"], index_col="DATE")
    plt.plot(eur,label='Euro')
    plt.plot(ltus,label='US')
    plt.plot(diff,label='Difference')
    plt.title("Long-Term Interest Rates and Difference")
    plt.xlabel("Years")
    plt.ylabel("% Return")
    plt.legend()
    plt.grid()
    plt.show()
# pltlongtermnew()
stdiff = pd.read_csv("st_diff.csv", parse_dates=["DATE"], index_col="DATE")
def pltshortterm():
    steu = pd.read_csv("st_euro.csv", parse_dates=["DATE"], index_col="DATE")
    stus = pd.read_csv("3mmm.csv", parse_dates=["DATE"], index_col="DATE")
    stdiff = pd.read_csv("st_diff.csv", parse_dates=["DATE"], index_col="DATE")
    plt.plot(steu[0:198],label='S-T Euro')
    plt.plot(stus[0:198],label='S-T US')
    plt.plot(stdiff[0:198],label = "Difference")
    plt.title("Short-Term Interest Rates")
    plt.xlabel("Years")
    plt.ylabel("% Return")
    plt.legend()
    plt.grid()
    plt.show()
pltshortterm()
uscomp = pd.read_csv("us comp.csv", parse_dates=["DATE"], index_col="DATE")
def pltusrates():
    ltus = pd.read_csv("usgby.csv", parse_dates=["DATE"], index_col="DATE")
    stus = pd.read_csv("3mmm.csv", parse_dates=["DATE"], index_col="DATE")
    uscomp = pd.read_csv("us comp.csv", parse_dates=["DATE"], index_col="DATE")
    plt.plot(ltus,label='Rt')
    plt.plot(stus,label="rt")
    plt.plot(uscomp,label = ('Rt-rt'))
    plt.title("US Long-Term and Short-Term Interest Rates")
    plt.xlabel("Years")
    plt.ylabel("% Return")
    plt.grid()
    plt.legend()
    plt.show()
# pltusrates()
spread = pd.read_csv("spread.csv", parse_dates=["DATE"], index_col="DATE")
def pltspread():
    us = pd.read_csv("us comp.csv", parse_dates=["DATE"], index_col="DATE")
    eu = pd.read_csv("euro comp.csv", parse_dates=["DATE"], index_col="DATE")
    spread = pd.read_csv("spread.csv", parse_dates=["DATE"], index_col="DATE")
    plt.plot(us,label='US Yield')
    plt.plot(eu,label="Euro Yield")
    plt.plot(spread,label = "Spread")
    plt.title("Difference of US and European Yield Curves")
    plt.xlabel("Years")
    plt.ylabel("% Return")
    plt.grid()
    plt.legend()
    plt.show()
# pltspread()

eucomp = pd.read_csv("euro comp.csv", parse_dates=["DATE"], index_col="DATE")
def plteurrates():
    steur = pd.read_csv("st_euro.csv", parse_dates=["DATE"], index_col="DATE")
    lteur = pd.read_csv("lt_euro.csv", parse_dates=["DATE"], index_col="DATE")
    eucomp = pd.read_csv("euro comp.csv", parse_dates=["DATE"], index_col="DATE")
    plt.plot(lteur,label='Rt')
    plt.plot(steur,label='rt')
    plt.plot(eucomp, label = "Rt-rt")
    plt.title("Euro Long-Term and Short-Term Interest Rates")
    plt.xlabel("Years")
    plt.ylabel("% Return")
    plt.grid()
    plt.legend()
    plt.show()
# plteurrates()

def pltdifferencing():
    diffeur = pd.read_csv("diffeur.csv", parse_dates=["DATE"], index_col="DATE")
    diffus = pd.read_csv("diffus.csv", parse_dates=["DATE"], index_col="DATE")
    plt.plot(diffeur, label="EUROZONE")
    plt.plot(diffus, label="US")
    plt.title('Eurozone & US Yield Curves')
    plt.xlabel("Year")
    plt.ylabel("(Long-Term Rates) - (Short-Term Rates)")
    plt.plot(figsize=(20,10))
    plt.legend()
    plt.show()
# pltdifferencing()
    
stus = pd.read_csv("3mmm.csv", parse_dates=["DATE"], index_col="DATE")#difference stationary
steu = pd.read_csv("st_euro.csv", parse_dates=["DATE"], index_col="DATE")#non-stationary
ltus = pd.read_csv("usgby.csv", parse_dates=["DATE"], index_col="DATE")#non-stationary
eur = pd.read_csv("euro99.csv", parse_dates=["DATE"], index_col="DATE")#non-stationary
# print(eur.head())
st_diff = pd.read_csv("st_diff.csv", parse_dates=["DATE"], index_col="DATE")

def adf_test(timeseries):
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)
# adf_test(stus["TB3MS", 0:198])

    
    
def kpsstest(timeseries):
    print ('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression='c')
    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Lags Used'])
    for key,value in kpsstest[3].items():
        kpss_output['Critical Value (%s)'%key] = value
    print(kpss_output)
# kpsstest(eucomp["Value"])
    
# def firstgraph(x,y):
#     a = pd.read_csv(x+".csv", parse_dates=["DATE"], index_col="DATE")
#     b = pd.read_csv(y+".csv", parse_dates=["DATE"], index_col="DATE")
#     plt.plot(a,label=x)
#     plt.plot(b,label=y)
#     plt.title(x+" & "+y)
#     plt.xlabel("Years")
#     plt.ylabel("Percent")
#     plt.legend()
#     plt.show()

# def single_graph(x):
#     a = pd.read_csv(x+".csv", parse_dates=["DATE"], index_col="DATE")
#     plt.plot(a,label=x)
#     plt.title(x)
#     plt.xlabel("Years")
#     plt.ylabel("Percent")
#     plt.legend()
#     plt.show()

def differ(name):
    name['Value_diff'] = name['Value'] - name['Value'].shift(1)
    name['Value_diff'].dropna().plot()
    test_set = name['Value_diff'].dropna()
    adf_test(test_set)
    kpsstest(test_set)
#     return(test_set)
# differ(eucomp)


def logdiff(name):
    name['Value_log'] = np.log(name['Value'])
    name['Value_log_diff'] = name['Value_log'] - name['Value_log'].shift(1)
    name['Value_log_diff'].dropna().plot()
    test_set = name['Value_log_diff'].dropna()
    
def twice_differ(name):
    name['Value_diff'] = name['Value'] - name['Value'].shift(1)
    name['Value_diff_diff'] = name['Value_diff'] - name['Value_diff'].shift(1)
    name["Value_diff_diff"]
    test_set = name["Value_diff_diff"].dropna().plot()
#     adf_test(test_set)
#     kpsstest(test_set)
#     return(test_set)
    
# twice_differ(eucomp)
    
# with open('DEXUSEU.csv', 'w', newline = '') as file:
#     thewriter = csv.writer(file)
#     thewriter.writerow(['DEXUSEU'])
#     for i in range(238):
#         thewriter.writerow([twice_differ(exchange)[i]])

print(ltus.index)


# In[2]:


# from pandas.tools.plotting import autocorrelation_plot
 

# series = pd.read_csv("usgby.csv", parse_dates=["DATE"], index_col="DATE")
# autocorrelation_plot(series)
# plt.show()

#ltus
#ltde
#eur
#stus
# steur -> test_set2(stationary after differencing with both adf and kpss)
# diffeur
# diffus


# In[3]:


lt_us = pd.read_csv("lt_us.csv", parse_dates=["DATE"], index_col="DATE")

def adf_test(timeseries):
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)
    
def kpsstest(timeseries):
    print ('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression='c')
    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Lags Used'])
    for key,value in kpsstest[3].items():
        kpss_output['Critical Value (%s)'%key] = value
    print(kpss_output)

def differ(name):
    name['Value_diff'] = name['Value'] - name['Value'].shift(1)
    name['Value_diff'].dropna().plot()
    test_set = name['Value_diff'].dropna()
    adf_test(test_set)
    kpsstest(test_set)
    return(test_set)

def logdiffer(name):
    name['Value_log'] = np.log(name['Value'])
    name['Value_log_diff'] = name['Value_log'] - name['Value_log'].shift(1)
    name['Value_log_diff'].dropna().plot()
    test_set = name['Value_log_diff'].dropna()
    adf_test(test_set)
    kpsstest(test_set)
    
def twice_differ(name):
    name['Value_diff'] = name['Value'] - name['Value'].shift(1)
    name['Value_diff_diff'] = name['Value_diff'] - name['Value_diff'].shift(1)
    name["Value_diff_diff"]
    test_set = name["Value_diff_diff"].dropna()

adf_test(spread["Value"])

# def main():
    
    

# if __name__ = "__main__":
#     main()
# main()


# In[14]:


import numpy as np
import statsmodels
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint, adfuller

def check_for_stationarity(X, cutoff=0.01):
    # H_0 in adfuller is unit root exists (non-stationary)
    # We must observe significant p-value to convince ourselves that the series is stationary
    pvalue = adfuller(X)[1]
    if pvalue < cutoff:
        print('p-value = '+ str(pvalue) + ' The series ' + X.name +' is likely stationary.')
        return True
    else:
        print('p-value = ' + str(pvalue) + ' The series ' + X.name +' is likely non-stationary.')
        return False
check_for_stationarity(stdiff["Value"])


# In[ ]:


# ltus = pd.read_csv("usgby.csv", parse_dates=["DATE"], index_col="DATE")#stationary at both with differencing
# ltus.rename(columns = {'IRLTLT01USM156N':'Value'}, inplace=True)
# ltde = pd.read_csv("grmn10.csv", parse_dates=["DATE"], index_col="DATE")#stationary at both with differencing
# ltde.rename(columns = {'IRLTLT01DEM156N':'Value'}, inplace=True)
# stus = pd.read_csv("yess.csv", parse_dates=["DATE"], index_col="DATE")#stationary with twice differencing
# stus.rename(columns = {'TB3MS':'Value'}, inplace=True)
# steur = pd.read_csv("wesee.csv", parse_dates=["DATE"], index_col="DATE")#stationary after differencing
# stadiffeur = pd.read_csv("diffeur.csv", parse_dates=["DATE"], index_col="DATE")#already stationary
# diffeur = pd.read_csv("diffeur.csv", parse_dates=["DATE"], index_col="DATE")
# diffeur.rename(columns = {'diff()':'Value'}, inplace=True)
# diffus = pd.read_csv("diffus.csv", parse_dates=["DATE"], index_col="DATE")#stationary after differencing
# diffus.rename(columns = {'diffus()':'Value'}, inplace=True)
# lteur = pd.read_csv("lteur.csv", parse_dates=["DATE"], index_col="DATE")#stationary after twice differencing
# lteur.rename(columns = {'IRLTLT01EZM156N':'Value'}, inplace=True)
# euroyield = pd.read_csv("yeildcurveeur.csv", parse_dates=["DATE"], index_col="DATE")
#################################################################################################################


# In[ ]:


# # with open('daten.csv', 'w', newline = '') as file:
# #     thewriter = csv.writer(file)
# #     thewriter.writerow(['US Yield','Euro long-term','US long_term','US short-term'])
# #     for i in range(238):
# #         thewriter.writerow([differ(diffus)[i],twice_differ(lteur)[i],differ(ltus)[i],twice_differ(stus)[i]])
    
# # , 'US Yield', 'Euro long-term', 'US long-term', 'Euro short-term', 'US short-term'


# In[17]:


# plt.plot(diff)
# plt.plot(stdiff)
# plt.show
stdiff.head()


# In[17]:


portion = (stus[0:198])
print(portion)


# In[18]:


adf_test(portion["TB3MS"])


# In[20]:


adf_test(diff["Value"])


# In[10]:


x = (stus[0:198])
adf_test(x["TB3MS"])
kpsstest(x["TB3MS"])

