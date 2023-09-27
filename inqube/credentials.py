import os


def load_from_env(cred_name):
    return os.getenv(f"INQUBE_CRED_{cred_name}")
