# Time Series Evaluation
### XGBoost vs fbProphet

https://www.kaggle.com/hmavrodiev/london-bike-sharing-dataset

The train dataset is about 16 months long. The aim is to predict the number of bikes taken out each hour of each day in the 3-month long test dataset. We use two models:

### fbProphet
multiple non-linear trends with multiple seasonal trends applied. This model is currently much weaker than XGBoost, which seems to be driven by the fact that there is only slightly more than one year of data available, which is imparing the model's yearly trend.

### XGBoost
Tree-based ensembling approach. This is the stronger of the two approaches, With a drastically lower RMSE. The model originally overfit the data, and I implemented early stopping after 20 iterations to correct this. 

