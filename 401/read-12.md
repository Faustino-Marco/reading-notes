# Pandas

## Read 
[reading](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
- See Cookbook
- Object Creation
  - Series
    - let pandas create a default integer index
      - `pd.Series([1,3,4,np.nan,6,8])`
  - DataFrame
    - use NumPy
      - datetime index vs labeled columns
    - pass a dictionay of objects that can be converted into a series like structure

- Viewing Data
  - head() / tail()
  - .to_numpy()
  - [] slices rows (enter value for position)
    - boolean indexing: use > 0
  - .reindex() resets axis

- Operations
  - exclude empties

- Histogramming
  - .value_counts()

- String Methods
  - .str.lower()

- Concat
  - ???

## Video
- All sorts of operations with and for data
  - All revolves around the "dataframe"
- Works in tandem with numpy, matplotlib
- Can run all sorts of stats ops on data 
- different commands to access various rows, columns and individual data

- Ex. Titanic, MSFT stock
  - can access things like liklihood of survival, stock price patterns
-  Operations are available
## Bookmark and Review
[Master Pandas](https://towardsdatascience.com/be-a-more-efficient-data-scientist-today-master-pandas-with-this-guide-ea362d27386)