import asyncio
import logging

from fastapi import FastAPI, HTTPException
import os



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
            "level": 'DEBUG',
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


@app.post("/sleep")
async def do_sleep():
    logging.info('sleep called')
    sleep_time = os.getenv("SLEEP_TIME", None)
    if not sleep_time:
        logging.warning('Env variable is empty')
        raise HTTPException(status_code=400, detail="Empty env var")

    await asyncio.sleep(int(sleep_time))

    logging.info('prepare answer')
    return {"time": sleep_time}


@app.get(
    "/ping",
    responses={"200": {"content": {"application/json": {"example": {"status": "OK"}}}}},
)
async def ping() -> dict:
    """Health check for service"""
    return {"status": "OK"}
