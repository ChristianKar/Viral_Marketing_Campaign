import pandas as pd
import numpy as np
from os import getcwd
import matplotlib.pyplot as plt
import datetime

CURR_PATH = getcwd()
# to get the current working directory
PATH_DATA = CURR_PATH + "/data/"

accounts_data = pd.read_csv(PATH_DATA + "instagram_accounts.csv")
posts_data = pd.read_csv(PATH_DATA + "instagram_posts.csv")

print(accounts_data.head())
print(accounts_data.info())
# print(posts_data.head())

accounts_data['sex'].map({"male": 0, "female": 1}).head()
plt.show()