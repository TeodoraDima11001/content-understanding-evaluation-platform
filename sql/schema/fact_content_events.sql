SELECT
    e.user_id,
    e.content_id,
    u.age,
    u.country,
    u.subscription,
    e.watch_time,
    e.click,

    CASE 
        WHEN e.watch_time > 20 THEN 1 
        ELSE 0 
    END AS high_engagement

FROM read_csv_auto('data/raw/content_events.csv') e
LEFT JOIN read_csv_auto('data/raw/users.csv') u
ON e.user_id = u.user_id;
