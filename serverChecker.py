import socket 

def is_running(site):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except:
        return False

if __name__ == "__main__":
    while True:
        site = input('Website to check: ')
        if is_running(f'{site}'):
            print(f"{site} is running!")
        else:
            print(f'{site} is not running! Try again later')

        if input("Would You like to check another website(Y/N)? ") in {'n', 'N'}:
            break
            