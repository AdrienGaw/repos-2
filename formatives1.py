#!/usr/bin/env python
# coding: utf-8

# ### 1. Savings Function

# In[26]:


def savings(gross_pay, tax_rate, expenses):
    return int((gross_pay*(1-tax_rate))-expenses)

savings(901, 0.34, 150)


# ### 2. Material Waste Function

# In[10]:


def material_waste(total_material, material_units, num_jobs, job_consumption):
    return str(total_material-num_jobs*job_consumption)+material_units

material_waste(350, "kg", 6, 20)


# ### 3. Interest Function

# In[1]:


def interest(principal, rate, periods):
    return int(principal*rate*periods + principal)

interest(500, 0.3, 2)    


# In[ ]:




