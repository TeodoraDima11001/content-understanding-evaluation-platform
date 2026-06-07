SELECT
    event_id,
    content_id,
    user_id,
    event_timestamp,
    event_type,
    watch_time_seconds,
    completion_rate
FROM {{ source('raw', 'fact_content_events') }}
