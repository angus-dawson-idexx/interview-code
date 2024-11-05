import sqlite3
from typing import TypedDict

import pandas as pd


# Here is the external application interface. The implementation details are
# not important; focus on the method signature of `Detector.run_detection`.


class BoundingBox(TypedDict):
    image_id: str
    x_center: float
    y_center: float
    width: float
    height: float


class Detector:
    def run_detection(
        self, collection_id: str, image_ids: list[str]
    ) -> list[BoundingBox]:
        """
        Run the detection application on a list of image IDs from a collection.

        :param collection_id: the ID of the collection
        :param image_ids: the IDs of the images to run detection on
        :return: a list of bounding boxes
        """
        pass  # Pretend this is implemented


# Here is the code for the detection task.
# `DetectionTask.run` is where the core logic is implemented.


class DetectionTask:
    def create_dataset(self) -> pd.DataFrame:
        """
        Fetch some images from a database.

        :return: pandas DataFrame with columns `collection_id` and `image_id`, both strings.
        """
        query = f"""
            SELECT 
                collection_id, 
                image_id
            FROM IMAGE
            LIMIT 25;
        """

        sql_connection = sqlite3.connect("...")
        dataset_df: pd.DataFrame = pd.read_sql(query, sql_connection)
        return dataset_df

    def run(self):
        """
        Run the task.

        Writes `bounding_boxes.csv` with the following columns:

        collection_id: the ID of the collection that the image belongs to
        image_id: the ID of the image the bounding box is in
        x1: x-coordinate of the top left corner (the left edge) of the bounding box
        y1: y-coordinate of the top left corner (the top edge) of the bounding box
        x2: x-coordinate of the bottom right corner (the right edge) of the bounding box
        y2: y-coordinate of the bottom right corner (the bottom edge) of the bounding box
        """

        # Initialize the detector API and load the dataset.
        detector = Detector()
        dataset_df: pd.DataFrame = self.create_dataset()

        # Iterate through the dataset and call the external interface, collecting the results
        bounding_boxes = []
        for collection_id, image_id in dataset_df.itertuples(index=False):
            bounding_boxes.extend(detector.run_detection(collection_id, image_id))

        # Write a CSV with the bounding box data.
        bounding_box_df = pd.DataFrame.from_records(bounding_boxes)
        bounding_box_df.to_csv("bounding_boxes.csv")


if __name__ == "__main__":
    task = DetectionTask()
    task.run()
