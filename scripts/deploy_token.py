from brownie import MyToken, accounts

from .constants import *


def main():
    acct = accounts.load(LOCAL_ACCOUNT)
    MyToken.deploy('MyToken', 'MT', {'from': acct}, publish_source=True)
