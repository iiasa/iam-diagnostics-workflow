from pathlib import Path

import pyam
from nomenclature import DataStructureDefinition, RegionProcessor, process
from scenariocompass import ScenarioCompassProcessor

here = Path(__file__).absolute().parent


def main(df: pyam.IamDataFrame) -> pyam.IamDataFrame:
    """Project/instance-specific workflow for scenario processing"""

    # Run the validation and processing
    definition = DataStructureDefinition(here / "definitions")
    return process(
        df,
        definition,
        processor=[
            RegionProcessor.from_directory(here / "mappings", definition),
            ScenarioCompassProcessor(),
        ],
    )
