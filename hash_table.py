"""
Check if person is in the hash.
"""

voted = {}


def check_voter(name):
    if voted.get(name):
        print("Kick him!")
    else:
        voted[name] = True
        print("Let him vote!")


check_voter('tom')
check_voter('mike')
check_voter('tom')


"""
Check if page URL is store in the hash.
"""

cache = {}


def get_page(url):
    if cache.get(url):
        return cache[url]       # Returns cached data
    else:
        data = get_data_from_server(url)
        cache[url] = data      # Saves this data in your cache first
        return data
