# Survey Fraud Detector


## Pre-requisites

Install Python and pipenv

[Python](https://www.python.org/)
[pipenv](https://pipenv.pypa.io/en/latest/)

Then run:

```
pipenv install
```

## Usage

Make sure the data.csv file in the working directory. 
Its format is:

```
ResponseId,IPAddress,LocationLatitude,LocationLongitude,Q30
R_3J2iBgza8t3kAa5,67.188.221.170,37.7906036376953125,-122.2411956787109375,94606
R_xusAgD4mKk9wZVv,73.162.173.166,37.7906036376953125,-122.2411956787109375,94606
R_eDauZhboR9lVbj3,73.162.173.166,37.7906036376953125,-122.2411956787109375,94606
R_2AR7kyNGVBWOcfA,73.189.15.220,37.7906036376953125,-122.2411956787109375,94606
R_cHeuuHngZ2HX42d,73.222.190.197,37.7906036376953125,-122.2411956787109375,94606
R_1nN3Y8x060v3hKR,73.252.133.137,37.7906036376953125,-122.2411956787109375,94606
```

Make sure you have an up to date `IP2LOCATION-LITE-DB9.BIN` file. The file
is updated every month. You get it by downloading the DB9-lite from here:
https://lite.ip2location.com/ip2location-lite

You'll need to register for a free account.

Then:

```
pipenv run python zipcode_convert.py 
```

The program will generate an itermediate file every 100 records and eventually
a final file called: `converted_GEO_location.csv`
