## 🟦 Select Columns
### SQL
```
SELECT col1, col2, col3
FROM table;
```
### Pandas
```
df[['col1', 'col2', 'col3']]
```
### PySpark
```
df.select('col1', 'col2', 'col3')
```

<br><br>

## 🟩 Filtering & Conditions
### SQL
```
SELECT *
FROM table
WHERE amount > 100
  AND status = 'active';
```
### Pandas
```
df[(df['amount'] > 100) & (df['status'] == 'active')]
```
### PySpark
```
df.filter((F.col('amount') > 100) & (F.col('status') == 'active'))
```

<br><br>

## 🟧 Cleaning & Transformations

### Replace Nulls
**SQL**
```
sql
SELECT COALESCE(col, 0) AS col
FROM table;
```
**Pandas**
```
python
df.fillna({'col': 0})
```

**PySpark**
```
df.fillna({'col': 0})
```

### Remove Duplicates

**SQL**
```
SELECT DISTINCT col1, col2 FROM table;
```

**Pandas**
```
df.drop_duplicates(subset=['col1', 'col2'])
```
**PySpark**
```
df.dropDuplicates(['col1', 'col2'])
```

### Create New Columns
**SQL**
```
SELECT *, price * qty AS total
FROM sales;
```

**Pandas**
```
df['total'] = df['price'] * df['qty']
```

**PySpark**
```
df.withColumn('total', F.col('price') * F.col('qty'))
```

<br><br>

## 🟨 Working with Dates

### Extract Components

**SQL**
```
SELECT
  EXTRACT(YEAR FROM date_col) AS year,
  EXTRACT(MONTH FROM date_col) AS month
FROM table;
```

**Pandas**
```
df['year'] = df['date_col'].dt.year
df['month'] = df['date_col'].dt.month
```

**PySpark**
```
df.withColumn('year', F.year('date_col')) \
  .withColumn('month', F.month('date_col'))
```  

### Date Differences

**SQL**
```
SELECT DATEDIFF(day, start_date, end_date) AS diff_days
FROM table;
```

**Pandas**
```
(df['end_date'] - df['start_date']).dt.days
```

**PySpark**
```
df.withColumn('diff_days', F.datediff('end_date', 'start_date'))
```


<br><br>

## 🟪 Group By & Aggregations

### SQL
```
SELECT category,
       COUNT(*) AS cnt,
       SUM(amount) AS total_amount,
       AVG(amount) AS avg_amount
FROM sales
GROUP BY category;
```

### Pandas
```
df.groupby('category').agg(
    cnt=('amount', 'count'),
    total_amount=('amount', 'sum'),
    avg_amount=('amount', 'mean')
)
```

### PySpark
```
df.groupBy('category').agg(
    F.count('*').alias('cnt'),
    F.sum('amount').alias('total_amount'),
    F.avg('amount').alias('avg_amount')
)
```


<br><br>

## 🟥 Joins

### SQL
```
SELECT a.*, b.value
FROM tableA a
JOIN tableB b ON a.id = b.id;
```

### Pandas
```
dfA.merge(dfB, on='id', how='inner')
```

### PySpark
```
dfA.join(dfB, on='id', how='inner')
```

<br><br>

## 🟫 Window Functions

### Row Number / Ranking
**SQL**
```
ROW_NUMBER() OVER(PARTITION BY dept ORDER BY salary DESC)
```

**Pandas**
```
df['rn'] = df.sort_values('salary', ascending=False) \
             .groupby('dept') \
             .cumcount() + 1
```

**PySpark**
```
w = Window.partitionBy('dept').orderBy(F.col('salary').desc())
df.withColumn('rn', F.row_number().over(w))
```

### Running Totals
**SQL**
```
 SUM(amount) OVER(PARTITION BY category ORDER BY date)
```

**Pandas**
```
df['running_total'] = df.sort_values('date') \
                        .groupby('category')['amount'] \
                        .cumsum()
```

**PySpark**
```
w = Window.partitionBy('category').orderBy('date') \
          .rowsBetween(Window.unboundedPreceding, Window.currentRow)
df.withColumn('running_total', F.sum('amount').over(w))
```

<br><br>

## 🟦 CTEs (Common Table Expressions)

### SQL
```
WITH sales_cte AS (
    SELECT *, price * qty AS total
    FROM sales
)
SELECT category, SUM(total)
FROM sales_cte
GROUP BY category;
```

### Pandas Equivalent
```
sales_cte = df.assign(total=df['price'] * df['qty'])
sales_cte.groupby('category')['total'].sum()
```

### PySpark Equivalent
```
sales_cte = df.withColumn('total', F.col('price') * F.col('qty'))
sales_cte.groupBy('category').sum('total')
```

<br><br>

## 🟧 CASE WHEN Patterns
### SQL
```
SELECT
  CASE
    WHEN score >= 90 THEN 'A'
    WHEN score >= 80 THEN 'B'
    ELSE 'C'
  END AS grade
FROM table;
```
### Pandas
```
df['grade'] = np.select(
    [df['score'] >= 90, df['score'] >= 80],
    ['A', 'B'],
    default='C'
)
```
### PySpark
```
df.withColumn(
    'grade',
    F.when(F.col('score') >= 90, 'A')
     .when(F.col('score') >= 80, 'B')
     .otherwise('C')
)
```
<br><br>

# 🟦 Delta Lake Commands (Databricks)

## Create Delta Table
```
sql
CREATE TABLE sales_delta
USING DELTA
AS SELECT * FROM sales;
```

## Optimize
```
sql
OPTIMIZE sales_delta;
```

## Z-Order
```
sql
OPTIMIZE sales_delta
ZORDER BY (customer_id);
```

## Time Travel
```
sql
SELECT * FROM sales_delta VERSION AS OF 3;
SELECT * FROM sales_delta TIMESTAMP AS OF '2024-01-01';
```

## Merge (Upsert)
```
sql
MERGE INTO target t
USING source s
ON t.id = s.id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```
<br><br>

# 🟪 Databricks Shortcuts & Tips
## Magic Commands
```
%sql
SELECT * FROM table;
```
```
%python
df = spark.table("table")
```

## Display
```
python
display(df)
```

## Auto Loader
```
python
cloudFiles
.format("cloudFiles")
.option("cloudFiles.format", "json")
.load("/path")
```

## Create a Managed Table
```
sql
CREATE TABLE my_table
USING DELTA
LOCATION '/mnt/data/my_table';
```

<br><br>

# 🟦 Quick Reference Table
|Subject	|SQL|	Pandas	|PySpark|
|--|--|--|--|
Select|	SELECT col	|df[col]	|select()|
Filter|	WHERE	|df[...]	|filter()
Clean|	COALESCE, DISTINCT	|fillna, drop_duplicates	|fillna, dropDuplicates
Dates|	EXTRACT, DATEDIFF	|.dt.year, .dt.days	|year(), datediff()
Group|	GROUP BY	|groupby().agg()	|groupBy().agg()
Join|	JOIN	|merge()|	join()
Window|	OVER()	|cumcount(), cumsum()|	Window().over()
CTE|	WITH cte AS (...)	|assign()|	withColumn()
CASE|	CASE WHEN	|np.select()	|when().otherwise()
Delta|	OPTIMIZE, MERGE	|—|	spark.read/write.format("delta")