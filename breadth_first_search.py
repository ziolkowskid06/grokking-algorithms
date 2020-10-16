"""
Find the mango seller, checking each friend.
"""

from collections import deque

# A map of the neighbors
graph = {}
graph["you"] = ["alice", 'bob', 'claire']
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    """Person whose last letter is -m is a mango seller"""
    return name[-1] == 'm'


def search(name):
    search_queue = deque()          # Creates a new queue
    search_queue += graph[name]     # Adds all neighbor to the queue
    searched = []       # Track which people have been searched
    # While queue isn't empty
    while search_queue:
        # Grabs the first person off the queue
        person = search_queue.popleft()
        # Checks if peson was searched
        if not person in searched:
            # Checks whether the person is a mango seller
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                # Adds all of this person's friends to the queue
                search_queue += graph[person]
                searched.append(person)
    return False    # No one in the queue was a mango seller


# Show results
search("you")
