#!/usr/bin/env python
# coding: utf-8

# In[112]:


import pandas as pd
data=pd.read_csv(r'C:\Users\HP\Desktop\BMI/BMI_Dataset.csv')
data.describe()
data


# In[113]:


class BMICalculator:
    
    #BMI calculation
    def calculator_BMI(self,weight,height):
        return round(weight/((height/100)**2),2)
    
    #classifying person based on BMI values 
    def classify_person_based_BMI(self,bmi):
        if bmi<=18.49:
            return "Underweight:Malnutrition risk"
        elif bmi>=18.5 and bmi<=24.99:
            return "Normal weight:Low risk"
        elif bmi>=25 and bmi<=29.99:
            return "Overweight:Enhanced risk"
        elif bmi>=30 and bmi<=34.99:
            return "Moderately obese:Medium risk"
        elif bmi>=35 and bmi<=39.99:
            return "Severely obese:High risk"
        else:
            return "Very severely obese:Very high risk"
        
    #overWeight count
    def overweight_count(self,data):
        count=0
        for i in range(len(data["BMI Category"])):
            if bmi_category[i]=="Overweight":
                count+=1
        return count
    
    #adding new columns
    def add_columns(self,data):
        bmi=pd.Series([])
        health_risk= pd.Series([])
        bmi_category=pd.Series([])
        for i in range(len(data)):
            height= data["HeightCm"][i] 
            weight=data["WeightKg"][i]
            bmi[i]=self.calculator_BMI(weight,height)
            bmi_category_list=self.classify_person_based_BMI(bmi[i]).split(":")
            health_risk[i]=bmi_category_list[1]
            bmi_category[i]=bmi_category_list[0]
        data.insert(3, "BMI", bmi)
        data.insert(4, "BMI Category", bmi_category)
        data.insert(5, "Health risk", health_risk) 

bmi_calculator=BMICalculator()
bmi_calculator.add_columns(data)
print("Number of Overweight Persons: "+ str(bmi_calculator.overweight_count(data)))
        


# In[114]:


data


# In[115]:


import unittest

class Test_BMICalculator(unittest.TestCase):
    bmi_calculator=BMICalculator()
    def test_BMI(self):
        self.assertEqual(bmi_calculator.calculator_BMI(80,141),40.24)      
        self.assertEqual(bmi_calculator.calculator_BMI(55,125),35.2)        
        self.assertEqual(bmi_calculator.calculator_BMI(90,162),34.29)     
        self.assertEqual(bmi_calculator.calculator_BMI(76,168),26.93)              
        self.assertEqual(bmi_calculator.calculator_BMI(68,184),20.09)
        self.assertEqual(bmi_calculator.calculator_BMI(55,173),18.38)    
         
    def test_BMI_category(self):
        self.assertEqual(bmi_calculator.classify_person_based_BMI(45).split(":")[0],"Very severely obese")
        self.assertEqual(bmi_calculator.classify_person_based_BMI(39.9).split(":")[0],"Severely obese")
        self.assertEqual(bmi_calculator.classify_person_based_BMI(30.0).split(":")[0],"Moderately obese")
        self.assertEqual(bmi_calculator.classify_person_based_BMI(29.99).split(":")[0],"Overweight")
        self.assertEqual(bmi_calculator.classify_person_based_BMI(18.5).split(":")[0],"Normal weight")
        self.assertEqual(bmi_calculator.classify_person_based_BMI(15).split(":")[0],"Underweight")
    
    def test_health_risk(self):
        self.assertEqual(bmi_calculator.classify_person_based_BMI(18.4).split(":")[1],"Malnutrition risk")
        self.assertEqual(bmi_calculator.classify_person_based_BMI(24.9).split(":")[1],"Low risk") 
        self.assertEqual(bmi_calculator.classify_person_based_BMI(25).split(":")[1],"Enhanced risk")
        self.assertEqual(bmi_calculator.classify_person_based_BMI(32.88).split(":")[1],"Medium risk")
        self.assertEqual(bmi_calculator.classify_person_based_BMI(37.75).split(":")[1],"High risk")
        self.assertEqual(bmi_calculator.classify_person_based_BMI(42.5).split(":")[1],"Very high risk")
        pass
        

unittest.main(argv=[''], verbosity =2, exit = False)


# In[ ]:




