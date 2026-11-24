# ============================================================================
# PHY1133: Python for Physicists - How Far Can You Kick It?
# Model Solution
# ============================================================================

import math
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# TASK 1: Data and the Drag Constant
# ============================================================================

G = 9.81      # gravitational acceleration (m/s^2)
RHO = 1.225   # density of air (kg/m^3)

# mass (kg), diameter (m), drag coefficient, launch speed (m/s)
football = {"mass": 0.430, "diameter": 0.220, "Cd": 0.25, "v0": 25.0}


def drag_constant(ball):
    """
    Return the drag constant k = RHO * Cd * A / (2 m) for a ball, in 1/m.

    Parameters:
        ball: Dictionary with keys "mass", "diameter" and "Cd"
    """
    radius = ball["diameter"] / 2.0
    area = math.pi * radius**2
    return RHO * ball["Cd"] * area / (2.0 * ball["mass"])


def terminal_velocity(k):
    """Return the terminal velocity sqrt(G / k), in m/s, for drag constant k (1/m)."""
    return math.sqrt(G / k)


# ============================================================================
# TASK 2: The Range Without Air
# ============================================================================

def vacuum_range(v0, angle_deg):
    """Return the range without air, in m, for launch speed v0 (m/s) and angle in degrees."""
    theta = math.radians(angle_deg)
    return v0**2 * math.sin(2.0 * theta) / G


# ============================================================================
# TASK 3: The Acceleration
# ============================================================================

def acceleration(vx, vy, k):
    """
    Return (ax, ay), in m/s^2, for a ball with velocity (vx, vy) and drag constant k.

    Parameters:
        vx, vy: Velocity components in m/s
        k: Drag constant in 1/m (k = 0 means no air)
    """
    speed = math.sqrt(vx**2 + vy**2)
    ax = -k * speed * vx
    ay = -G - k * speed * vy
    return ax, ay


# ============================================================================
# TASK 4: The Simulation
# ============================================================================

def simulate_trajectory(v0, angle_deg, k, dt=0.001):
    """
    Simulate a kick with the Euler method until the ball goes below the ground.

    Parameters:
        v0: Launch speed in m/s
        angle_deg: Launch angle in degrees
        k: Drag constant in 1/m
        dt: Time step in s (default 0.001)

    Returns:
        NumPy arrays t, x, y. The last point is the first one below the ground,
        so the range is x[-1].
    """
    theta = math.radians(angle_deg)

    # Starting values
    t = 0.0
    x = 0.0
    y = 0.0
    vx = v0 * math.cos(theta)
    vy = v0 * math.sin(theta)

    ts = [t]
    xs = [x]
    ys = [y]

    # One Euler step per pass, until the ball goes below the ground
    while y >= 0:
        ax, ay = acceleration(vx, vy, k)

        # Update the position first, using the velocity from the start of the step
        x = x + vx * dt
        y = y + vy * dt
        vx = vx + ax * dt
        vy = vy + ay * dt
        t = t + dt

        ts.append(t)
        xs.append(x)
        ys.append(y)

    return np.array(ts), np.array(xs), np.array(ys)


# ============================================================================
# TASK 6: Finding the Best Angle
# ============================================================================

def range_vs_angle(v0, k, dt=0.001):
    """Return NumPy arrays of angles (1 to 89 degrees) and their ranges, in m."""
    angles = []
    ranges = []

    for angle in range(1, 90):
        t, x, y = simulate_trajectory(v0, angle, k, dt)
        angles.append(angle)
        ranges.append(x[-1])

    return np.array(angles), np.array(ranges)


# ============================================================================
# RESULTS
# ============================================================================

