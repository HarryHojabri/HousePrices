import pandas as pd
import numpy as np


def clean_test_data(test_data):

# Droping the features with over 50% blank values and the feature 'Id'
    test_data.drop(['Alley', 'PoolQC', 'GarageYrBlt', 'Fence', 'MiscFeature', 'Id'], axis = 1, inplace = True)

# Filling blank values in floating features with mean value
    test_data["LotFrontage"] = test_data["LotFrontage"].fillna(test_data["LotFrontage"].mean())
    test_data["BsmtFinSF1"] = test_data["BsmtFinSF1"].fillna(test_data["BsmtFinSF1"].mean())
    test_data["BsmtFinSF2"] = test_data["BsmtFinSF2"].fillna(test_data["BsmtFinSF2"].mean())
    test_data["BsmtUnfSF"] = test_data["BsmtUnfSF"].fillna(test_data["BsmtUnfSF"].mean())
    test_data["TotalBsmtSF"] = test_data["TotalBsmtSF"].fillna(test_data["TotalBsmtSF"].mean())
    test_data["GarageCars"] = test_data["GarageCars"].fillna(test_data["GarageCars"].mean())
    test_data["GarageArea"] = test_data["GarageArea"].fillna(test_data["GarageArea"].mean())

# Filling blank values in features below with mode value
    test_data["MSZoning"] = test_data["MSZoning"].fillna(test_data["MSZoning"].mode()[0])
    test_data["BsmtCond"] = test_data["BsmtCond"].fillna(test_data["BsmtCond"].mode()[0])
    test_data["BsmtQual"] = test_data["BsmtQual"].fillna(test_data["BsmtQual"].mode()[0])
    test_data["FireplaceQu"] = test_data["FireplaceQu"].fillna(test_data["FireplaceQu"].mode()[0])
    test_data["GarageType"] = test_data["GarageType"].fillna(test_data["GarageType"].mode()[0])
    test_data["GarageFinish"] = test_data["GarageFinish"].fillna(test_data["GarageFinish"].mode()[0])
    test_data["GarageQual"] = test_data["GarageQual"].fillna(test_data["GarageQual"].mode()[0])
    test_data["GarageCond"] = test_data["GarageCond"].fillna(test_data["GarageCond"].mode()[0])
    test_data["MasVnrType"] = test_data["MasVnrType"].fillna(test_data["MasVnrType"].mode()[0])
    test_data["Utilities"] = test_data["Utilities"].fillna(test_data["Utilities"].mode()[0])
    test_data["BsmtFinType1"] = test_data["BsmtFinType1"].fillna(test_data["BsmtFinType1"].mode()[0])
    test_data["KitchenQual"] = test_data["KitchenQual"].fillna(test_data["KitchenQual"].mode()[0])
    test_data["Functional"] = test_data["Functional"].fillna(test_data["Functional"].mode()[0])
    test_data["SaleType"] = test_data["SaleType"].fillna(test_data["SaleType"].mode()[0])
    test_data["Exterior1st"] = test_data["Exterior1st"].fillna(test_data["Exterior1st"].mode()[0])
    test_data["Exterior2nd"] = test_data["Exterior2nd"].fillna(test_data["Exterior2nd"].mode()[0])
    test_data["BsmtFullBath"] = test_data["BsmtFullBath"].fillna(test_data["BsmtFullBath"].mode()[0])
    test_data["BsmtHalfBath"] = test_data["BsmtHalfBath"].fillna(test_data["BsmtHalfBath"].mode()[0])
    test_data["BsmtExposure"] = test_data["BsmtExposure"].fillna(test_data["BsmtExposure"].mode()[0])
    test_data["BsmtFinType2"] = test_data["BsmtFinType2"].fillna(test_data["BsmtFinType2"].mode()[0])
    test_data["LandContour"] = test_data["LandContour"].fillna(test_data["LandContour"].mode()[0])
    test_data["LandSlope"] = test_data["LandSlope"].fillna(test_data["LandSlope"].mode()[0])
    test_data["Condition2"] = test_data["Condition2"].fillna(test_data["Condition2"].mode()[0])
    test_data["YrSold"] = test_data["YrSold"].fillna(test_data["YrSold"].mode()[0])
    test_data["PavedDrive"] = test_data["PavedDrive"].fillna(test_data["PavedDrive"].mode()[0])
    test_data["MSSubClass"] = test_data["MSSubClass"].fillna(test_data["MSSubClass"].mode()[0])
    test_data["CentralAir"] = test_data["CentralAir"].fillna(test_data["CentralAir"].mode()[0])
    test_data["MasVnrArea"] = test_data["MasVnrArea"].fillna(test_data["MasVnrArea"].mode()[0])
