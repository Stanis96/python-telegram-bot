import environ


env = environ.Env()
environ.Env.read_env(str(".env"))

TOKEN = env("TOKEN")

URL_API = env("URL_API")

BARS = ["/bars/"]
BEERS = ["/beers/"]

EMOJI = ["\U0001F37B", "\U0001F51E", "\U0001F614"]
