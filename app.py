from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import psutil
import os,sys
from module2 import buffer

if psutil.cpu_percent() >=95 or psutil.virtual_memory().percent >=95 :
    os.system("systemctl poweroff")

while True:
        
    console = Console()

    panel = Panel(
        "[bold green]System Status:[/bold green] All services operational.",
        title="[bold cyan]Project Tittle[/bold cyan]",
        style="bright_white on black",
        border_style="green"
    )

    console.print(panel)


    grid = Table.grid(expand=True, padding=1)

    # ratio=1 gives equal column widths
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)
    grid.add_column(ratio=1)

    # Render two panels side by side
    grid.add_row(
        Panel(
            f"[bold green]CPU Usage:{psutil.cpu_percent()}[/bold green]%", 
            title="Processor", 
            border_style="green"),
        Panel(
            f"[bold green]RAM Usage:{psutil.virtual_memory().percent}[/bold green]%",
              title="Memory", 
              border_style="magenta"),
        Panel(
            f"[bold green]SWAP Usage:{psutil.swap_memory().percent}[/bold green]%", 
            title="Swap",
             border_style="green"),
        Panel(
            f"[bold green]Diska Usage:{psutil.disk_usage('/').percent}[/bold green]%",
             title="Storage", 
             border_style="blue")
        
    )

    console.print(grid)

    panel_analyzing=Panel(
        f"[bold yellow]suggestion:{buffer}[bold yellow]",  #buffer from file module2.py
        title="Analyzing", 
        border_style="blue",
        height=10,
        expand=True
        )

    console.print(panel_analyzing)


    panel_terminal=Panel(
        "[bold green]Terminal >>> ...Type Exit To Exit[bold green]", 
        title=">>>", 
        border_style="green",
        height=0,
        expand=True
        )

    console.print(panel_terminal)

    user_input=Prompt.ask(">>>")
    if user_input.lower() in ["exit","q"]:
        break
    else:
        process = subprocess.Popen([sys.executable, "module1.py"])
        
        



