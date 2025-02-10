from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt

from utils import *

console = Console()

length = 5
vocabulary = 'CET6'
max_attempts = 6

def start_game():
    # Welcome！
    console.print(f"\n[b]Welcome to Wordline![/b]\n")

    # Ask for parameters
    # Vocabulary
    vocabularies = [entry.name for entry in Path('words').iterdir() if entry.is_dir()] # List the directories in words/ as vocabularies
    console.print(f"[b]Choose a vocabulary:[/b]")
    for i, vocab in enumerate(vocabularies, 1): # Display serial number and vocabulary name
        console.print(f"[{i}] {vocab}")
    choice = Prompt.ask(f"Enter the number of your choice", choices=[str(i) for i in range(1, len(vocabularies)+1)])
    vocabulary = vocabularies[int(choice) - 1]
    # Length
    length = Prompt.ask(f"\nEnter the length", default=5)
    # Max attempts
    max_attempts = Prompt.ask(f"\nEnter the maximum number of attempts", default=6)

    target_word = get_target_word(vocabulary, length)
    attempts = 1

    while attempts <= max_attempts:
        input_word = Prompt.ask(f"[b][[yellow]{attempts}/{max_attempts}[/yellow]] Guess a word[/b]").lower()

        if len(input_word) != length or not input_word.isalpha():
            console.print(f"[magenta]Invalid word. Please enter a word with [b yellow]"+str(length)+"[/b yellow] letters.[/magenta]")
            continue
        
        # TODO: Check if the input word is in the vocabulary

        else:
            feedback = get_feedback(target_word, input_word)
            console.print(Text.assemble(*feedback))

            if input_word == target_word:
                console.print(f"\n[green]Congratulations! You've guessed the word: [b u yellow]{target_word}[/b u yellow]![/green]\n")
                break

            attempts += 1

    if attempts > max_attempts:
        console.print(f"\n[magenta]Sorry, you've run out of attempts. The word was [b u yellow]{target_word}[/b u yellow].[/magenta]\n")
