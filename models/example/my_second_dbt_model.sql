{{ config(materialized='table') }}

with source_data as (

    select 10 as id
    union all
    select 20 as id

)

select *
from source_data
