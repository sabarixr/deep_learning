
import time
import sys
import random

# ASCII Art for gunfire effects
gunshots = [
    "🔫 Pew! Pew!",
    "💥 Bang! Bang!",
    "🔫 🚀 Boom!",
    "💥💥 Rat-a-tat-tat!",
    "🔫 🔥 Ka-pow!",
]

# Function to simulate gunfire with delays and text animation
def simulate_gunfight():
    print("\033[91m⚠️  ALERT: Enemies spotted! They're shooting at you! ⚠️\033[0m")
    time.sleep(1)
    
    # Simulating gunshots for a few seconds
    for _ in range(10):
        gunshot = random.choice(gunshots)
        sys.stdout.write(f"\r{gunshot}")
        sys.stdout.flush()
        time.sleep(0.5)

    print("\n\033[91mThe enemies are still out there...\033[0m")
    time.sleep(1)
    print("\033[93mBatmobile can't be summoned until the area is secure!\033[0m")


if __name__ == "__main__":
    simulate_gunfight()
