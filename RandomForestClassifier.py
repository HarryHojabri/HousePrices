import pandas as pd
import numpy as np
import train_data_cleanning
import test_data_cleanning
import categ_onehot_multicol
from sklearn.ensemble import RandomForestClassifier
import csv


# Read train set
train_data = pd.read_csv("train.csv")
# Read test set
test_data = pd.read_csv("test.csv")


# Droping the features with over 50% blank values and filling blank values with mean and mode
# values for the features having blank values in data_cleanning classes for the treain and test sets:
train_data_cleanning.clean_train_data(train_data)
test_data_cleanning.clean_test_data(test_data)


# In the following, categorical features are listed to convert to integer in onehot encoding
FeaturesToConvert=['MSZoning','Street','LotShape','LandContour','Utilities','LotConfig','LandSlope','Neighborhood',
'Condition1','Condition2','BldgType','HouseStyle','RoofStyle','RoofMatl','Exterior1st','Exterior2nd','ExterQual',
'ExterCond','Foundation','BsmtQual','BsmtCond','BsmtExposure','BsmtFinType1','BsmtFinType2','Heating','HeatingQC',
'CentralAir','Electrical','KitchenQual','Functional','FireplaceQu','GarageType','GarageFinish','GarageQual','GarageCond',
'PavedDrive','SaleType','SaleCondition', 'MasVnrType']

# Since some of the categorical features take different numbers of values in train and test sets, the onehot encoding
# is done on a concatenated set of them.
final_trd = pd.concat([train_data, test_data], axis = 0)
final_trd = categ_onehot_multicol.cat_onehot(FeaturesToConvert, final_trd)

# The following line removes any column that is correlated with another column which are therefore redundant.
final_trd = final_trd.loc[:, ~final_trd.columns.duplicated()]

# After the onehot encoding is done and categorical features are converted to integer, the concatenated set is split to
# train set and test set.
new_train_data = final_trd.iloc[:1422, :]
new_test_data = final_trd.iloc[1422:, :]

# The initial test set had no label. However, after the concatenation and onehot encoding, one needs to make sure the
# label is droped.
new_test_data.drop(['SalePrice'], axis = 1, inplace = True)

# In the new train set, the label should get split so the train data is prepared to train and predict the result for
# the test set.
y_train = new_train_data['SalePrice']
new_train_data.drop(['SalePrice'], axis = 1, inplace = True)
x_train = new_train_data


x_test = new_test_data


rfc = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
rfc.fit(x_train, y_train)

predictions = rfc.predict(x_test)

with open('submission_random_forest2.csv', 'w', newline ='') as file_pred:
    writer_pred = csv.writer(file_pred)
    writer_pred.writerow(["Id", "SalePrice"])
    for i in range(1461, 2920):
        writer_pred.writerow([i, predictions[i-1461]])
file_pred.close()
print("Your submission was successfully saved!")








#clf = xgboost.XGBRegressor()
#clf.fit(cleanned_train_data, label)
#label_pred = clf.predict(cleanned_test_data)
