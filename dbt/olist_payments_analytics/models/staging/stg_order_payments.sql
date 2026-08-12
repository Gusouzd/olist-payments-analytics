SELECT 
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    payment_value
FROM {{ source('raw_olist', 'order_payments') }}
WHERE payment_type != 'not_defined'