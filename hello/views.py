import csv
import json
import requests
from django.core.handlers.wsgi import WSGIRequest
from datetime import datetime
from django.http import HttpResponse
from dateutil import parser


def packageHealthView(
    request: WSGIRequest, package_name: str, version: str
) -> HttpResponse:
    package_info = {}

    # Grab license information from the csv file
    with open("hello/files/licenses.csv") as licenses_file:
        lf = list(zip(*csv.reader(licenses_file)))

        packages = lf[0]
        licenses = lf[1]

        for index, package in enumerate(packages):
            package_info[package] = {"name": package, "license": licenses[index]}

    # Add infomration from the vulnerablities csv file
    with open("hello/files/vulnerabilities.csv") as vulnerabilities_file:
        vf = list(zip(*csv.reader(vulnerabilities_file)))

        package_ids = vf[0]
        package_names = vf[1]
        package_version = vf[2]
        package_description = vf[3]
        package_created = vf[4]

        for index, package in enumerate(package_names):
            # Format the create date
            timestamp = int(package_created[index])
            dt = datetime.utcfromtimestamp(timestamp)
            format_time = dt.strftime("%Y-%m-%dT%H:%M:%SZ")

            package_info[package][package_version[index]] = {
                "version": package_version[index],
                "id": package_ids[index],
                "description": package_description[index],
                "created": format_time,
            }

    # Build the response from the data we processed
    # from the csv files
    response = {
        "name": package_name,
        "version": version,
        "license": package_info[package_name]["license"],
        "vulnerabilities": [
            {
                "id": package_info[package_name][version]["id"],
                "description": package_info[package_name][version]["description"],
                "created": package_info[package_name][version]["created"],
            }
        ],
    }

    return HttpResponse(json.dumps(response))


def packageView(request: WSGIRequest, package_name: str) -> HttpResponse:
    # Request package information from npm
    NPM_REGISTRY_BASE_URL = "https://registry.npmjs.org/"
    request_url = f"{NPM_REGISTRY_BASE_URL}{package_name}"

    response = requests.get(request_url)
    data = response.json()

    # Start building the package information we will return
    package_data = {
        "name": package_name,
    }

    # Find the release versions
    releases = []

    versions = data["versions"]

    for v in versions:
        releases.append(v)

    package_data["releases"] = releases

    # Find the most recent release by the time information
    # Do not rely on the latest release flag
    release_info = data.get("time")

    latest_release_date = None
    latest_release = None

    for release, time in release_info.items():
        if release == "modified" or release == "created":
            continue

        release_datetime = parser.isoparse(time)

        if latest_release_date is None:
            latest_release_date = release_datetime
            latest_release = release
            continue

        new_later_than_latest = latest_release_date < release_datetime
        if new_later_than_latest:
            latest_release_date = release_datetime
            latest_release = release
            continue

    package_data["latest"] = latest_release

    return HttpResponse(json.dumps(package_data))
