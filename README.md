# HousePrices
Predict sales prices and practice feature engineering

The House Price project, taken from Kaggle, is about creating a model to predict house prices. With 79 features describing so many aspects of residential homes in Ames, Iowa, this competition is to predict the final price of each home in the test set.

https://www.kaggle.com/c/house-prices-advanced-regression-techniques

There are 2 datasets in the project:

"train.csv" which is the labeled training set including different information such as basement condition, garage type, etc., and their labels, "SalePrice" indicating the price of each of the 1459 houses in the training set.

"test.csv" including 1459 unlabeled houses: After training the model on train.csv, the labels are calculated for the this dataset and stored in the corresponding .csv file.

The library scikit-learn is imported and Random Forest is applied to solve the problem.

The main part of this project though is feature engineering and dara cleaning where 5 features in training and test sets include over 50% blank values and are droped then, 39 and 35 feaures include a smaller number of blank values in train and test sets respectively and those blank values are filled with either mean or mode values depending on their types.

Also, there are 39 categorical features which need to be converted to integer so the algorithm can use them and come up with predictions. To do so, onehot encoding is applied and the redundant columns (with correlation to other columns) are dropped afterwards.
