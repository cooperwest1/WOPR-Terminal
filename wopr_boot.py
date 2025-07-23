import time

print("WOPR SYSTEM BOOT SEQUENCE")
time.sleep(1)
print("Loading core modules...")
time.sleep(1)
print("Initializing thermal logic array...")
time.sleep(1)
print("Hello Professor Falken.")
time.sleep(1)

while True:
    cmd = input(">")
    if cmd.lower() in ["play game", "global thermonuclear war", "tic tac toe"]:
        print("WOULD YOU LIKE TO PLAY A GAME?")
    elif cmd.lower() == "exit":
        print("SHUTTING DOWN...")
        break
    else:
        print("UNKNOWN COMMAND")
