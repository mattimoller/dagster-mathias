from dagster import ScheduleDefinition, job

from .assets.amsterdam_marathon import bib_reporter


@job
def check_bib_availability():
    bib_reporter()


bib_schedule = ScheduleDefinition(
    job=check_bib_availability, cron_schedule="*/10 * * * *"
)
