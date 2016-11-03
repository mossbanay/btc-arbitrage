from api.api import MarketAPI

def main():
    api = MarketAPI()
    print(api.get_bids())

if __name__ == '__main__':
    main()
