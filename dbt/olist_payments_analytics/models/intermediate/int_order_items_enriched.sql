SELECT
    oi.order_id,
    oi.product_id,
    oi.price,
    oi.freight_value,
    p.product_category_name
FROM {{ ref('stg_order_items') }} oi
INNER JOIN {{ ref('stg_products') }} p ON oi.product_id = p.product_id