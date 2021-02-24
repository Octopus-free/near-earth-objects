"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from helpers import datetime_to_str


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    # TODO: Write the results to a CSV file, following the specification in the instructions.

    with open(filename, 'w') as csv_to_write:
        csv_writer = csv.DictWriter(csv_to_write, fieldnames=fieldnames)
        csv_writer.writeheader()

        for each_approach in results:
            csv_writer.writerow({
                'datetime_utc': datetime_to_str(each_approach.time),
                'distance_au': each_approach.distance,
                'velocity_km_s': each_approach.velocity,
                'designation': each_approach.designation,
                'name': each_approach.neo.name,
                'diameter_km': each_approach.neo.diameter,
                'potentially_hazardous': str(each_approach.neo.hazardous)})


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    dict_for_json = list()

    for each_approach in results:
        row_for_json = {
            'datetime_utc': datetime_to_str(each_approach.time),
            'distance_au': each_approach.distance,
            'velocity_km_s': each_approach.velocity,
            'neo': {
                'designation': each_approach.designation,
                'name': each_approach.neo.name,
                'diameter_km': each_approach.neo.diameter,
                'potentially_hazardous': each_approach.neo.hazardous
            }
        }
        dict_for_json.append(row_for_json)

    with open(filename, 'w') as json_to_write:
        json_to_write.write(json.dumps(dict_for_json, indent=4))
