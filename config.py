from environs import Env

#  Берется с https://my.telegram.org/auth

env = Env()
env.read_env()

api_id = env.int("API_ID")
api_hash = env.str("API_HASH")
phone_number = env.str("PHONE")
