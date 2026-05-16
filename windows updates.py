import time
import random


def clear_screen(lines=10):
    for i in range(lines):
        print()


def progress_bar(perc, width=30):
    filled = int((perc / 100.0) * width)
    return "[" + ("#" * filled) + ("-" * (width - filled)) + "]"


def show_update(perc, component, action, lines=10):
    clear_screen(lines)
    print("Windows is Updating. Please Do not Turn Off your Computer")
    print("Progress:", progress_bar(perc), f"{perc}%")
    print("Component:", component)
    print("Status:", action)


components = [
    "Security Intelligence",
    "Windows Defender",
    "Device Drivers",
    "Network Stack",
    "DirectX Runtime",
    "System Files",
    "Registry Settings",
    "Start Menu Experience",
]

actions = [
    "Preparing",
    "Downloading",
    "Installing",
    "Applying",
    "Verifying",
    "Finalizing",
]


print("Windows is Updating. Please Do not Turn Off your Computer")
print("Progress:", progress_bar(0), "0%")
perc = 0
time.sleep(10)


while perc < 63:
    # same structure as your original code
    for i in range(10):
        print()
    a = random.randint(1, 8)
    perc = min(63, perc + a)
    time.sleep(random.randint(3, 9))
    show_update(perc, random.choice(components), random.choice(actions), 0)
    time.sleep(random.randint(2, 10))


if perc == 63:
    time.sleep(random.randint(5, 15))


while perc < 90:
    for i in range(10):
        print()
    a = random.randint(1, 6)
    perc = min(90, perc + a)
    time.sleep(random.randint(3, 9))
    show_update(perc, random.choice(components), random.choice(actions), 0)


while perc < 100:
    for i in range(10):
        print()
    perc += 1
    time.sleep(random.randint(5, 11))
    show_update(perc, random.choice(components), "Finalizing", 0)


if perc == 100:
    for i in range(10):
        print()
    show_update(perc, "System Files", "Finalizing", 0)
    time.sleep(random.randint(5, 15))

for i in range(10):
    print()
print("Restarting Your Computer")
time.sleep(5)

for i in range(10):
    print()
    time.sleep(0.25)

print("Updates Completed.")



