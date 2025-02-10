import random
from rich.console import Console
from rich.text import Text

console = Console()

def get_feedback(target, input):
    feedback = []
    target_letter_count = {letter: target.count(letter) for letter in set(target)}
    correct_positions = [False] * len(target)

    for i, letter in enumerate(input):
        if letter == target[i]:
            feedback.append(Text(letter.upper(), style="bold green"))
            target_letter_count[letter] -= 1
            correct_positions[i] = True
        else:
            feedback.append(None)

    for i, letter in enumerate(input):
        if feedback[i] is None:
            if letter in target and target_letter_count[letter] > 0 and not correct_positions[i]:
                feedback[i] = Text(letter.upper(), style="bold yellow")
                target_letter_count[letter] -= 1
            else:
                feedback[i] = Text(letter.upper(), style="dim")

    return feedback


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