import argparse
from chart_creator import ChartCreator
from gui import GUI
from spreadsheet_saver import SpreadsheetSaver
from price_history import PriceHistory


def main():
    parser = construct_argument_parser()
    args = parser.parse_args()

    if args.gui:
        GUI().build()

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
        try:
            history.create_new_price_record()
            print(history.records[-1].value)
            if args.file:
                history.save_to_file(args.file)
        except:
            print(
                "ERROR: Failed to scrape current value. Please verify your url and xpath"
            )
            exit(1)

    if args.write:
        try:
            history.save_to_file(args.write)
        except:
            print(f"ERROR: Failed to save the price history to {args.write}")
            exit(1)

    if args.spreadsheet:
        try:
            SpreadsheetSaver().save_history_to_file(history, args.spreadsheet)
        except:
            print(f"ERROR: Failed to export a spreadsheet to {args.file}")
            exit(1)

    if args.image:
        try:
            ChartCreator(history).save_chart_as_image(args.image)
        except:
            print(f"ERROR: Failed to save a chart to {args.file}")

    if args.chart:
        ChartCreator(history).show_interactive_chart()


def construct_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--chart",
        help="Show an interactive chart of the price history",
        action="store_true",
    )
    parser.add_argument(
        "-i", "--image", help="Save a chart of the price history as an image"
    )
    parser.add_argument(
        "-g",
        "--gui",
        help="Opens up GUI. Doesn't require any additional arguments",
        action="store_true",
    )
    parser.add_argument("-n", "--name", help="Name of the monitored value")
    parser.add_argument(
        "-r",
        "--read",
        help="Read the price history from a json file. If specified, overrides --name, --unit, --url and --xpath",
    )
    parser.add_argument(
        "-s",
        "--spreadsheet",
        help="Save the price history as a spreadsheet",
    )
    parser.add_argument("--url", help="The URL of a website you want to monitor")
    parser.add_argument("--unit", help="The unit of a measured value (e.g. $)")
    parser.add_argument(
        "-v",
        "--value",
        help="""
            Prints a current value of an element specified with --xpath found on a website specified with --url. If --write location was specified, this value will be appended to the price history
            """,
        action="store_true",
    )
    parser.add_argument(
        "-w", "--write", help="Write the price history as json to a specified location"
    )
    parser.add_argument(
        "-x", "--xpath", help="The XPath leading to an element you want to monitor"
    )
    return parser


def create_price_history_from(args) -> PriceHistory:
    history = PriceHistory()
    if args.url:
        history.url = args.url
    if args.xpath:
        history.xpath = args.xpath
    if args.unit:
        history.unit = args.unit
    if args.name:
        history.name = args.name
    return history


if __name__ == "__main__":
    main()
