SELECT
    user_id,
    content_id,
    watch_time,
    click,
    content_type
FROM {{ source('raw', 'content_events') }}
