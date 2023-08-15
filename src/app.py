import os
import logging

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/hi")
def hello_world():
    return "Hello, world!"
