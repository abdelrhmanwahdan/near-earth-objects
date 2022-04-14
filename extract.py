"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
row, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, "r") as f:
        data = csv.DictReader(f)
        neos = []
        neo_dict = {}
        for row in data:
            neo_dict["name"] = row["name"] if row["name"] else None
            neo_dict["diameter"] = float(row["diameter"]) if row["diameter"] else None
            neo_dict["hazardous"] = False if row["pha"] in ["", "N"] else True
            neo_dict["designation"] = row["pdes"]
            try:
                neo = NearEarthObject(**neo_dict)
            except Exception as e:
                print(e)
            else:
                neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.
    
    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, "r") as f:
        approaches_data = json.load(f)
        keys = ["designation", "time", "distance", "velocity"]
        data = []
        for d in approaches_data["data"]:
            row = [d[0], d[3], float(d[4]), float(d[7])]
            data.append(row)

        approaches_dict = [dict(zip(keys, d)) for d in data]
        approaches = []
        for row in approaches_dict:
            try:
                approach = CloseApproach(**row)
            except Exception as e:
                print(e)
            else:
                approaches.append(approach)
    return approaches
