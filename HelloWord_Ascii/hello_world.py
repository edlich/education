import datetime

def print_hello():
    ascii_art = r"""
     _   _      _ _         __        __         _     _ _ 
    | | | | ___| | | ___    \ \      / /__  _ __| | __| | |
    | |_| |/ _ \ | |/ _ \    \ \ /\ / / _ \| '__| |/ _` | |
    |  _  |  __/ | | (_) |    \ V  V / (_) | |  | | (_| |_|
    |_| |_|\___|_|_|\___/      \_/\_/ \___/|_|  |_|\__,_(_)
                                                        
    """
    print(ascii_art)
    print("Hello World!")
    print("Current time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    print_hello()
