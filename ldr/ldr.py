import time

def loading_spinner(ld,duration):
    animation = "|/-\\"
    start_time = time.time()

    while time.time() - start_time < duration:
        for char in animation:
            print(f"\r{ld} {char}", end="")
            time.sleep(0.1)
    print("\rDone!")

# Example: Display loading spinner for 5 seconds
# loading_spinner(5)
