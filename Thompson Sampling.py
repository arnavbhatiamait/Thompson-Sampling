# %% [markdown]
# Thompson Sampling

# %% [markdown]
# Importing the libraries

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import math

# %% [markdown]
# Import the Data set

# %%
df=pd.read_csv("Ads_CTR_Optimisation.csv")
df.head()

# %% [markdown]
# Implementing Thompson Sampling

# %%
N=10000
d=10
ads_selected=[]
no_of_reward_1=[0]*d #alpha
no_of_reward_0=[0]*d #beta
Total_reward=0
for n in range(N):
    ad=0
    max_random=0
    for i in range (d):
        random_beta=random.betavariate(no_of_reward_1[i]+1,no_of_reward_0[i]+1)
        # max_random=max(max_random,random_beta)
        if (max_random<random_beta):
            max_random=random_beta
            ad=i
    ads_selected.append(ad)
    reward=df.values[n,ad]
    if(reward==1):
        no_of_reward_1[ad]+=1
    else:
        no_of_reward_0[ad]+=1
    Total_reward+=reward
# print(ads_selected)
# print(Total_reward)
    

# %% [markdown]
# Visulation of The Results

# %%
plt.hist(ads_selected)
plt.title("Histogram of Thompson Sampling")
plt.xlabel("Ads")
plt.ylabel("Number of Times each ad was selected")
plt.savefig("Thompson Sampling Histogram.png")
plt.show()


