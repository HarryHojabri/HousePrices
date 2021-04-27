# HousePrices
Predict sales prices and practice feature engineering

The House Price project, taken from Kaggle, is about creating a model to predict house prices. With 79 features describing so many aspects of residential homes in Ames, Iowa, this competition is to predict the final price of each home in the test set.

https://www.kaggle.com/c/house-prices-advanced-regression-techniques

There are 2 datasets in the project:

"train.csv" which is the labeled training set including different information such as basement condition, garage type, etc., and their labels, "SalePrice" indicating the price of each of the 1459 houses in the training set.

"test.csv" including 1459 unlabeled houses: After training the model on train.csv, the labels are calculated for the this dataset and stored in the corresponding .csv file.

The library scikit-learn is imported and Random Forest is applied to solve the problem.
