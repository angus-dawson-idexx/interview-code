import sqlite3
from typing import TypedDict

import boto3

BUCKET = "test-bucket"


class BoundingBox(TypedDict):
    image_id: str
    x_center: float
    y_center: float
    width: float
    height: float


class Task:
    def __init__(self) -> None:
        session = boto3.session.Session()
        self.s3_client = session.client('s3')
        self.sql_connection = sqlite3.connect("local.db")

    def run(self) -> str:
        """
        Runs the task.

        :return: the S3 path to the output file.
        """
        raise NotImplementedError()
