#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import re
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# Load the CSV files
file_paths = {
    '도시공원': r'C:\Users\jeong\Desktop\Photonics Project\streamlit_data\부산 도시 공원.csv',
    '보관소': r'C:\Users\jeong\Documents\도로명주소(자전거보관소).csv',
    '대여소': r'C:\Users\jeong\Desktop\Photonics Project\streamlit_data\부산광역시_자전거대여소_20230822.csv'
}

encoding = 'euc-kr'
data = {}

for key, file_path in file_paths.items():
    data[key] = pd.read_csv(file_path, encoding=encoding)

# Function to extract '구' or '군' from the address
def extract_gu_gun(address):
    if isinstance(address, str):
        match = re.search(r'(\S+구|\S+군)', address)
        return match.group(1) if match else None
    return None

# Extract '구' or '군' from each dataset
data['도시공원']['구군'] = data['도시공원']['소재지지번주소'].apply(extract_gu_gun)
data['보관소']['구군'] = data['보관소']['도로명 주소'].apply(extract_gu_gun)
data['대여소']['구군'] = data['대여소']['소재지지번주소'].apply(extract_gu_gun)
data['대여소']['구군'].fillna(data['대여소']['소재지도로명주소'].apply(extract_gu_gun), inplace=True)

# Count the number of entries for each '구' or '군' in each dataset
counts = {}
for key in data.keys():
    counts[key] = data[key]['구군'].value_counts()

# Combine the counts into a single DataFrame
combined_counts = pd.DataFrame(counts).fillna(0)
combined_counts['총개수'] = combined_counts.sum(axis=1)

# Sort the combined counts in descending order
combined_counts_sorted = combined_counts.sort_values(by='총개수', ascending=False)

# Save the combined counts to a CSV file
output_csv_path = r'C:\Users\jeong\Desktop\Photonics Project\streamlit_data\combined_counts.csv'
combined_counts_sorted.to_csv(output_csv_path, encoding='euc-kr')

# Set the font for Korean characters explicitly
font_path = r"C:\Users\jeong\Desktop\LG_Smart_UI-Regular.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Plot the results as a bar chart
plt.figure(figsize=(14, 10))
combined_counts_sorted['총개수'].plot(kind='bar')
plt.title('Number of Parks, Storage, and Rental Locations by 구/군')
plt.xlabel('구/군')
plt.ylabel('Total Number of Locations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:





# In[1]:


import pandas as pd
import re
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


# In[2]:


# Load the CSV files
file_paths = {
    '도시공원': r'C:\Users\jeong\Desktop\Photonics Project\streamlit_data\부산 도시 공원.csv',
    '보관소': r'C:\Users\jeong\Documents\도로명주소(자전거보관소).csv',
    '대여소': r"C:\Users\jeong\Desktop\Photonics Project\공공데이터\자전거 대여소.csv"}

encoding = 'euc-kr'
data = {}


# In[3]:


for key, file_path in file_paths.items():
    data[key] = pd.read_csv(file_path, encoding=encoding)


# In[5]:


data


# In[6]:


# Function to extract '구' or '군' from the address
def extract_gu_gun(address):
    if isinstance(address, str):
        match = re.search(r'(\S+구|\S+군)', address)
        return match.group(1) if match else None
    return None


# In[7]:


# Extract '구' or '군' from each dataset
data['도시공원']['구군'] = data['도시공원']['소재지지번주소'].apply(extract_gu_gun)
data['보관소']['구군'] = data['보관소']['도로명 주소'].apply(extract_gu_gun)
data['대여소']['구군'] = data['대여소']['소재지지번주소'].apply(extract_gu_gun)
data['대여소']['구군'].fillna(data['대여소']['소재지도로명주소'].apply(extract_gu_gun), inplace=True)


# In[8]:


data['도시공원']['구군']


# In[9]:


# Count the number of entries for each '구' or '군' in each dataset
counts = {}
for key in data.keys():
    counts[key] = data[key]['구군'].value_counts()


# In[10]:


# Combine the counts into a single DataFrame
combined_counts = pd.DataFrame(counts).fillna(0)
combined_counts['총개수'] = combined_counts.sum(axis=1)


# In[11]:


combined_counts


# In[13]:


# Sort the combined counts in descending order
combined_counts_sorted = combined_counts.sort_values(by='총개수', ascending=False)

# Save the combined counts to a CSV file
#output_csv_path = r'C:\Users\jeong\Desktop\Photonics Project\streamlit_data\combined_counts.csv'
#combined_counts_sorted.to_csv(output_csv_path, encoding='euc-kr')


# In[14]:


combined_counts_sorted


# In[15]:


# Set the font for Korean characters explicitly
font_path = r"C:\Users\jeong\Desktop\LG_Smart_UI-Regular.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


# In[19]:


# Plot the results as a stacked bar chart with different colors
plt.figure(figsize=(14, 10))
combined_counts_sorted[['도시공원', '보관소', '대여소']].plot(kind='bar', stacked=True, color=['green', 'blue', 'red'])
plt.title('구/군별 공원,대여소,보관소 수')
plt.xlabel('구/군')
plt.ylabel('개수')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[ ]:




