#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# Load the CSV file
file_path = r"C:\Users\jeong\Desktop\Photonics Project\보관소(도로명주소).csv"
data = pd.read_csv(file_path)

# Function to extract '구' or '군' from the address
def extract_gu_gun(address):
    if isinstance(address, str):
        match = re.search(r'(\S+구|\S+군)', address)
        return match.group(1) if match else None
    return None

# Extract '구' or '군' from the address column
data['구군'] = data['도로명 주소'].apply(extract_gu_gun)

# Count the number of storage locations for each '구' or '군'
gu_gun_counts = data['구군'].value_counts()

# Sort the counts in descending order
gu_gun_counts_sorted = gu_gun_counts.sort_values(ascending=False)

# Set the font for Korean characters explicitly
font_path = r"C:\Users\jeong\Desktop\LG_Smart_UI-Regular.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Plot the results as a bar chart
plt.figure(figsize=(12, 8))
gu_gun_counts_sorted.plot(kind='bar')
plt.title('구/군별 자전거 보관수')
plt.xlabel('구/군')
plt.ylabel('개수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:




