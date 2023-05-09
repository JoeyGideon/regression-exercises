# regression-exercises

# a place for my regression exercises and files related to these exeercises



## Data Dictionary

| Feature | Definition | Data Type | 
| --- | --- | --- |
| id | row index number, range: 0 - 2985216 | int64 |
| parcelid | Unique numeric id assigned to each property: 10711725 - 169601949  | int64 |
| bathroomcnt | Number of bathrooms a property has: 0 - 32 | float64 | 
| bedroomcnt | Number of bedrooms a property has: 0 - 25  | float64 |
| calculatedfinishedsquarefeet | Number of square feet of the property: 1 - 952576 | float64 |
| fips | [(FIPS)](https://transition.fcc.gov/oet/info/maps/census/fips/fips.txt) Five digit number of which the first two are the FIPS code of the state to which the county belongs. Leading 0 is removed from the data: 6037=Los Angeles County, 6059=Orange County, 6111=Ventura County | float64 |
| lotsizesquarefeet |The land the property occupies in squared feet : 100 - 371000512 | float64 |
| propertylandusetypeid | Unique numeric id that identifies what the land is used for: the 261=Single Family Residential, 262=Rural Residence, 273=Bungalow | float64 |
| roomcnt | Total number of rooms in the principal residence | float64 |
| yearbuilt | Year the property was built | float64 |
| transactiondate| The most recent date the property was sold: yyyy-mm-dd | object |
 
| Target | Definition | Data Type |
| --- | --- | --- |
| taxamount | The total property tax assessed for that assessment year | float64 |
| taxvaluedollarcnt |The total tax assessed value of the parcel | float64 |



```

