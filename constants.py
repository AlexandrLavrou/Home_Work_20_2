import os

PWD_ALGO = "sha256"
PWD_HASH_SALT = os.getenv("PWD_HASH_SALT", "").encode()  # will load from env
PWD_HASH_ITERATIONS = int(os.getenv("PWD_HASH_ITERATIONS", "100000"))

# JWT tokens
TOKEN_ALGO = "HS256"
TOKEN_SECRET = os.getenv("TOKEN_SECRET", "changeme")
