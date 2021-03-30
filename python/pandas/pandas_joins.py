import pandas as pd
import numpy as np
product=pd.DataFrame({
    'Product_ID':[101,102,103,104,105,106,107],
    'Product_name':['Watch','Bag','Shoes','Smartphone','Books','Oil','Laptop'],
    'Category':['Fashion','Fashion','Fashion','Electronics','Study','Grocery','Electronics'],
    'Price':[299.0,1350.50,2999.0,14999.0,145.0,110.0,79999.0],
    'Seller_City':['Delhi','Mumbai','Chennai','Kolkata','Delhi','Chennai','Bengalore']
})
customer=pd.DataFrame({
    'id':[1,2,3,4,5,6,7,8,9],
    'name':['Olivia','Aditya','Cory','Isabell','Dominic','Tyler','Samuel','Daniel','Jeremy'],
    'age':[20,25,15,10,30,65,35,18,23],
    'Product_ID':[101,0,106,0,103,104,0,0,107],
    'Purchased_Product':['Watch','NA','Oil','NA','Shoes','Smartphone','NA','NA','Laptop'],
    'City':['Mumbai','Delhi','Bangalore','Chennai','Chennai','Delhi','Kolkata','Delhi','Mumbai']
})

pd.merge(product,customer,on='Product_ID')

pd.merge(product,customer,left_on='Product_name',right_on='Purchased_Product')


#
#Let’s take things up a notch. The leadership team now wants more details about the products sold. They want to know about all the products sold by the seller to the same city i.e., seller and customer both belong to the same city.

#In this case, we have to perform an inner join on both Product_ID and Seller_City of product and Product_ID and City columns of the customer dataframe.


pd.merge(product,customer,how='inner',left_on=['Product_ID','Seller_City'],right_on=['Product_ID','City'])

# Need to do a FULL outer join 
#We can perform Full join by just passing the how argument as ‘outer’ to the merge() function:
pd.merge(product,customer,on='Product_ID',how='outer')



#mention the indicator argument as True in the function, and a new column of name _merge will be created in the resulting dataframe:

pd.merge(product,customer,on='Product_ID',how='outer',indicator=True)

#Validation in Pandas joins.
# There is a validate argument in pandas in which different arguments can be provided . 1. one_to_one, 2. many_to_many 3.many_to_one 4. one_to_many
pd.merge(product_dup,customer,how='inner',on='Product_ID',validate='many_to_many')
# above statement help to validate the results if results are many to many.
# we can also drop duplicates from input dataframe.
pd.merge(product.drop_duplicates(),customer,on='Product_ID',how='outer',indicator=True)