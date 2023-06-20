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

