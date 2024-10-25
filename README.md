```
usage: liczyrzepa [-h] [-c] [-i IMAGE] [-n NAME] [-r READ] [-s SPREADSHEET] [--url URL] [--unit UNIT] [-v] [-w WRITE] [-x XPATH]

options:
  -h, --help            show this help message and exit
  -c, --chart           Show an interactive chart of the price history
  -i IMAGE, --image IMAGE
                        Save a chart of the price history as an image
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
