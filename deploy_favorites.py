import boa
from guide import RPC_URL, ANVIL_KEY
from boa.network import NetworkEnv, EthereumRPC
from eth_account import Account

def main():
    rpc = RPC_URL
    env = NetworkEnv(EthereumRPC(rpc))
    boa.set_env(env)

    anvil_key = ANVIL_KEY
    my_account = Account.from_key(anvil_key)
    boa.env.add_account(my_account, force_eoa=True)

    favorites_contract = boa.load("favorites.vy")

    print("Storing a person...")
    favorites_contract.add_person("Alice", 20)

    person_data = favorites_contract.list_of_people(0)
    print(f"Person: {person_data}")

    



if __name__ == "__main__":
    main()