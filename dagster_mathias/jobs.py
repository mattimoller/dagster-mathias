from dagster import DefaultScheduleStatus, ScheduleDefinition, job

from .assets.amsterdam_marathon import bib_reporter


@job
def check_bib_availability():
    bib_reporter()


bib_schedule = ScheduleDefinition(
    job=check_bib_availability,
    cron_schedule="3,13,23,33,43,53 * * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)
