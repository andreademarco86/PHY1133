# ============================================================================
# PHY1133: Python for Physicists - TSP Flight Route Assignment
# Complete Model Solution
# ============================================================================

import math
import itertools
import matplotlib.pyplot as plt

# ============================================================================
# TASK 1: Data and Helpers
# ============================================================================

# Airport data: (name, latitude in degrees, longitude in degrees)
airports = [
    ("Malta Int. (MLA)",     35.857, 14.477),
    ("Catania (CTA)",        37.469, 15.066),
    ("Palermo (PMO)",        38.176, 13.103),
    ("Rome Fiumicino (FCO)", 41.800, 12.238),
    ("Athens (ATH)",         37.936, 23.947),
    ("Naples (NAP)",         40.886, 14.290),
    ("Tunis (TUN)",          36.851, 10.228),
    ("Algiers (ALG)",        36.691,  3.215),
    ("Barcelona (BCN)",      41.297,  2.078),
    ("Nice (NCE)",           43.665,  7.215),
]

def get_coordinates(airports, index):
    """
    Helper function to extract coordinates from airport data by index.

    Parameters:
        airports: List of tuples (name, lat, lon)
        index: Integer index of the airport

    Returns:
        Tuple (lat, lon) in degrees
    """
    return (airports[index][1], airports[index][2])


# ============================================================================
# TASK 2: Distance Functions
# ============================================================================

def deg2rad(deg):
    """
    Convert degrees to radians.

    Parameters:
        deg: Angle in degrees

    Returns:
        Angle in radians
    """
    return deg * math.pi / 180.0


def euclidean_distance(p, q, R=6371.0):
    """
    Calculate local flat Euclidean distance between two points on Earth.
    This is an approximation valid for small regions.

    Parameters:
        p: Tuple (lat_deg, lon_deg) for first point
        q: Tuple (lat_deg, lon_deg) for second point
        R: Earth's radius in km (default 6371.0)

    Returns:
        Distance in kilometres
    """
    lat1, lon1 = p
    lat2, lon2 = q

    # Calculate differences
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Mean latitude in radians
    phi_bar = deg2rad((lat1 + lat2) / 2.0)

    # Conversion factors from degrees to km
    k_lat = math.pi * R / 180.0
    k_lon = k_lat * math.cos(phi_bar)

    # Euclidean distance in km
    distance = math.sqrt((k_lon * delta_lon)**2 + (k_lat * delta_lat)**2)

    return distance


def haversine_distance(p, q, R=6371.0):
    """
    Calculate great-circle distance between two points on Earth using
    the Haversine formula.

    Parameters:
        p: Tuple (lat_deg, lon_deg) for first point
        q: Tuple (lat_deg, lon_deg) for second point
        R: Earth's radius in km (default 6371.0)

    Returns:
        Distance in kilometres along Earth's surface
    """
    lat1, lon1 = p
    lat2, lon2 = q

    # Convert to radians
    lat1_rad = deg2rad(lat1)
    lon1_rad = deg2rad(lon1)
    lat2_rad = deg2rad(lat2)
    lon2_rad = deg2rad(lon2)

    # Calculate differences
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Haversine formula
    a = math.sin(delta_lat / 2.0)**2 + \
        math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2.0)**2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c

    return distance


def route_length(route, airports, distance_fn=haversine_distance):
    """
    Calculate the total distance of a route through multiple airports.

    Parameters:
        route: List of airport indices, e.g., [0, 3, 5, 7, 0]
        airports: List of airport data tuples
        distance_fn: Distance function to use (default: haversine_distance)

    Returns:
        Total distance in kilometres
    """
    total_distance = 0.0

    # Loop through consecutive pairs in the route
    for i in range(len(route) - 1):
        idx1 = route[i]
        idx2 = route[i + 1]

        # Get coordinates for both airports
        coord1 = get_coordinates(airports, idx1)
        coord2 = get_coordinates(airports, idx2)

        # Add distance between consecutive airports
        total_distance += distance_fn(coord1, coord2)

    return total_distance


# ============================================================================
# TASK 3: TSP Algorithms
# ============================================================================

