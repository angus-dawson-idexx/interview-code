from argparse import ArgumentParser
from typing import TypedDict

import boto3
import pandas as pd


BUCKET = "some-bucket"


class BoundingBox(TypedDict):
    image_id: str
    x_center: float
    y_center: float
    width: float
    height: float


class Detector:

    def run_detection(self, collection_id: str, image_ids: list[str]) -> list[BoundingBox]:
        """
        Run the detection application on a list of image IDs from a collection.

        :param collection_id: the ID of the collection
        :param image_ids: the IDs of the images to run detection on
        :return: a list of bounding boxes
        """
        pass  # Pretend this is implemented


class DetectionTask:

    def __init__(self) -> None:
        session = boto3.session.Session()
        self.s3_client = session.client('s3')

    def load_dataset_csv_data(self) -> pd.DataFrame:
        """
        Loads data from a CSV file in S3 specified as
        --dataset-csv-path into a pandas DataFrame.

        :return: a DataFrame with the loaded CSV data
        """
        p = ArgumentParser()
        p.add_argument("--dataset-csv-path", required=False, type=str)
        dataset_csv_path = p.parse_args().dataset_csv_path

        dataset_df: pd.DataFrame = ...  # load CSV from s3 into a DataFrame

        return dataset_df

    def run(self) -> str:
        """
        Runs the task.

        :return: the S3 path to the output file.
        """
        raise NotImplementedError()


if __name__ == '__main__':
    task = DetectionTask()
    print(task.run())
