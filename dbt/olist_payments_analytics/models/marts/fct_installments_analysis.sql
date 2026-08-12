SELECT 
    pe.payment_type,
    COUNT(*) AS total_pedidos,
	ROUND(AVG(pe.payment_value), 2) AS ticket_medio,
	ROUND(AVG(pe.payment_installments), 2) AS media_parcelas
FROM {{ ref('int_payments_enriched')}} AS pe
GROUP BY payment_type