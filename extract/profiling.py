import pandas as pd

def profile_dataframe(df):
    # Initialize lists to store the profile information
    column_names = []
    counts = []
    datatypes = []
    null_values = []
    duplicates = []

    # Iterate through each column in the input DataFrame
    for column in df.columns:
        column_names.append(column)
        counts.append(df[column].count())
        datatypes.append(str(df[column].dtype))
        null_values.append(df[column].isnull().sum())
        duplicates.append(df[column].duplicated().sum())

    # Create the profile DataFrame
    df_prof = pd.DataFrame({
        'column_name': column_names,
        'count': counts,
        'datatype': datatypes,
        'nullValues': null_values,
        'duplicates': duplicates
    })

    return df_prof