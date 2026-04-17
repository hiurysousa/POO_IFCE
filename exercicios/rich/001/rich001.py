from rich import print
import rich
from rich.traceback import install

print("Olá [bold red on blue]mundo[/]!")
rich.inspect(float)
install() # erro de forma mais legível