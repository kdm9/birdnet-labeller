#!/home/kevin/.cache/venvs/audioprocessing/bin/python3
from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
import dateutil.parser

from datetime import datetime
import argparse
import sys
from sys import stdin, stdout, stderr
from pathlib import Path
from collections import Counter

def parse_datetime(datestr):
    return dateutil.parser.parse(datestring)

def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", "-o",  type=argparse.FileType("w"), default=stdout,
                    help="Output labels.txt file for Audacity")
    ap.add_argument("--longitude", "-x", "--lon", dest="longitude", type=float, default=9,
                    help="Observation longitude (default: Tübingen-ish)")
    ap.add_argument("--latitude", "-y", "--lat", dest="latitude", type=float, default=48,
                    help="Observation latitude (default: Tübingen-ish)")
    ap.add_argument("--date", "-d", type=parse_datetime, default=datetime.now(),
                    help="Observation date/time")
    ap.add_argument("--min-confidence", "-c", type=float, default=0.2,
                    help="Minimum model confidence to report")
    ap.add_argument("input", type=Path)
    args = ap.parse_args(argv)

    print("Analysing recording... ", file=stderr)
    analyzer = Analyzer()
    recording = Recording(analyzer, args.input, lat=args.latitude, lon=args.longitude, date=args.date, min_conf=args.min_confidence)
    stderr.flush()
    recording.analyze()

    print("Finished! Most common detections are:", file=stderr)
    histo = Counter([x.common_name for x in recording.detection_list])
    for sp, ct in histo.most_common(50):
        print("   ", sp.rjust(30), str(ct).rjust(5), file=stderr)

    for det in recording.detection_list:
        msg = f"{det.common_name} ({det.scientific_name}); conf={det.confidence*100:0.0f}%"
        print(det.start_time, det.end_time, msg, sep="\t", file=args.output)


if __name__ == "__main__":
    main()
    


