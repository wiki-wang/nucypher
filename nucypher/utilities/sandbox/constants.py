import os

from nucypher.blockchain.eth import constants

TEST_KNOWN_URSULAS_CACHE = {}

TEST_URSULA_STARTING_PORT = 7468

DEFAULT_NUMBER_OF_URSULAS_IN_DEVELOPMENT_NETWORK = 10

DEVELOPMENT_TOKEN_AIRDROP_AMOUNT = 1000000 * int(constants.M)

DEVELOPMENT_ETH_AIRDROP_AMOUNT = 10 ** 6 * 10 ** 18  # wei -> ether

MINERS_ESCROW_DEPLOYMENT_SECRET = os.urandom(constants.DISPATCHER_SECRET_LENGTH)

POLICY_MANAGER_DEPLOYMENT_SECRET = os.urandom(constants.DISPATCHER_SECRET_LENGTH)

TEST_URSULA_INSECURE_DEVELOPMENT_PASSWORD = 'this-is-not-a-secure-password'