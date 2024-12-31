"""
Purpose: dotenv module

    pip install -U python-dotenv --user

"""
import os
from pathlib import Path  # Python 3.6+ only

import dotenv

print(f"{dotenv.find_dotenv() =}")
# recognizes .env in current directory, if not specified

# To load the .env file
# dotenv.load_dotenv()
dotenv.load_dotenv(verbose=True)
# dotenv.load_dotenv(dotenv.find_dotenv())

# # # OR, explicitly providing path to '.env'
# env_path = Path(".") / ".env"
# dotenv.load_dotenv(dotenv_path=env_path)

# Accessing the .env file keys
print(
    f"""
    {os.getenv('REDIS_ADDRESS')   =}
    {os.getenv('MEANING_OF_LIFE') =}
    {os.getenv('MULTILINE_VAR')   =}

    {os.getenv('S3_BUCKET')       =}
    {os.getenv('SECRET_KEY')      =}

    {os.getenv('server')          =}
    {os.getenv('port')            =}
    {os.getenv('url_format')      =}
    {os.getenv('url')             =}
"""
)
# NOTE:
# 1. load_dotenv does not override existing System environment variables.
# 2. To override, pass override=True to load_dotenv()

# (.venv) .venv@mandavac6 ➜ /workspaces/PythonBatchNovDec2024/12_Modules/13_dotenv_module (class24) $ python a_dotenv_module.py 
# dotenv.find_dotenv() ='/workspaces/PythonBatchNovDec2024/.env'

#     os.getenv('REDIS_ADDRESS')   =None
#     os.getenv('MEANING_OF_LIFE') =None
#     os.getenv('MULTILINE_VAR')   =None

#     os.getenv('S3_BUCKET')       =None
#     os.getenv('SECRET_KEY')      =None

#     os.getenv('server')          ='ahhudbeubi.hduegue.78uejj.com'
#     os.getenv('port')            ='3003'
#     os.getenv('url_format')      ='random'
#     os.getenv('url')             ='tb.qb.com'