# Time Series Evaluation - WIP
## XGBoost vs fbProphet

# time series forecasting of a kaggle dataset:  
https://www.kaggle.com/hmavrodiev/london-bike-sharing-dataset

The train dataset is about 16 months long. The aim is to predict the number of bikes taken out each hour of each day in the 3-month long test dataset. We use two models:

###XGBoost
Tree-based ensembling approach. Currently the stronger of the two models in terms of root-mean-squared-error.

###fbProphet
multiple non-linear trends with multiple seasonal trends applied. This model is currently much weaker than XGBoost, though it needs more tuning.