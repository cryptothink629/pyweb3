from brownie import MyNFT, accounts

from .constants import *


def main():
    acct = accounts.load(LOCAL_ACCOUNT)
    MyNFT.deploy({'from': acct}, publish_source=True)
