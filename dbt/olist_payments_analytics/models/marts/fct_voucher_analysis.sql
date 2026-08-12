WITH voucher_agregado AS (
    SELECT
        order_id,
        COUNT(DISTINCT payment_type) AS TIPOS_DE_PAGAMENTO,
        SUM(CASE WHEN payment_type = 'voucher' THEN payment_value ELSE 0 END) AS SOMA_VALOR_VOUCHER,
        SUM(payment_value) AS VALOR_PAGO
    FROM {{ ref('int_payments_enriched') }}
    GROUP BY order_id
),

tipo_de_uso AS (

    SELECT 
        order_id,
        TIPOS_DE_PAGAMENTO,
        SOMA_VALOR_VOUCHER,
        VALOR_PAGO,
        CASE WHEN TIPOS_DE_PAGAMENTO = 1 THEN 'Exclusivo' ELSE 'Combinado' END AS USO_EXCLUSIVO,
        ROUND(SOMA_VALOR_VOUCHER / VALOR_PAGO * 100, 2) AS PCT_COBERTO_VOUCHER
    FROM voucher_agregado
    WHERE SOMA_VALOR_VOUCHER > 0

)

SELECT *
FROM tipo_de_uso