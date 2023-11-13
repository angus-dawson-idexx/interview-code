from datetime import datetime
from io import BytesIO

import pandas as pd

from common import Task, BUCKET


class DatasetTask(Task):

    def create_dataset(self) -> pd.DataFrame:
        """
        Fetch some images from a database.

        :return: pandas DataFrame with columns `collection_id` and `image_id`, both strings.
        """
        query = f"""
        SELECT collection_id, image_id
        FROM IMAGE
        LIMIT 25;
        """
        result = pd.read_sql(query, self.sql_connection)
        return result

    def run(self) -> str:
        """
        Runs the task.

        :return: the S3 path to the output file.
        """
        now = datetime.now()
        time = now.strftime("%Y%m%d-%H%M%S")
        key = f'dataset_job/{time}.csv'

        df = self.create_dataset()

        file_obj = BytesIO()
        df.to_csv(file_obj, index=False)

        self.s3_client.upload_fileobj(file_obj, BUCKET, key)

        return f"s3://{BUCKET}/{key}"


if __name__ == '__main__':
    task = DatasetTask()
    print(task.run())
