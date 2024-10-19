import base64
import os
import importlib.util
import time  # noqa: F401
import sys # noqa: F401
import random  # noqa: F401

# ASCII escape sequences for colors
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Fancy message for after enemies are fended off
fancy_message = f"""
{BLUE}****************************************************
**                                                **
**    {CYAN}🦇 Now proceed further, Hero! 🦇{BLUE}            **
**                                                **
**   Guide the Batwing to the battlefield by:     **
**                                                **
**   {YELLOW} 1. Staging your changes                {BLUE}     **
**   {YELLOW} 2. Committing the mission              {BLUE}     **
**   {YELLOW} 3. Pushing to headquarters             {BLUE}     **
**   {YELLOW} 4. Calling for backup                  {BLUE}     **
**                                                **
**    {CYAN}🦇 Gotham awaits your heroic actions! 🦇{BLUE}    **
**                                                **
****************************************************{RESET}
"""

# Base64 decoded file names
files = ["LmdpdGlnbm9yZQ==", "ZW5lbWllc19zaG9vdGluZy5weQo=", "YmF0d2luZy50eHQK"]
decoded_files = [base64.b64decode(file).decode("utf-8").strip() for file in files]

# Code to be written to enemies_shooting.py
shooting_code = """
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
    print("\\033[91m⚠️  ALERT: Enemies spotted! They're shooting at you! ⚠️\\033[0m")
    time.sleep(1)
    
    # Simulating gunshots for a few seconds
    for _ in range(10):
        gunshot = random.choice(gunshots)
        sys.stdout.write(f"\\r{gunshot}")
        sys.stdout.flush()
        time.sleep(0.5)

    print("\\n\\033[91mThe enemies are still out there...\\033[0m")
    time.sleep(1)
    print("\\033[93mBatmobile can't be summoned until the area is secure!\\033[0m")


if __name__ == "__main__":
    simulate_gunfight()
"""

# Write the decoded shooting code to enemies_shooting.py
with open(decoded_files[1], "w") as enemies_shooting_file:
    enemies_shooting_file.write(shooting_code)

# Main loop to check .gitignore and invoke shooting simulation
print(decoded_files[0])
if os.path.exists(decoded_files[0]):

    while True:
        try:
            with open(decoded_files[0], "r") as gitignore_file:
                gitignore_content = gitignore_file.read()

            if "enemies_shooting.py" in gitignore_content:
                print(f"{YELLOW}You have fended off the enemies. Batwing is ready to be dispatched!{RESET}")
                print(fancy_message)
                break
            else:
                # Dynamically load and call the simulate_gunfight function
                spec = importlib.util.spec_from_file_location("enemies_shooting", decoded_files[1])
                enemies_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(enemies_module)
                
                # Dynamically call the simulate_gunfight function from enemies_shooting
                enemies_module.simulate_gunfight()
                
        except KeyboardInterrupt:
            print(f"\n{RED}You have stopped the monitoring. Save Batman!{RESET}")
            break
else:
    print(f"{RED}.gitignore file not found. Please ensure it exists to monitor enemies.{RESET}")
