import os
import json

from unipath import Path

def setup_env():
    env = Path(__file__).ancestor(2).child('.env.json')
    if env.isfile():
        with open(env) as data_file:
            env_variables = json.load(data_file)
            for env_key, env_value in env_variables.items():
                os.environ[env_key] = env_value
