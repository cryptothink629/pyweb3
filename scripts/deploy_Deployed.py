from brownie import Deployed, accounts

from .constants import *


def main():
    acct = accounts.load(LOCAL_ACCOUNT)
    Deployed.deploy(1, {'from': acct}, publish_source=True)
