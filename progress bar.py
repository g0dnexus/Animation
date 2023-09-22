import time
from colorama import init, Fore

init()
bar_length = 20

def update_progress(progress):
    filled_length = int(bar_length * progress)
    bar = f"{Fore.GREEN}█" * filled_length + f"{Fore.RESET}-" * (bar_length - filled_length)
    print(f'\rProgress: [{bar}] {progress * 100:.1f}%', end='', flush=True)

def main():
    total_items = 100 
    for item_index in range(total_items + 1):
        progress = item_index / total_items
        update_progress(progress)
        time.sleep(0.1)
    print("\nCompleted!")

if __name__ == '__main__':
    main()