if __name__ == "__main__":
    k = drag_constant(football)
    v0 = football["v0"]

    # ------------------------------------------------------------------------
    # Task 1
    # ------------------------------------------------------------------------
    print("TASK 1: Data and the drag constant")
    print(f"k   = {k:.5f} 1/m")
    print(f"v_t = {terminal_velocity(k):.2f} m/s")

    # ------------------------------------------------------------------------
    # Task 2
    # ------------------------------------------------------------------------
    print("\nTASK 2: The range without air")
    for angle in (30, 45, 60):
        print(f"vacuum_range(25, {angle}) = {vacuum_range(25, angle):.2f} m")

    # ------------------------------------------------------------------------
    # Task 3
    # ------------------------------------------------------------------------
    print("\nTASK 3: The acceleration")
    print("acceleration(10, 0, 0)  =", acceleration(10, 0, 0))
    ax, ay = acceleration(20, 15, k)
    print(f"acceleration(20, 15, k) = ({ax:.4f}, {ay:.4f})")

    # ------------------------------------------------------------------------
    # Task 4
    # ------------------------------------------------------------------------
    print("\nTASK 4: The simulation (45 degrees)")
    t, x, y = simulate_trajectory(v0, 45, k)
    print(f"Number of points: {len(t)}")
    print(f"Flight time:      {t[-1]:.2f} s")
    print(f"Highest point:    {y.max():.2f} m")
    print(f"Range:            {x[-1]:.2f} m")

    # ------------------------------------------------------------------------
    # Task 5
    # ------------------------------------------------------------------------
    print("\nTASK 5: Testing the simulation (k = 0, 45 degrees)")
    t, x, y = simulate_trajectory(v0, 45, 0)
    R_sim = x[-1]
    R_exact = vacuum_range(v0, 45)
    rel_err = abs(R_sim - R_exact) / R_exact
    print(f"Simulated range: {R_sim:.3f} m")
    print(f"Exact range:     {R_exact:.3f} m")
    print(f"Relative error:  {rel_err:.1e}")

    # ------------------------------------------------------------------------
    # Task 6
    # ------------------------------------------------------------------------
    print("\nTASK 6: Finding the best angle")
    angles, ranges = range_vs_angle(v0, k)
    i = np.argmax(ranges)
    print(f"Best angle:            {angles[i]} deg")
    print(f"Best range:            {ranges[i]:.2f} m")
    print(f"Range without air:     {R_exact:.2f} m (45 deg)")
    print(f"Ratio of the ranges:   {ranges[i] / R_exact:.3f}")

    # ------------------------------------------------------------------------
    # Task 7, Figure 1: Trajectories with and without air
    # ------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 4.5))
    for n, angle in enumerate([15, 30, 45, 60, 75]):
        t, x, y = simulate_trajectory(v0, angle, 0)
        ax.plot(x, y, "--", color=f"C{n}")
        t, x, y = simulate_trajectory(v0, angle, k)
        ax.plot(x, y, "-", color=f"C{n}", label=f"{angle}°")
    ax.set_ylim(bottom=0)
    ax.set_aspect("equal")
    ax.set_xlabel("Horizontal distance x (m)")
    ax.set_ylabel("Height y (m)")
    ax.set_title("Football at 25 m/s: with air (solid), without air (dashed)")
    ax.legend(title="Launch angle")

    # ------------------------------------------------------------------------
    # Task 7, Figure 2: Range against angle
    # ------------------------------------------------------------------------
    vacuum_ranges = [vacuum_range(v0, angle) for angle in angles]
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(angles, ranges, "-", label="With air")
    ax.plot(angles, vacuum_ranges, "--", label="Without air")
    ax.plot(angles[i], ranges[i], "o", color="C0")
    ax.plot(45, R_exact, "o", color="C1")
    ax.set_xlabel("Launch angle (degrees)")
    ax.set_ylabel("Range (m)")
    ax.set_title("Football at 25 m/s: range against launch angle")
    ax.legend()

    # ------------------------------------------------------------------------
    # Written questions 3 and 4: the checks they ask for
    # ------------------------------------------------------------------------
    print("\nWRITTEN QUESTION 3: Task 5 with dt ten times smaller")
    t, x, y = simulate_trajectory(v0, 45, 0, dt=0.0001)
    print(f"Relative error: {abs(x[-1] - R_exact) / R_exact:.1e}")

    print("\nWRITTEN QUESTION 4: A gentle kick at 10 m/s")
    angles_10, ranges_10 = range_vs_angle(10, k)
    i_10 = np.argmax(ranges_10)
    print(f"Best angle:          {angles_10[i_10]} deg")
    print(f"Ratio of the ranges: {ranges_10[i_10] / vacuum_range(10, 45):.3f}")

    plt.show()
