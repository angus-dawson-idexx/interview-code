from argparse import ArgumentParser

import pandas as pd

from common import Task


class DetectionTask(Task):

    def load_dataset_csv_data(self) -> pd.DataFrame:
        """
        Loads data from a CSV file in S3 specified as
        --dataset-csv-path into a pandas DataFrame.

        :return: a DataFrame with the loaded CSV data
        """
        p = ArgumentParser()
        p.add_argument("--dataset-csv-path", required=False, type=str)
        namespace = p.parse_args()
        data = self.load_csv_from_s3(namespace.sampler_csv_path)
        return data

    def load_csv_from_s3(self, csv_path: str) -> pd.DataFrame:
        """
        Given a path to a .csv file in S3 ("s3://<bucket>/<key>"),
        loads the CSV file as a pandas DataFrame.

        :param csv_path: the URI of the CSV file in S3
        :return: a DataFrame with the loaded CSV data
        """
        raise NotImplementedError()

    def run(self) -> str:
        """
        Runs the task.

        :return: the S3 path to the output file.
        """
        raise NotImplementedError()


if __name__ == '__main__':
    task = DetectionTask()
    print(task.run())
