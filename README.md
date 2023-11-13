## Annotation Pipeline: Detection Task

We are building a pipeline to provide our annotators with detected objects on an image
that they need to label. Each detected object will be indicated by a bounding box on the image.

Each image, denoted by "image_id", is within a collection of images, denoted by "collection_id". 
Each collection contains several images. 

The first stage of our pipeline, the dataset task, fetches 25 image IDs from a database 
and exports them as a CSV file in an S3 bucket. This is implemented in `dataset_task.py`.

We have an application that runs a bounding box detection algorithm on these images.
This application's interface can be found in `detector.pyi`.

The rest of our pipeline needs to receive a CSV file with rows representing the bounding
boxes detected by this algorithm. The CSV file should have the following columns:

```
collection_id: the ID of the collection that the image belongs to
image_id: the ID of the image the bounding box is in
x1: x-coordinate of the top left corner (the left edge) of the bounding box
y1: y-coordinate of the top left corner (the top edge) of the bounding box
x2: x-coordinate of the bottom right corner (the right edge) of the bounding box
y2: y-coordinate of the bottom right corner (the bottom edge) of the bounding box
```

This file should be exported to a CSV file in the same bucket as the dataset CSV.

Your assignment is to implement logic in `detection_task.py` to achieve this.
