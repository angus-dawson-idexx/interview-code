from common import BoundingBox

class Detector:
    def run_detection(self, collection_id: str, image_ids: list[str]) -> list[BoundingBox]: ...
