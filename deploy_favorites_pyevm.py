import boa

def main():
    print("Let's read in the Vyper code and deploy it!")
    favorites_contract = boa.load("favorites.vy")
    
    starting_favorite_number = favorites_contract.retrieve()
    print(f"The Starting favorite number is: {starting_favorite_number}")

    favorites_contract.store(50)
    ending_favorites_number = favorites_contract.retrieve()
    print(f"The ending favorite number is: {ending_favorites_number}")

if __name__ == "__main__":
    main()