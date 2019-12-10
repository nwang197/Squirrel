# Squirrel Tracker
This is a web app called "Squirrel Tracker" that keeps track of squirrel sightings and activities in Central Park, New York City. It includes:

* 100 locations of recorded squirrel sightings pinpointed on the OpenStreet map
* Listing of all squirrel ID's on record
* Page to add new squirrel sightings information
* Page to edit existing squirrel sightings information
* Stats about 5 attributes of squirrel sightings

## Squirrel Census Data
The original file of the squirrel sightings data is available for download [here](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw).

To import a CSV file of squirrel census data from the command line, use the command

```
$ python manage.py import_squirrel_data /path/to/file.csv
```

To export a CSV file of squirrel census data from the command line, use the command

```
$ python manage.py export_squirrel_data /path/to/file.csv
```

## Project Group Name and Section
Project Group 20, Section 2

## UNI of Team Members
UNIs: [nw2432, wc2695]

## Links to the Server
* [Map](https://nuoya-project-4501.appspot.com/map/)
* [All Sightings](https://nuoya-project-4501.appspot.com/sightings/)
* [Add](https://nuoya-project-4501.appspot.com/sightings/add)
* [Stats](https://nuoya-project-4501.appspot.com/sightings/stats/)
* Edit: access by clicking on each squirrel ID from "All Sightings" page

## A Note to the Grader
Wenxin’s coupon for the Google Cloud Virtual Machine expired when we first started the project. Nuoya wrote the files for the map, import, and export, while Wenxin was responsible for the sightings part. But later we did most of the debugging and deploying work together on Nuoya’s machine. This explains the uneven contributions shown on GitHub.
