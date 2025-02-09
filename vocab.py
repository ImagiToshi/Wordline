import random
from rich.console import Console

console = Console()

def get_target_word(vocabulary, length):
    try:
        with open(f'words/{vocabulary}/{length}.txt', 'r', encoding='utf-8') as file:
            words = file.readlines() # Each line is a word
            if words:
                return random.choice(words).strip()
            else:
                raise ValueError("No words found for this length.")
    except FileNotFoundError:
        console.print(f"[red]Error: The file for {vocabulary}/{length}.txt was not found.[/red]")
        return None
    except ValueError as e:
        console.print(f"[red]{e}[/red]")
        return None