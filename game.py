from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt

from utils import *

console = Console()

# TODO: Ask the player to choose a vocabulary and word length
length = 5
vocabulary = 'CET6'
max_attempts = 6

def start_game():
    # Welcome！
    console.print(f"\n[b]Welcome to Wordline![/b]\n")

    # Choose vocabulary and word length and set max attempts
    

    target_word = get_target_word(vocabulary, length)
    attempts = 1

    while attempts <= max_attempts:
        input_word = console.input(f"[cyan][{attempts}/{max_attempts}][cyan] [b yellow]Guess a word: [/b yellow]").lower()

        if len(input_word) != length or input_word.isalpha() == False:
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
