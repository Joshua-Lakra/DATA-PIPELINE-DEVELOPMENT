# DATA-PIPELINE-DEVELOPMENT

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : JOSHUA ATULYA LAKRA

*INTERN ID* : CT08DG1187

*DOMAIN* : DATA SCIENCE

*DURATION* : 8 WEEKS

*MENTOR* : Neela Santhosh

*Description* :
Data preprocessing is one of the most fundamental steps in the data science pipeline, as it directly affects the quality and accuracy of any machine learning model built downstream. Task 1 focuses on building a full preprocessing pipeline using two powerful Python libraries: Pandas and Scikit-learn. The objective is to prepare raw data into a clean, numerical format that a machine learning algorithm can understand and work with effectively.

To begin, we load the dataset using the pandas library, which offers fast and easy-to-use data structures. The dataset is assumed to contain both numerical features like age and income, and categorical features like gender and city. One column is designated as the target—this is the label we want the model to predict.

Next, we separate the features (X) from the target (y). At this stage, the data is still in its raw form, and may contain missing values, inconsistent formatting, or strings that need to be converted into numbers.

To deal with this, we define two separate preprocessing pipelines:
Numerical Pipeline:
Handles missing values using the SimpleImputer class with a strategy like mean.
Scales the features using StandardScaler, which standardizes values to have a mean of 0 and a standard deviation of 1. This is crucial for many algorithms that are sensitive to scale.
Categorical Pipeline:
Handles missing string data using SimpleImputer with the most_frequent strategy.
Encodes the categorical data using OneHotEncoder, converting strings like "Male" or "New York" into a binary format.
Both pipelines are combined using ColumnTransformer which maps each pipeline to its respective column type. This ensures that numerical and categorical data are processed differently but in parallel.
The full pipeline is encapsulated in a Pipeline object, which allows seamless integration and automation of all preprocessing steps. After calling .fit_transform(), we receive a clean and fully numeric matrix that is ready to be fed into a machine learning model.

As a final step, we convert the processed output into a new DataFrame with understandable column names, and save it to a new CSV file. This not only preserves the transformation but allows the data to be shared, deployed, or reused later.
The benefits of using a pipeline structure include:
Reusability and modularity.
Less code duplication.
Easier debugging and testing.
Compatibility with machine learning workflows like cross-validation and grid search.
This task sets the foundation for model building by ensuring the input data is consistent, clean, and numerical—essential properties for accurate predictions.


*OUTPUT* : 
<img width="934" height="131" alt="Image" src="https://github.com/user-attachments/assets/071fcddd-7b65-4a88-b490-49a434a96b48" />
<img width="990" height="605" alt="Image" src="https://github.com/user-attachments/assets/91a76822-c868-4965-b644-ce1b8cd715bd" />
