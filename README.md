# liczyrzepa

liczyrzepa is a simple command line tool for monitoring prices or other numerical values found on websites that do not provide an API.

## Features

- Scraping numerical values found on a website with specified URL and Xpath,
- Storing name and unit associated with the scraped value,
- Creating price histories that can be saved and loaded,
- Exporting price histories as spreadsheets,
- A simple GUI allowing to perform these operations manually.

## Usage

```
usage: liczyrzepa [-h] [-c] [-i IMAGE] [-g] [-n NAME] [-r READ] [-s SPREADSHEET] [--url URL] [--unit UNIT] [-v] [-w WRITE] [-x XPATH]

options:
  -h, --help            show this help message and exit
  -c, --chart           Show an interactive chart of the price history
  -i IMAGE, --image IMAGE
                        Save a chart of the price history as an image
  -g, --gui             Opens up GUI. Doesn't require any additional arguments
  -n NAME, --name NAME  Name of the monitored value
  -r READ, --read READ  Read the price history from a json file. If specified, overrides --name, --unit, --url and --xpath
  -s SPREADSHEET, --spreadsheet SPREADSHEET
                        Save the price history as a spreadsheet
  --url URL             The URL of a website you want to monitor
  --unit UNIT           The unit of a measured value (e.g. $)
  -v, --value           Prints a current value of an element specified with --xpath found on a website specified with --url.
                        If --write location was specified, this value will be appended to the price history
  -w WRITE, --write WRITE
                        Write the price history as json to a specified location
  -x XPATH, --xpath XPATH
                        The XPath leading to an element you want to monitor
```

## Name origin

Liczyrzepa (Czech: _Krakonoš_) is a Polish name of a mythical spirit of the Giant Mountains (Polish: _Karkonosze_, Czech: _Krkonoše_). While the etymology of Liczyrzepa is not clear, a legend was created to explain the name origin. According to the legend, a princess of the city of Świdnica (German: _Schweidnitz_) was kidnapped by Liczyrzepa, but she managed to escape by distracting him with an order to count turnips in the field. Hence the name Liczyrzepa (_liczyć_ – to count, _rzepa_ – turnip): "one who counts turnips".

The name was picked due to the author's fondness of Karkonosze and the legend itself, as well as a loose reference to the project, which, while doesn't exactly count anything, is close enough to be named this way.
