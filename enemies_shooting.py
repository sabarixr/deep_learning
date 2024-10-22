
import time
import sys
import random
from summon_batwing import check_gitignore

gunshots = [
    "🔫 Pew! Pew!",
    "💥 Bang! Bang!",
    "🔫 🚀 Boom!",
    "💥💥 Rat-a-tat-tat!",
    "🔫 🔥 Ka-pow!",
]

def simulate_gunfight():
    if check_gitignore():
            return 1
    print()
    print("\033[91m⚠️  ALERT: Enemies spotted! They're shooting at you! ⚠️\033[0m")
    time.sleep(1)

    for _ in range(5):
        if check_gitignore():
            return 1
        gunshot = random.choice(gunshots)
        sys.stdout.write(f"\r{' ' * 30}")
        sys.stdout.write(f"\r{gunshot}")
        sys.stdout.flush()
        time.sleep(0.5)
    print()
    print("\n\033[91mThe enemies are still out there...\033[0m")
    time.sleep(1)
    print("\033[93mBatwing can't be summoned until the area is secure!\033[0m")
