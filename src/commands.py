import argparse
from liczyrzepa.types import PriceHistory
from liczyrzepa.web_scraper import WebScraper

parser = argparse.ArgumentParser()
parser.add_argument("--url", help="The URL of a website you want to monitor")
parser.add_argument("--unit", help="The unit of a measured values (e.g. $)")
parser.add_argument(
    "-x", "--xpath", help="The XPath leading to an element you want to monitor"
)
parser.add_argument(
    "-f", "--file", help="Output file to which the presented value will be saved"
)
parser.add_argument(
    "-v",
    "--value",
    help="Prints a current value of an element specified with --xpath found on a website specified with --url",
    action="store_true",
)
parser.add_argument
args = parser.parse_args()

if args.value:
    history = PriceHistory()
    history.create_new_price_record()
    print(history.records[-1].value)
    if args.file:
        history.save_to_file(args.file)
