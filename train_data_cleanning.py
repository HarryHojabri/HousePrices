import pandas as pd
import numpy as np



def clean_train_data(train_data):

# Droping the features with over 50% blank values and the feature 'Id'
    train_data.drop(['Alley', 'PoolQC', 'GarageYrBlt', 'Fence', 'MiscFeature', 'Id'], axis = 1, inplace = True)

# Filling blank values in floating features with mean value
    train_data["LotFrontage"] = train_data["LotFrontage"].fillna(train_data["LotFrontage"].mean())
    train_data["BsmtFinSF1"] = train_data["BsmtFinSF1"].fillna(train_data["BsmtFinSF1"].mean())
    train_data["BsmtFinSF2"] = train_data["BsmtFinSF2"].fillna(train_data["BsmtFinSF2"].mean())

# Filling blank values in features below with mode value
    train_data["BsmtCond"] = train_data["BsmtCond"].fillna(train_data["BsmtCond"].mode()[0])
    train_data["BsmtQual"] = train_data["BsmtQual"].fillna(train_data["BsmtQual"].mode()[0])
    train_data["FireplaceQu"] = train_data["FireplaceQu"].fillna(train_data["FireplaceQu"].mode()[0])
    train_data["GarageType"] = train_data["GarageType"].fillna(train_data["GarageType"].mode()[0])
    train_data["GarageFinish"] = train_data["GarageFinish"].fillna(train_data["GarageFinish"].mode()[0])
    train_data["GarageQual"] = train_data["GarageQual"].fillna(train_data["GarageQual"].mode()[0])
    train_data["GarageCond"] = train_data["GarageCond"].fillna(train_data["GarageCond"].mode()[0])
    train_data["MSZoning"] = train_data["MSZoning"].fillna(train_data["MSZoning"].mode()[0])
    train_data["MasVnrType"] = train_data["MasVnrType"].fillna(train_data["MasVnrType"].mode()[0])
    train_data["KitchenQual"] = train_data["KitchenQual"].fillna(train_data["KitchenQual"].mode()[0])
    train_data["Functional"] = train_data["Functional"].fillna(train_data["Functional"].mode()[0])
    train_data["SaleType"] = train_data["SaleType"].fillna(train_data["SaleType"].mode()[0])
    train_data["Exterior1st"] = train_data["Exterior1st"].fillna(train_data["Exterior1st"].mode()[0])
    train_data["Exterior2nd"] = train_data["Exterior2nd"].fillna(train_data["Exterior2nd"].mode()[0])
    train_data["BsmtFullBath"] = train_data["BsmtFullBath"].fillna(train_data["BsmtFullBath"].mode()[0])
    train_data["BsmtHalfBath"] = train_data["BsmtHalfBath"].fillna(train_data["BsmtHalfBath"].mode()[0])
    train_data["BsmtExposure"] = train_data["BsmtExposure"].fillna(train_data["BsmtExposure"].mode()[0])
    train_data["BsmtFinType2"] = train_data["BsmtFinType2"].fillna(train_data["BsmtFinType2"].mode()[0])
    train_data["LandContour"] = train_data["LandContour"].fillna(train_data["LandContour"].mode()[0])
    train_data["LandSlope"] = train_data["LandSlope"].fillna(train_data["LandSlope"].mode()[0])
    train_data["Condition2"] = train_data["Condition2"].fillna(train_data["Condition2"].mode()[0])
    train_data["YrSold"] = train_data["YrSold"].fillna(train_data["YrSold"].mode()[0])
    train_data["PavedDrive"] = train_data["PavedDrive"].fillna(train_data["PavedDrive"].mode()[0])
    train_data["MSSubClass"] = train_data["MSSubClass"].fillna(train_data["MSSubClass"].mode()[0])
    train_data["CentralAir"] = train_data["CentralAir"].fillna(train_data["CentralAir"].mode()[0])
    train_data["MasVnrArea"] = train_data["MasVnrArea"].fillna(train_data["MasVnrArea"].mode()[0])
#train_data["BsmtFinType1"] = train_data["BsmtFinType1"].fillna(train_data["BsmtFinType1"].mode()[0])
#train_data["Electrical"] = train_data["Electrical"].fillna(train_data["Electrical"].mode()[0])

# The following line removes all the rows containing a blank value.
    train_data.dropna(inplace=True)
