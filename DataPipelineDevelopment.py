import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

#Loading the Dataset
data = pd.read_csv("sampledataset.csv")


numerical_categories = ['age', 'income']
string_categories = ['gender', 'city']
target = 'target'

#Splitting dataset to features and targets
X = data[numerical_categories + string_categories]
y = data[target]

#Defining Transformations
#Numerical pipeline
num_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

#Categorical pipeline
string_pipeline = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

#Combinining all the pipelines
preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, numerical_categories),
    ('cat', string_pipeline, string_categories)
])

#Creating output pipeline
full_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor)
])

#Transforming the dataset
X_processed = full_pipeline.fit_transform(X)

#One hot encoded column names
encoded_columns = full_pipeline.named_steps['preprocessor'] \
    .named_transformers_['cat'] \
    .named_steps['encoder'] \
    .get_feature_names_out(string_categories)

#Combining column names
all_columns = numerical_categories + list(encoded_columns)

#Adding processed data to a frame
X_df = pd.DataFrame(X_processed, columns=all_columns)
X_df['target'] = y.values

#Saving as csv format
X_df.to_csv("processed_dataset.csv", index=False)

print("Processing completed\nData is ready for use.")
