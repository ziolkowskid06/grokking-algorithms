"""
Figure out the smalest set of stations you can play on to cover all states.
"""

# List of states you want to cover.
states_needed = set({"mt", "wa", "or", "id", "nv",
                     "ut", "ca", "az"})

# List of stations and their range.
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# Hold final set of stations.
final_stations = set()

# Loop until states_needed is empty.
while states_needed:
    # Go through every station and pick the one that cover the most uncovered states.
    best_station = None
    states_covered = set()
    # Check which one is the best station.
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station        # Set intersection
        # Check whether this station covers more states than the current best_station.
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    # Update states needed and add best station.
    states_needed -= states_covered
    final_stations.add(best_station)

# Show solution
print(final_stations)
