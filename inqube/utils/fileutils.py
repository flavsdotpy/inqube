import csv
import json

from inqube.exceptions import InvalidFileFormatException


def write_file(output_path: str, data: list[dict], format: str):
    if format == "json":
        write_jsonlines_file(output_path, data)
    elif format == "csv":
        write_csv_file(output_path, data)
    else:
        raise InvalidFileFormatException(f"Invalid file format `{format}`. Valid formats: json, csv")

def write_jsonlines_file(output_path: str, data: list[dict]):
    with open(output_path, "w") as fout:
        for row in data:
            fout.write(json.dumps(row, ensure_ascii=False))
            fout.write("\n")

def write_csv_file(output_path: str, data: list[dict]):
    with open(output_path, "w") as fout:
        writer = csv.DictWriter(fout, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
