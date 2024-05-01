from dagster import Definitions, load_assets_from_modules

from . import jobs
from .assets import amsterdam_marathon

all_assets = load_assets_from_modules([amsterdam_marathon])
all_schedules = [jobs.bib_schedule]
all_jobs = [jobs.check_bib_availability]
defs = Definitions(assets=all_assets, jobs=all_jobs, schedules=all_schedules)
