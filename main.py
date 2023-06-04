#!/usr/bin/python3

# ---------------------------------------------------------------------------------
# Name         : SMCProxy | Simple Command Line Proxy
# Desc         : Simple Proxy utility can be used for pentesting and hiding
#                IP address from commands. It also shows lines of progress
#                when a connection is required.
# Author       : Wildy Sheverando [ Wildy238 ]
# Date         : 04-04-2023
# License      : GNU General Public License V3
# License Link : https://raw.githubusercontent.com/wildy238/License/main/gplv3.txt
# ---------------------------------------------------------------------------------

# >> Import used library
import subprocess
import argparse
import os

# >> Create args parse object
parser = argparse.ArgumentParser(description='SMCProxy - Simple Command Line Proxy')

# >> Set args argument
parser.add_argument('--host', dest='host', type=str, required=True)
parser.add_argument('--port', dest='port', type=int, required=True)
parser.add_argument('--command', dest='command', type=str, nargs='+', required=True)

# >> Call parse to args and redeclare to string
args = parser.parse_args()
host = args.host
port = args.port
command = " ".join(args.command)
proxys = f"{host}:{port}"

# >> Validate if host, port, command declared
if host and port and command:
    proxies = {
        'http_proxy': proxys,
        'https_proxy': proxys,
        'ftp_proxy': proxys,
        'all_proxy': proxys,
        'socks_proxy': proxys,
        'no_proxy': '127.0.0.1,localhost,local',
    }

    env = {**proxies, **os.environ}
    try:
        subprocess.run(command, check=True, shell=True, env=env)
    except subprocess.CalledProcessError as e:
        print("Program Stopped")
        
# >> Host, port, command not declared
else:
    env = os.environ
    try:
        subprocess.run(command, check=True, shell=True, env=env)
    except subprocess.CalledProcessError as e:
        print("Program Stopped")
