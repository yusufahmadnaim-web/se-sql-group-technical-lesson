import pandas as pd
import sqlite3
conn = sqlite3.connect('data.sqlite')

q = """
SELECT country, COUNT(*)
FROM customers
GROUP BY country
;
"""
q = """
SELECT
   customerNumber,
   COUNT(*) AS number_payments,
   MIN(CAST(amount AS FLOAT)) AS min_purchase,
   MAX(CAST(amount AS FLOAT)) AS max_purchase,

AVG(CAST(amount AS FLOAT)) AS avg_purchase,
   SUM(CAST(amount AS FLOAT)) AS total_spent
FROM payments
GROUP BY customerNumber
;
"""

payment_summary = pd.read_sql(q, conn)

print(payment_summary)
q = """
SELECT
   customerNumber,
   COUNT(*) AS number_payments,
   MIN(CAST(amount AS FLOAT)) AS min_purchase,
   MAX(CAST(amount AS FLOAT)) AS max_purchase,
   AVG(CAST(amount AS FLOAT)) AS avg_purchase,
   SUM(CAST(amount AS FLOAT)) AS total_spent
FROM payments
GROUP BY customerNumber
HAVING avg_purchase > 50000
;
"""

payments_over_fifty_thousand = pd.read_sql(q, conn)
print(payments_over_fifty_thousand)

q = """
SELECT
   customerNumber,
   COUNT(*) AS number_payments,
   MIN(CAST(amount AS FLOAT)) AS min_purchase,
   MAX(CAST(amount AS FLOAT)) AS max_purchase,
   AVG(CAST(amount AS FLOAT)) AS avg_purchase,
   SUM(CAST(amount AS FLOAT)) AS total_spent
FROM payments
WHERE CAST(amount AS FLOAT) > 50000
GROUP BY customerNumber
HAVING number_payments >= 2
;
"""

multiple_purchase_payment_summary = pd.read_sql(q, conn)
print(multiple_purchase_payment_summary)

q = """
SELECT
   customerNumber,
   COUNT(*) AS number_payments,
   MIN(CAST(amount AS FLOAT)) AS min_purchase,
   MAX(CAST(amount AS FLOAT)) AS max_purchase,
   AVG(CAST(amount AS FLOAT)) AS avg_purchase,
   SUM(CAST(amount AS FLOAT)) AS total_spent
FROM payments
WHERE CAST(amount AS FLOAT) > 50000
GROUP BY customerNumber
HAVING number_payments >= 2
ORDER BY total_spent
LIMIT 1
;
"""

lowest_duplicate_spender = pd.read_sql(q, conn)
print(lowest_duplicate_spender)

conn.close()