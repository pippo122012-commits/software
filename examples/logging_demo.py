"""Standalone file-logging demonstration; inspect analysis.log afterward."""

import logging

logging.basicConfig(
    filename="analysis.log", level=logging.INFO, format="%(levelname)s: %(message)s"
)
logging.debug("Reading one row")
logging.info("Analysis started")
logging.warning("Some rows were excluded")
