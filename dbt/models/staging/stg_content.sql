SELECT
    content_id,
    title,
    genre,
    subgenre,
    language
FROM {{ source('raw', 'dim_content') }}
