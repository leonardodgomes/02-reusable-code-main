## PAndas Cheatsheet

|Command|Explanation|
|--|--|
|df.shape	|# Get dimensions of df|
|df.head()	|# Display first 5 rows|
|df.info()	|# Show datatypes and info|
|df.dropna()	|# Remove missing values|
|df['column']	|# Select single column|
|df.describe()	|# Get summary statistics|
|df.reset_index()	|# Reset row indices|
|df.fillna(value)	|# Fill missing values|
|df.value_counts()	|# Count unique values|
|df.loc[row_label]	|# Select rows by label|
|df.iloc[row_index]	|# Select rows by position|
|df['column' ].mean()|	# Calculate column average|
|df[['col1', 'col2' ]]	|# Select multiple columns|
|df.merge(df2, on='key')	|# Combine two dataframes|
|df.sort_values('column')	|# Sort by column values|
|df.drop('column', axis=1)	|# Remove columns|
|df.groupby('column').agg()	|# Group and aggregate data|
|df.query('column > value')	|# Filter using condition|
|df = pd.read_csv('file.csv')	|# Load data from CSV file|
|df.rename(columns={'old': 'new'})	|# Rename columns|
