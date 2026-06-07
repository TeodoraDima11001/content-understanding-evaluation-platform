CREATE TABLE fact_content_events (
    event_id BIGINT,
    content_id VARCHAR(50),
    user_id VARCHAR(50),
    event_timestamp TIMESTAMP,
    event_type VARCHAR(50),
    watch_time_seconds INT,
    completion_rate FLOAT,
    device_type VARCHAR(50),
    country VARCHAR(50),
    session_id VARCHAR(100)
);
