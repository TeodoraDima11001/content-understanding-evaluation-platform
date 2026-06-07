SELECT
    user_id,
    age,
    country,
    subscription
FROM {{ source('raw', 'users') }}
