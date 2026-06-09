SELECT
    user_id,
    age,
    country,
    subscription
FROM read_csv_auto('data/raw/users.csv');