def brute_force_route(airports, start_index=0):
    """
    Find the optimal TSP route using exhaustive search (brute force).
    This guarantees the shortest route but is slow for large problems.

    Parameters:
        airports: List of airport data tuples
        start_index: Index of the starting airport (default: 0)

    Returns:
        Tuple (best_route, best_length) where:
            - best_route is a list of indices forming the optimal tour
            - best_length is the total distance in km
    """
    # Generate list of all other airports (excluding start)
    n = len(airports)
    others = [i for i in range(n) if i != start_index]

    # Initialize best solution
    best_route = None
    best_length = float('inf')

    # Try all permutations of the other airports
    for perm in itertools.permutations(others):
        # Build complete route: start -> permutation -> start
        route = [start_index] + list(perm) + [start_index]

        # Calculate length using Haversine distance
        length = route_length(route, airports, haversine_distance)

        # Update best if this is shorter
        if length < best_length:
            best_length = length
            best_route = route

    return best_route, best_length


def nearest_neighbour_route(airports, start_index=0):
    """
    Find a TSP route using the nearest neighbour heuristic.
    This is fast but may not find the optimal solution.

    Parameters:
        airports: List of airport data tuples
        start_index: Index of the starting airport (default: 0)

    Returns:
        List of indices forming the route
    """
    # Initialize
    current = start_index
    route = [current]

    # Create set of unvisited airports (excluding start)
    n = len(airports)
    unvisited = set(range(n))
    unvisited.remove(start_index)

    # Greedily visit nearest unvisited airport at each step
    while unvisited:
        current_coords = get_coordinates(airports, current)

        # Find nearest unvisited airport
        nearest = None
        min_distance = float('inf')

        for candidate in unvisited:
            candidate_coords = get_coordinates(airports, candidate)
            distance = haversine_distance(current_coords, candidate_coords)

            if distance < min_distance:
                min_distance = distance
                nearest = candidate

        # Move to nearest airport
        route.append(nearest)
        unvisited.remove(nearest)
        current = nearest

    # Return to starting airport to close the loop
    route.append(start_index)

    return route


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("TSP FLIGHT ROUTE PLANNING - Mediterranean Airports")
    print("=" * 70)

    # Run brute force algorithm
    print("\nRunning brute force algorithm (exact solution)...")
    route_exact, length_exact = brute_force_route(airports, start_index=0)
    print(f"Brute force complete!")
    print(f"  Optimal route: {route_exact}")
    print(f"  Total distance: {length_exact:.2f} km")

    # Run nearest neighbour algorithm
    print("\nRunning nearest neighbour heuristic...")
    route_nn = nearest_neighbour_route(airports, start_index=0)
    length_nn = route_length(route_nn, airports, haversine_distance)
    print(f"Nearest neighbour complete!")
    print(f"  Heuristic route: {route_nn}")
    print(f"  Total distance: {length_nn:.2f} km")

    # Compare results
    print("\n" + "=" * 70)
    print("COMPARISON")
    print("=" * 70)
    print(f"Brute force distance:       {length_exact:.2f} km")
    print(f"Nearest neighbour distance: {length_nn:.2f} km")
    difference = length_nn - length_exact
    percent_diff = (difference / length_exact) * 100
    print(f"Difference:                 {difference:.2f} km ({percent_diff:.1f}% longer)")

    # Print route details for both
    print("\n" + "=" * 70)
    print("ROUTE DETAILS")
    print("=" * 70)
    print("\nOptimal route (Brute Force):")
    for i, idx in enumerate(route_exact):
        print(f"  {i}. {airports[idx][0]}")

    print("\nNearest Neighbour route:")
    for i, idx in enumerate(route_nn):
        print(f"  {i}. {airports[idx][0]}")

    # ========================================================================
    # VISUALIZATION
    # ========================================================================

    print("\n" + "=" * 70)
    print("CREATING VISUALIZATION")
    print("=" * 70)

    # Create a figure with two subplots side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # Extract coordinates for all airports
    lats = [airport[1] for airport in airports]
    lons = [airport[2] for airport in airports]
    names = [airport[0] for airport in airports]

    # ---- Plot 1: Brute Force (Optimal) Route ----
    ax1.set_title('Optimal Route (Brute Force)\nDistance: {:.2f} km'.format(length_exact),
                  fontsize=14, fontweight='bold')
    ax1.set_xlabel('Longitude (degrees)', fontsize=12)
    ax1.set_ylabel('Latitude (degrees)', fontsize=12)
    ax1.grid(True, alpha=0.3)

    # Plot all airports as points
    ax1.scatter(lons, lats, s=100, c='red', zorder=5, edgecolors='black', linewidths=1.5)

    # Add labels for each airport
    for i, name in enumerate(names):
        ax1.annotate(name, (lons[i], lats[i]),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8, fontweight='bold')

    # Plot the optimal route
    route_lons_exact = [airports[idx][2] for idx in route_exact]
    route_lats_exact = [airports[idx][1] for idx in route_exact]
    ax1.plot(route_lons_exact, route_lats_exact, 'b-', linewidth=2, alpha=0.7, label='Optimal route')

    # Highlight start/end point (Malta)
    ax1.scatter([airports[0][2]], [airports[0][1]], s=200, c='green',
               marker='*', zorder=10, edgecolors='black', linewidths=2, label='Start/End')

    ax1.legend(loc='best')

    # ---- Plot 2: Nearest Neighbour Route ----
    ax2.set_title('Nearest Neighbour Route (Heuristic)\nDistance: {:.2f} km'.format(length_nn),
                  fontsize=14, fontweight='bold')
    ax2.set_xlabel('Longitude (degrees)', fontsize=12)
    ax2.set_ylabel('Latitude (degrees)', fontsize=12)
    ax2.grid(True, alpha=0.3)

    # Plot all airports as points
    ax2.scatter(lons, lats, s=100, c='red', zorder=5, edgecolors='black', linewidths=1.5)

    # Add labels for each airport
    for i, name in enumerate(names):
        ax2.annotate(name, (lons[i], lats[i]),
                    xytext=(5, 5), textcoords='offset points',
                    fontsize=8, fontweight='bold')

    # Plot the nearest neighbour route
    route_lons_nn = [airports[idx][2] for idx in route_nn]
    route_lats_nn = [airports[idx][1] for idx in route_nn]
    ax2.plot(route_lons_nn, route_lats_nn, 'purple', linewidth=2, alpha=0.7, label='NN route')

    # Highlight start/end point (Malta)
    ax2.scatter([airports[0][2]], [airports[0][1]], s=200, c='green',
               marker='*', zorder=10, edgecolors='black', linewidths=2, label='Start/End')

    ax2.legend(loc='best')

    plt.tight_layout()
    plt.savefig('tsp_routes_comparison.png', dpi=150, bbox_inches='tight')
    print("\nVisualization saved as 'tsp_routes_comparison.png'")
    plt.show()

    # ========================================================================
    # OPTIONAL: Compare Euclidean vs Haversine distances
    # ========================================================================

    print("\n" + "=" * 70)
    print("OPTIONAL: Distance Metric Comparison")
    print("=" * 70)

    # Calculate optimal route length using Euclidean distance
    length_exact_euclidean = route_length(route_exact, airports, euclidean_distance)
    print(f"\nOptimal route using different distance metrics:")
    print(f"  Haversine distance:  {length_exact:.2f} km")
    print(f"  Euclidean distance:  {length_exact_euclidean:.2f} km")
    print(f"  Difference:          {abs(length_exact - length_exact_euclidean):.2f} km")

    # Test a few point-to-point distances
    print("\n" + "-" * 70)
    print("Sample point-to-point distance comparisons:")
    print("-" * 70)

    test_pairs = [
        (0, 1, "Malta -> Catania"),
        (0, 4, "Malta -> Athens"),
        (7, 8, "Algiers -> Barcelona"),
    ]

    for idx1, idx2, description in test_pairs:
        p1 = get_coordinates(airports, idx1)
        p2 = get_coordinates(airports, idx2)

        d_haversine = haversine_distance(p1, p2)
        d_euclidean = euclidean_distance(p1, p2)

        print(f"{description}:")
        print(f"  Haversine: {d_haversine:.2f} km | Euclidean: {d_euclidean:.2f} km | "
              f"Diff: {abs(d_haversine - d_euclidean):.2f} km")

    print("\n" + "=" * 70)
    print("COMPLETE MODEL SOLUTION - ALL TASKS FINISHED")
    print("=" * 70)