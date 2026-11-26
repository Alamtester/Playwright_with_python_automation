import json
from pathlib import Path


class TestDataReader:

    def read_json(filename):

        file_path = Path(__file__).parent.parent / "test_data" / filename

        with open(file_path , "r", encoding= "utf-8") as file:
            return json.load(file)

