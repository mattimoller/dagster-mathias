from dagster import Definitions, load_assets_from_modules

from .assets import amsterdam_marathon

all_assets = load_assets_from_modules([amsterdam_marathon])

defs = Definitions(
    assets=all_assets,
)
