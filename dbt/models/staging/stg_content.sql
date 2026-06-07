SELECT
    e.user_id,
    e.content_id,
    u.country,
    u.subscription,
    e.watch_time,
    e.click,
    CASE 
        WHEN e.watch_time > 20 THEN 1 
        ELSE 0 
    END AS high_engagement
FROM {{ ref('stg_events') }} e
LEFT JOIN {{ ref('stg_user') }} u
    ON e.user_id = u.user_id
