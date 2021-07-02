from app.service import UserService, ListingService



if __name__ == "__main__":
    print("Enter Function Name: ")
    fnc = input().lower()
    if fnc == "r":
        res = UserService().register(fnc)
        print(res)
