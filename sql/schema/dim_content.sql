SELECT
    content_id,
    'unknown' AS title,
    'unknown' AS category
FROM read_csv_auto('data/raw/content_events.csv');
