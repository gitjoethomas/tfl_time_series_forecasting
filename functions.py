def train_test_split(data, percent_in_test):
    """splits data set into two arrays - train and test, based on the % to keep in test set"""
    num_to_test = len(data) - (round(len(data) * (percent_in_test / 100))) # convert % to float

    train = data[:num_to_test]
    test = data[num_to_test:]
    
    return train, test


# the algorithm also expects your date and outcome variables to be named specifically
def column_renamer(dataset):
    """renames 'timestamp' column to 'ds' and 'num_bikes' to y, as prophet expects"""
    dataset = dataset.rename({'timestamp':'ds','num_bikes':'y'}, axis = 1)
    return dataset


# xgboost doesn't like datetime datatypes, so we'll pull all the components out into new columns
def create_date_components(dataframe):
    """pulls out the datetime components from datetime data, as granular as hour-level"""
    dataframe['hour'] = dataframe['timestamp'].dt.hour
    dataframe['dayofweek'] = dataframe['timestamp'].dt.dayofweek
    dataframe['quarter'] = dataframe['timestamp'].dt.quarter
    dataframe['month'] = dataframe['timestamp'].dt.month
    dataframe['year'] = dataframe['timestamp'].dt.year
    dataframe['dayofyear'] = dataframe['timestamp'].dt.dayofyear
    dataframe['dayofmonth'] = dataframe['timestamp'].dt.day
    dataframe['weekofyear'] = dataframe['timestamp'].dt.weekofyear
    
    dataframe = dataframe.set_index('timestamp')
    
    return dataframe