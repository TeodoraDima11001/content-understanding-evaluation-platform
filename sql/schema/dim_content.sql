CREATE TABLE dim_content (
    content_id VARCHAR(50) PRIMARY KEY,
    title VARCHAR(255),
    creator_id VARCHAR(50),
    language VARCHAR(50),
    content_format VARCHAR(50),
    genre VARCHAR(100),
    subgenre VARCHAR(100),
    mood VARCHAR(100),
    release_date DATE
);
