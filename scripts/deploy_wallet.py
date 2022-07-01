from brownie import Wallet, accounts

from .constants import *


def main():
    acct = accounts.load(LOCAL_ACCOUNT)
    Wallet.deploy({'from': acct}, publish_source=True)
