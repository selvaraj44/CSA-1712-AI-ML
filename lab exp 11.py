
colors = ["Red", "Green", "Blue"]

graph = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

coloring = {}

def solve(region):
    if region == len(graph):
        return True

    regions = list(graph.keys())
    current = regions[region]

    for color in colors:
        if all(coloring.get(neighbor) != color
               for neighbor in graph[current]):
            coloring[current] = color

            if solve(region + 1):
                return True

            del coloring[current]

    return False

if solve(0):
    print("Map Coloring Solution:")
    for region, color in coloring.items():
        print(region, ":", color)
else:
    print("No solution found")
