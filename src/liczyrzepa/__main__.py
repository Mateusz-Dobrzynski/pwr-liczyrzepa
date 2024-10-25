import argparse
from chart_creator import ChartCreator
from spreadsheet_saver import SpreadsheetSaver
from price_history import PriceHistory


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="The URL of a website you want to monitor")
    parser.add_argument("--unit", help="The unit of a measured value (e.g. $)")
    parser.add_argument(
        "-x", "--xpath", help="The XPath leading to an element you want to monitor"
    )
    parser.add_argument(
        "-f", "--file", help="Output file to which the price history will be saved"
    )
    parser.add_argument(
        "-v",
        "--value",
        help="Prints a current value of an element specified with --xpath found on a website specified with --url",
        action="store_true",
    )
    parser.add_argument(
        "-i", "--image", help="Save a chart of the price history as an image"
    )
    parser.add_argument(
        "-c",
        "--chart",
        help="Show an interactive chart of the price history",
        action="store_true",
    )
    parser.add_argument(
        "-s",
        "--spreadsheet",
        help="Path of a spreadsheet file to which the price history will be exported",
    )
    parser.add_argument("-r", "--read", help="Path of a price history input file")
    parser.add_argument
    args = parser.parse_args()

    if not args.read:
        history = create_price_history_from(args)
    else:
        history = PriceHistory(args.read)

    if args.value:
        if not args.read and (not args.url or not args.xpath):
            print(
                'URL and Xpath are required to determine a value. Use "liczyrzepa --help" for more information'
            )
            exit(1)
        history.create_new_price_record()
        print(history.records[-1].value)
        if args.file:
            history.save_to_file(args.file)

    if args.file:
        history.save_to_file(args.file)

    if args.spreadsheet:
        SpreadsheetSaver().save_history_to_file(history, args.spreadsheet)

    if args.image:
        ChartCreator(history).save_chart_as_image(args.image)

    if args.chart:
        ChartCreator(history).show_interactive_chart()


def create_price_history_from(args) -> PriceHistory:
    history = PriceHistory()
    if args.url:
        history.url = args.url
    if args.xpath:
        history.xpath = args.xpath
    if args.unit:
        history.unit = args.unit
    return history


if __name__ == "__main__":
    main()
