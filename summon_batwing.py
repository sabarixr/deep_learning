import base64
import os
import importlib.util
import time
import sys
import random
import string

RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RESET = "\033[0m"

HEALTH_DECREASE_RATE = 10
COUNT_DODGE = 3
BATMAN_HEALTH = 100
CONNECTION_MADE = False

files = ["LmdpdGlnbm9yZQ==", "ZW5lbWllc19zaG9vdGluZy5weQo=", "YmF0d2luZy50eHQK"]
decoded_files = [base64.b64decode(file).decode("utf-8").strip() for file in files]

def check_gitignore():
    with open(decoded_files[0], "r") as gitignore_file:
        gitignore_content = gitignore_file.read()
    return "enemies_shooting.py" in gitignore_content

shooting_code = """
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
    print("\\033[91m⚠️  ALERT: Enemies spotted! They're shooting at you! ⚠️\\033[0m")
    time.sleep(1)

    for _ in range(5):
        if check_gitignore():
            return 1
        gunshot = random.choice(gunshots)
        sys.stdout.write(f"\\r{' ' * 30}")
        sys.stdout.write(f"\\r{gunshot}")
        sys.stdout.flush()
        time.sleep(0.5)

    print("\\n\\033[91mThe enemies are still out there...\\033[0m")
    time.sleep(1)
    print("\\033[93mBatmobile can't be summoned until the area is secure!\\033[0m")
"""

def collect_git_command(command):
    print(f"{CYAN}✨ Collected Git command: {command}! Use it wisely! ✨{RESET}")

with open(decoded_files[1], "w") as enemies_shooting_file:
    enemies_shooting_file.write(shooting_code)

if os.path.exists(decoded_files[0]):
    fended_off = False
    health = BATMAN_HEALTH
    print(f"{CYAN}💔 Batman's Health: {health}/{BATMAN_HEALTH}{RESET}")

    while health > 0:
        if COUNT_DODGE == 0:
            with open(decoded_files[2], "w") as batwing_file:
                batwing_file.write("The legendary weapon of Batman is ready to strike!")
            print(f"\n{GREEN}🌟 Communication with Batwing successful! 🌟{RESET}")
            print(f"{YELLOW}✨ The .gitignore file is used to specify files and directories that should be ignored by Git, preventing them from being tracked or added to version control. ✨{RESET}")
            print(f"{GREEN}⚠️ Please add {RED}enemies_shooting.py {GREEN}to your .gitignore file. ⚠️{RESET}\n")

            CONNECTION_MADE = True


        try:
            if check_gitignore() and fended_off:
                break

            spec = importlib.util.spec_from_file_location("enemies_shooting", decoded_files[1])
            enemies_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(enemies_module)

            value = enemies_module.simulate_gunfight()
            if value == 1:
                fended_off = True
            if not CONNECTION_MADE:
                dodge_letter = random.choice(string.ascii_lowercase)

                print(f"{YELLOW}⚠️  Quick Time Event! Press '{dodge_letter}' to dodge the attack!{RESET}")
                start_time = time.time()
                user_input = input("Your input: ").strip().lower()
                elapsed_time = time.time() - start_time

                if user_input == dodge_letter and elapsed_time < 2:
                    print(f"{GREEN}✅ Dodge successful! You avoided the attack!{RESET}")
                    COUNT_DODGE -= 1
                else:
                    print(f"{RED}❌ Dodge failed! You got hit! Lose {HEALTH_DECREASE_RATE} health points.{RESET}")
                    health -= HEALTH_DECREASE_RATE
                    HEALTH_DECREASE_RATE *=1.5
                    print(f"{CYAN}💔 Batman's Health: {health}/{BATMAN_HEALTH}{RESET}")
                    sys.exit()

            if random.random() < 0.5:
                collect_git_command("git status")

        except KeyboardInterrupt:
            print(f"\n{RED}You have stopped the monitoring. Save Batman!{RESET}")
            sys.exit()

    if health <= 0:
        print(f"{RED}💀 Batman has fallen. The city needs a new hero! 💀{RESET}")

else:
    print(f"{RED}.gitignore file not found. Please ensure it exists to monitor enemies.{RESET}")

if health > 0:
    print(f"\n{YELLOW}You have fended off the enemies. Batwing is ready to be dispatched!{RESET}")
    fancy_message = f"""
    {BLUE}****************************************************
    **                                                **
    **    {CYAN}🦇 Now proceed further, Hero! 🦇{BLUE}            **
    **                                                **
    **   Guide the Batwing to the battlefield by:     **
    **                                                **
    **   {YELLOW} 1. Staging your changes                {BLUE}     **
    **   {YELLOW} 2. Committing the changes              {BLUE}     **
    **   {YELLOW} 3. Pushing to repository             {BLUE}       **
    **   {YELLOW} 4. Sending a PR                  {BLUE}           **
    **                                                **
    **    {CYAN}🦇 Gotham awaits your heroic actions! 🦇{BLUE}    **
    **                                                **
    ****************************************************{RESET}
        """
    print(fancy_message)

sys.exit()
