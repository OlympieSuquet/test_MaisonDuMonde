SELECT t.date,
	sum(t.prod_price*t.prod_qty) as "chiffre d'affaires"
FROM transactions t
WHERE t.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY t.date
ORDER BY t.date ASC;


SELECT t.client_id AS Client,
	sum(CASE WHEN p.product_type = "MEUBLE" THEN t.prod_price*prod_qty
		ELSE 0 END) AS ventes_meuble,
	sum(CASE WHEN p.product_type = "DECO" THEN t.prod_price*prod_qty
		ELSE 0 END) AS ventes_deco
FROM transactions t
INNER JOIN product_nomenclature p ON p.product_id = t.prod_id
WHERE t.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY t.client_id;