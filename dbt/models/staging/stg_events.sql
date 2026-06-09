SELECT
    user_id,
    content_id,
    watch_time,
    click,
    content_type
FROM read_csv_auto('data/raw/content_events.csv');
