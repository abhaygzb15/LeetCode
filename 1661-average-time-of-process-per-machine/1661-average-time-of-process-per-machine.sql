# Write your MySQL query statement below
with processdurations as (
    select machine_id,process_id,
    max(case when activity_type="end" then timestamp else null end) -
    max(case when activity_type="start" then timestamp else null end) as duration
    from activity group by machine_id,process_id
)

select machine_id,round(avg(duration),3) as "processing_time" from processdurations group by machine_id;