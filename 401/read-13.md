# Linear Regressions

## Read
[How to Run Linear Regression in Python](http://bigdata-madesimple.com/how-to-run-linear-regression-in-python-scikit-learn/)
- SciKit-Learn
  - powerful Python module for ML
    - linreg, classification, clustering, model selection, dimensionality reduction
- Boston Housing Data
  - `import sklearn`
  - `df.columns = boston.feature_names`
- create linreg object
  - lm.fit() 
    - fits a linear model
  - lm.predict()
    - predict Y using linear model with est coeff.
- fitting linear model  
  - lm.fit(X, bos.PRICE)
    - see high coeff at RM
    - plt.scatter(bos.RM, bos.PRICE)
    - xlabel, ylabel, title, show
- Predicting
  - lm.predict(X)[0:5]
    - outputs array of predicted y's
- Train-test split
  - divide data sets randomly
    - skl provides train_test_split()
    - ?????
## Videos
[Intro to Simple Linear Regressions](https://www.youtube.com/watch?v=KsVBBJRb9TE)
- simple for one explanatory variable
- predicted var = y
  - response (dependent)
- used var = x 
  - explanatory (independent)
- discover correlation between x and y
- assume linear relationship
  - E(y|x) = y-int + slopeX
  - random error component
  - produce est. regression line
  - yhat = yint-hat + mhatX
    - least squares

## Additional Resources
[Linear Regression in Python](https://realpython.com/linear-regression-in-python/)

## Bookmark and Review
[Train & Test Splits](https://towardsdatascience.com/train-test-split-and-cross-validation-in-python-80b61beca4b6)

## Things I'd like to know more about
- I could definitely use a refresher on least squares and differential eq's...