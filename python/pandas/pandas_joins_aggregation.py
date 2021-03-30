import pandas as pd
import numpy as np
url = (
       "https://raw.github.com/pandas-dev"
      "/pandas/master/pandas/tests/io/data/csv/tips.csv"
   )

tips = pd.read_csv(url)

tips.head()
tips[["total_bill", "tip", "smoker", "time"]].head(5)
tips.assign(tip_rate=tips["tip"]/tips["total_bill"]).head(5)
## assigning where clause
tip_with_rate=tips.assign(tip_rate=tips["tip"]/tips["total_bill"])

# Boolean indexing
is_dinner = tips["time"] == "Dinner"
is_dinner.value_counts()


# Filteration 
tip_new=tip_with_rate[(tip_with_rate["time"] == "Dinner") & (tip_with_rate["tip"] > 5.00)]

# Rank function implementation in Pandas
#SELECT * FROM (
#  SELECT
#    t.*,
#    RANK() OVER(PARTITION BY sex ORDER BY tip) AS rnk
#  FROM tips t
#  WHERE tip < 2
#)
#WHERE rnk < 3
#ORDER BY sex, rnk;
#equivalent in pandas  is provided below.

(
     tips[tips["tip"] < 2]
     .assign(rnk_min=tips.groupby(["sex"])["tip"].rank(method="min"))
     .query("rnk_min < 3")
     .sort_values(["sex", "rnk_min"])
  )