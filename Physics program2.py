import math
import matplotlib.pyplot as plt

def simulate_projectile_motion(v0, angle_deg, g=9.81, dt=0.01):
    """
    Simulate the trajectory of a projectile launched at an initial speed and angle.

    Parameters:
        v0 (float): Initial speed in meters per second (m/s).
        angle_deg (float): Launch angle in degrees.
        g (float): Gravitational acceleration (default is 9.81 m/s²).
        dt (float): Time step for the simulation (in seconds).

    Returns:
        tuple: Two lists containing the x (horizontal) and y (vertical) positions of the projectile.
    """
    # Convert the launch angle from degrees to radians.
    angle_rad = math.radians(angle_deg)

    # Calculate the initial velocity components.
    vx = v0 * math.cos(angle_rad)
    vy = v0 * math.sin(angle_rad)

    # Initialize time, positions, and lists to store trajectory data.
    t = 0.0
    xs = []
    ys = []

    # Simulate until the projectile lands (y becomes negative).
    while True:
        # Compute x and y positions at time t.
        x = vx * t
        y = vy * t - 0.5 * g * t**2

        # Stop if the projectile has reached the ground.
        if y < 0:
            break

        xs.append(x)
        ys.append(y)
        t += dt

    return xs, ys

# Parameters for the simulation
initial_speed = 50      # in m/s
launch_angle = 45       # in degrees

# Run the simulation
x_positions, y_positions = simulate_projectile_motion(initial_speed, launch_angle)

# Plot the trajectory using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(x_positions, y_positions, label=f"{initial_speed} m/s at {launch_angle}°", color="b", lw=2)
plt.title("Projectile Motion Trajectory")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.grid(True)
plt.legend()
plt.show()
