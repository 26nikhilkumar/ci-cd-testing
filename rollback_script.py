import logging

logging.basicConfig(filename="ci_cd.log", level=logging.INFO)

try:
    logging.info("Starting rollback...")
    # Simulate rollback logic
    logging.info("Rollback completed successfully.")
except Exception as e:
    logging.error(f"Rollback failed: {e}")
    raise
