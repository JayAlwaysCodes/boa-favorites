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

    # Deploy the contract
    favorites_contract = boa.load("favorites.vy")

    # Call set_bool() to update my_bool to True
    print("Setting boolean value to True...")
    favorites_contract.set_bool()

    # Now call get_bool() to retrieve the updated value
    print("Getting boolean value...")
    bool_value = favorites_contract.get_bool()
    print(f"Boolean Value: {bool_value}")

if __name__ == '__main__':
    main()