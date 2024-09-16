# Birdnet-labeller

A reasonably simple script that generates a list of bird calls detected with
birdnetlib, nicely formatted for use with Audacity.


# Install

For now, please install from GitHub (only tested on Linux, but in theory might work elsewhere).

```
pip install git+https://github.com/kdm9/birdnet-labeller.git#egg=birdnet-labeller
```

Ideally, do this within a virtual environment, or with pipx.

# Usage

```
$ birdnet-labeller --help

usage: birdnet-labeller [-h] [--output OUTPUT] [--longitude LONGITUDE] [--latitude LATITUDE] [--date DATE] [--min-confidence MIN_CONFIDENCE] input

positional arguments:
  input

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output labels.txt file for Audacity
  --longitude LONGITUDE, -x LONGITUDE, --lon LONGITUDE
                        Observation longitude (default: Tübingen-ish)
  --latitude LATITUDE, -y LATITUDE, --lat LATITUDE
                        Observation latitude (default: Tübingen-ish)
  --date DATE, -d DATE  Observation date/time
  --min-confidence MIN_CONFIDENCE, -c MIN_CONFIDENCE
                        Minimum model confidence to report

```

For example, from recent recording: `birdnet-labeller -o 240816_001.labels.txt
--date 2024-08-16 -x 9 -y 48 -c 0.3 240816_001.WAV`, which generates
a `.labels.txt` file corresponding to a WAV straight from a field recording.
Then, in Audacity: File -> Import -> Audio -> Select the wav file, and File ->
Import -> Labels -> Select the labels.txt file. You should see the labels pop
up at the correct times. 	
