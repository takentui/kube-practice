import logging
import os

from fastapi import FastAPI, HTTPException

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s %(levelname)s] %(name)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


logging.config.dictConfig(LOGGING)

app = FastAPI()


@app.get("/factorial")
async def get_factorial(n: int | None = None) -> int:
    if n is None:
        n = int(os.getenv("DEFAULT_N", 0))
    logging.info("Start calculating")
    if not n:
        logging.warning("N is less than 1")
        raise HTTPException(status_code=400, detail="WTF bro?")

    result = 1
    for i in range(n):
        result *= i + 1

    logging.info("prepare answer")
    return result
