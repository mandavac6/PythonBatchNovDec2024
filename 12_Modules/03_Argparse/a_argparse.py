"""
Purpose: importance and usage of argparse
"""


# # Method 1: hard- coding
# user_name = 'Tom'
# password = 'brady@123'
# server_name = 'qb.tampabay.com'
'''
 $ python a_argparse.py 

The server login details are:
    USER NAME   : Tom
    PASSWORD    : brady@123
    SERVER NAME : qb.tampabay.com
    '''


# # Method 2: input() - run time
# user_name = input('Enter username:')
# password = input('Enter password:')
# server_name = input('Enter server name:')
'''
 $ python a_argparse.py 
Enter username:tom
Enter password:brady@123
Enter server name:qb.tb.com

The server login details are:
    USER NAME   : tom
    PASSWORD    : brady@123
    SERVER NAME : qb.tb.com'''


# # Method 3: input() - run time with getpass for password
# import getpass
# user_name = input('Enter username:')
# password = getpass.getpass('Enter password:')
# server_name = input('Enter server name:')

'''
 $ python a_argparse.py 
Enter username:tb
Enter password:
Enter server name:qb@tb.com

The server login details are:
    USER NAME   : tb
    PASSWORD    : bradt34@12
    SERVER NAME : qb@tb.com
'''


# # Method 4: sys.argv
# import sys

# if len(sys.argv) != 4:
#     print('Help:')
#     print(f'python {__file__} username password server_fqdn')
#     sys.exit(1)

# user_name = sys.argv[1]
# password = sys.argv[2]
# server_name = sys.argv[3]
'''
 $ python a_argparse.py 
Help:
python /workspaces/PythonBatchNovDec2024/12_Modules/03_Argparse/a_argparse.py username password server_fqdn
 $ python a_argparse.py abv 123@123 qb.com

The server login details are:
    USER NAME   : abv
    PASSWORD    : 123@123
'''

# Method 5: argparse
import argparse

parser = argparse.ArgumentParser(
    description="Details to login to server", 
    epilog="-----Please follow help doc ----"
)
# description: for the text that is shown before the help text
# epilog: for the text shown after the help text

parser.add_argument("-u", "--username", help="login user name", type=str, required=True)
parser.add_argument("-p", "--password", help="login user password", type=str, required=True)
parser.add_argument("-s","--servername", help="server name", type=str, required=False, default="www.google.com",)

args = parser.parse_args()

user_name = args.username
password = args.password
server_name = args.servername

'''

 $ python a_argparse.py
usage: a_argparse.py [-h] -u USERNAME -p PASSWORD [-s SERVERNAME]
a_argparse.py: error: the following arguments are required: -u/--username, -p/--password
 $ python a_argparse.py -h
usage: a_argparse.py [-h] -u USERNAME -p PASSWORD [-s SERVERNAME]

Details to login to server

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        login user name
  -p PASSWORD, --password PASSWORD
                        login user password
  -s SERVERNAME, --servername SERVERNAME
                        server name

-----Please follow help doc ----
 $ python a_argparse.py -u tom -p brady@123

The server login details are:
    USER NAME   : tom
    PASSWORD    : brady@123
    SERVER NAME : www.google.com

'''

print(
    f"""
The server login details are:
    USER NAME   : {user_name}
    PASSWORD    : {password}
    SERVER NAME : {server_name}
"""
)