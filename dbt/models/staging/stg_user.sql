SELECT
    user_id,
    country,
    subscription_type
FROM {{ source('raw', 'dim_user') }}
