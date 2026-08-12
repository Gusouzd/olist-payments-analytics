SELECT 
    op.order_id,
    op.payment_sequential,
    op.payment_type,
    op.payment_installments,
    op.payment_value,
    o.order_purchase_timestamp,
    o.order_approved_at,
    o.order_status,
    COUNT(*) OVER(PARTITION BY op.order_id) AS payments_per_order
FROM {{ ref('stg_order_payments') }} AS op
INNER JOIN {{ ref('stg_orders') }} o ON op.order_id = o.order_id