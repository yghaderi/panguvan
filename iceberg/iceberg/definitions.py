from dagster import Definitions, load_assets_from_modules

from . import tgju  # noqa: TID252

all_assets = load_assets_from_modules([tgju])

defs = Definitions(
    assets=all_assets,
)
