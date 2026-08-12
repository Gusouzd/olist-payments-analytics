WITH agrupamento AS (

    SELECT 
        DATE_TRUNC(pe.order_purchase_timestamp, MONTH) as MES,
        pe.payment_type AS TIPO_PAGAMENTO,
        COUNT(*) AS COMPRAS_POR_MES,
        SUM(payment_value) AS VALOR_TOTAL
    FROM {{ ref('int_payments_enriched') }} AS pe
    GROUP BY MES, TIPO_PAGAMENTO

), 

porcentagem AS (

    SELECT
        MES,
        TIPO_PAGAMENTO,
        COMPRAS_POR_MES,
        VALOR_TOTAL,
        ROUND((VALOR_TOTAL / (SUM(VALOR_TOTAL) OVER(PARTITION BY MES)))* 100, 2) AS PCT_VALOR
    FROM agrupamento

)

SELECT * FROM porcentagem
