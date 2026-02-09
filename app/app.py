import time
import socket

def main():
    hostname = socket.gethostname()
    print(f"Application started on host: {hostname}")

    while True:
        print("App is running...")
        time.sleep(5)

if __name__ == "__main__":
    main()
