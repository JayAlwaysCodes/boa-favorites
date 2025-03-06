import boa
from guide import RPC_URL, ANVIL_KEY
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account

MY_CONTRACT = "0x5FbDB2315678afecb367f032d93F642f64180aa3"

def main():
    rpc = RPC_URL
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    anvil_key = ANVIL_KEY
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa=True)

    favorite_deployer = boa.load_partial("favorites.vy")
    favorites_contract = favorite_deployer.at(MY_CONTRACT)

    favorite_number = favorites_contract.retrieve()
    print(f"Favorite number is: {favorite_number}")

    favorites_contract.store(40)
    favorite_number_updated = favorites_contract.retrieve()
    print(f"Favorite number updated is: {favorite_number_updated}")



if __name__ == "__main__":
    main()