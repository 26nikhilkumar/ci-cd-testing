import logging

logging.basicConfig(filename="ci_cd.log", level=logging.INFO)

try:
    logging.info("Starting deployment...")
    raise Exception("Simulated deployment failure!")  # Simulate a failure
except Exception as e:
    logging.error(f"Deployment failed: {e}")
    raise
