import random
from rich.console import Console
from rich.text import Text

from feedback import get_feedback

console = Console()


# Get a random word from a vocabulary
def get_target_word(vocabulary, length):
    with open(f'words/{vocabulary}/{length}.txt', 'r', encoding='utf-8') as file:
        words = file.readlines()  # Each line is a word
        return random.choice(words).strip()


# TODO: Ask the player to choose a vocabulary and word length
length = 5
vocabulary = 'CET6'
max_attempts = 6


target_word = get_target_word(vocabulary, length)

console.print(f"\n[bold]Welcome to Wordline![/bold]\n")

attempts = 1

while attempts <= max_attempts:
    input_word = console.input(f"[cyan][{attempts}/{max_attempts}][cyan] [yellow bold]Guess a word: [/yellow bold]").lower()

    if len(input_word) != length or input_word.isalpha() == False:
        console.print(f"[magenta]Invalid word. Please enter a word with [white bold]"+str(length)+"[/white bold] letters.[/magenta]")
        continue
    
    # TODO: Check if the input word is in the vocabulary

    else:
        feedback = get_feedback(target_word, input_word)
        console.print(Text.assemble(*feedback))

        if input_word == target_word:
            console.print(f"\n[green]Congratulations! You've guessed the word: [yellow bold underline]{target_word}[/yellow bold underline]![/green]\n")
            break

        attempts += 1

if attempts > max_attempts:
    console.print(f"\n[magenta]Sorry, you've run out of attempts. The word was [yellow bold underline]{target_word}[/yellow bold underline].[/magenta]\n")