#!/usr/bin/python3
import io
import subprocess
import sys
import time
from datetime import date, datetime

import typer
from rich.console import Console

from branch_time.GitRepositoryError import GitRepositoryError

app = typer.Typer(help="Awesome CLI user manager.")
console = Console()


def is_not_same_branch(last_line, branch):
    console.print(last_line)
    return branch not in last_line


def last_line_on_file(file) -> str:
    try:
        file.seek(io.SEEK_CUR)
        return file.readlines()[-1]
    except IndexError:
        return ""


def time_change(time):
    hora, min, sec = time.split(":")
    data_current = datetime.now()
    data_obj = datetime(
        data_current.year,
        data_current.month,
        data_current.day,
        int(hora),
        int(min),
        int(sec),
    )
    hour, min, seg = f"{data_current - data_obj}".split(":")[:3]
    return f"{hour} {min} {seg.split('.')[0]}"


def count_time(branch: str, last_line: str) -> str:
    try:
        time = last_line.split("Tempo:")[1].replace("\n", "")
        return f"Changer for Branch:{branch} after{time_change(time)}\n\n"
    except:
        return "\n"


@app.command()
def getFile(
    repository: str = typer.Argument(
        ".", help="Repository git. Default: Current directory"
    ),
    time_in_minute: int = typer.Option(
        5, "--time", "-t", help="Time for update current branch"
    ),
    output_file: str = typer.Option(
        date.today(),
        "--output",
        "-o",
        help="location where text file with timing of branch changes will be saved",
    ),
):
    # console.print("[red1]Time count started...\n\n")
    while True:
        with open(f"{output_file}.txt", "a+") as file:
            try:
                process = subprocess.Popen(
                    "git rev-parse --abbrev-ref HEAD",
                    stdout=subprocess.PIPE,
                    cwd=repository,
                )
                output, error = process.communicate()
                now = datetime.now()
                branch = output.decode().replace("\n", "")
                if branch == "":
                    raise GitRepositoryError("")

                last_line = last_line_on_file(file)
                if is_not_same_branch(last_line, branch):
                    file.write(count_time(branch, last_line))
                    file.write(
                        f"Branch: {branch} - Time: {now.hour}:{now.minute}:{now.second}\n"
                    )
                time.sleep(time_in_minute * 60)
                
            except NotADirectoryError:
                console.print("[red1]Directory not found")
                sys.exit(1)
            except KeyboardInterrupt:
                now = datetime.now()
                file.write(f"FINISHED... {now.hour}:{now.minute}:{now.second}\n")
                sys.exit(0)
            except GitRepositoryError as git_error:
                console.print(git_error.message)
                console.print(
                    "[red1]--repository parameter does not point to a git repository"
                )
                sys.exit(1)
