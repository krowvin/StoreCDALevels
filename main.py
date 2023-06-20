#!/usr/bin/python3
import requests
import os
import json
from urllib.parse import quote

WEB_DIR = "levels"
ENDPOINT = "https://cwms-data.usace.army.mil/cwms-data/levels"
HEADERS = {
    "User-Agent": "SWT Data Loader",
    "Accept": "application/json;version=2"
}

ELEV_CONS = ".Elev.Inst.0.Top of Conservation"

PROJECTS = ["KEYS"]


def getLevelData(LID: str, office: str):
    """
    Retrieves data for a given location level ID and office using an API endpoint. 

    Args:
        LID (str): The ID of the location level to retrieve data for.
        office (str): The name of the office associated with the location level.

    Returns:
        A list of two elements, where the first element is a string representing the date of the data, and the
        second element is a float representing the value of the data.

    Raises:
        requests.exceptions.RequestException: If an error occurs while making the HTTP request.

    Example:
        >>> getLevelData("TXKT2.Elev.Inst.0.Top of Conservation", "SWF")
        ['2023-04-12', 1234.56]
    """
    #try:
    # Pulling things in metric and then converting because for some reason some of the EN values return incorrectly
    res = requests.get(
        ENDPOINT + f"?name={quote(LID)}&office={office}&format=json", headers=HEADERS, timeout=15)
    values = res.json()["location-levels"]["location-levels"][0]["values"]["segments"][0]["values"]
    values = values[-1]
    return [values[0], values[1]]
    #except Exception as err:
    #    print(f"Failed to get level data for {LID}: Error - ", err)
    #    return [None, None]


def main():
    # Start Here
    for proj in PROJECTS:
        date, value = getLevelData(proj + ELEV_CONS, "SWT")
        print(date, value)

if __name__ == "__main__":
    main()