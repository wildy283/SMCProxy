# SMCProxy | Simple Command Line Proxy
SMCProxy is a simple command line proxy utility that can be used for pentesting and hiding IP address from commands. It also shows lines of progress when a connection is required.

## Requirements
* [Python](https://www.python.org/) 3.6 or higher.

## Library Used
* subprocess
* argparse
* os

## Usage
```
python main.py --host 127.0.0.1 --port 8080 --command curl "https://api.wildy.my.id/ipgeo"
```
For Binary
```
smcproxy --host 127.0.0.1 --port 8080 --command curl "https://api.wildy.my.id/ipgeo"
```


## License
GNU General Public License V3. Read the [LICENSE](LICENSE) for more information.
