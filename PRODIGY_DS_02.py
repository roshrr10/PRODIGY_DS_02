#!/usr/bin/env python
# coding: utf-8

# # TASK 2

# AIM: To perform data cleaning and exploratory data analysis (EDA) on the insurance dataset. The dataset contains information about individuals, including their age, gender, body mass index (BMI), and other attributes.

# In[1]:


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load the dataset
file_path = 'insurance.csv'
data = pd.read_csv(file_path)


# In[3]:


# Display the first few rows of the dataset
data.head()


# In[4]:


# Checking for missing values
data.isnull().sum()


# In[5]:


# Display basic statistics
data.describe()


# In[6]:


# Check data types of each column
data.dtypes


# In[7]:


# Plotting the distribution of ages using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['age'], kde=True, bins=30)
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[8]:


# Plotting the distribution of BMI using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['bmi'], kde=True, bins=30)
plt.title('Distribution of BMI')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.show()


# In[9]:


# Plotting the distribution of expenses using a histogram
plt.figure(figsize=(10, 6))
sns.histplot(data['expenses'], kde=True, bins=30)
plt.title('Distribution of Expenses')
plt.xlabel('Expenses')
plt.ylabel('Frequency')
plt.show()


# In[10]:


# Plotting the distribution of genders using a bar chart
plt.figure(figsize=(10, 6))
sns.countplot(x='sex', data=data)
plt.title('Distribution of Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[11]:


# Plotting the distribution of smokers using a bar chart
plt.figure(figsize=(10, 6))
sns.countplot(x='smoker', data=data)
plt.title('Distribution of Smokers')
plt.xlabel('Smoker')
plt.ylabel('Count')
plt.show()


# In[12]:


# Plotting the distribution of regions using a bar chart
plt.figure(figsize=(10, 6))
sns.countplot(x='region', data=data)
plt.title('Distribution of Regions')
plt.xlabel('Region')
plt.ylabel('Count')
plt.show()


# In[13]:


# Scatter plot of age vs. expenses
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='expenses', data=data)
plt.title('Age vs. Expenses')
plt.xlabel('Age')
plt.ylabel('Expenses')
plt.show()


# In[14]:


# Scatter plot of BMI vs. expenses
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bmi', y='expenses', data=data)
plt.title('BMI vs. Expenses')
plt.xlabel('BMI')
plt.ylabel('Expenses')
plt.show()


# In[15]:


# Box plot of smoker vs. expenses
plt.figure(figsize=(10, 6))
sns.boxplot(x='smoker', y='expenses', data=data)
plt.title('Smoker vs. Expenses')
plt.xlabel('Smoker')
plt.ylabel('Expenses')
plt.show()


# In[16]:


# Box plot of region vs. expenses
plt.figure(figsize=(10, 6))
sns.boxplot(x='region', y='expenses', data=data)
plt.title('Region vs. Expenses')
plt.xlabel('Region')
plt.ylabel('Expenses')
plt.show()


# In[17]:


# Violin plot of region vs. expenses
plt.figure(figsize=(10, 6))
sns.violinplot(x='region', y='expenses', data=data)
plt.title('Region vs. Expenses')
plt.xlabel('Region')
plt.ylabel('Expenses')
plt.show()


# In[18]:


# Pairplot to explore relationships between multiple variables
sns.pairplot(data, hue='smoker')
plt.show()


# ## Conclusion
# 
# We performed data cleaning and exploratory data analysis (EDA) on the insurance dataset. We explored the distributions of various features such as age, BMI, expenses, gender, smoker status, and region. Additionally, we examined relationships between variables to identify patterns and trends in the data.
# 
# Key findings include:
# - The distribution of ages and BMIs shows a range of values with certain peaks.
# - Expenses show a right-skewed distribution, indicating that a smaller number of individuals have high medical expenses.
# - The gender distribution is fairly balanced.
# - A significant difference in expenses between smokers and non-smokers, with smokers generally incurring higher expenses.
# - Regional differences in expenses, though less pronounced than the smoker effect.
# - Scatter plots indicate a positive relationship between BMI and expenses, and between age and expenses to some extent.
# 
# These insights can help in understanding the demographics and characteristics of the individuals in the dataset, as well as in making informed decisions for further analysis or modeling tasks.
# 
