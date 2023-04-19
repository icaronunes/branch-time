#!/usr/bin/python3
# -*- coding: utf-8 -*-
import typer
import subprocess
from datetime import datetime, date
import time
import io
import sys

app = typer.Typer()


def is_not_same_branch(last_line, branch):
    print(last_line)
    return branch not in last_line


def last_line_on_file(file) -> str:
    try:
        file.seek(io.SEEK_CUR)
        return file.readlines()[-1]
    except IndexError:
        return ''


def time_change(time):
    hora, minutos, sec = time.split(":")
    data_atual = datetime.now()
    data_obj = datetime(data_atual.year, data_atual.month,
                        data_atual.day, int(hora), int(minutos), int(sec))
    hour, min, seg = f"{data_atual - data_obj}".split(':')[:3]
    return f"{hour} {min} {seg.split('.')[0]}"


def count_time(branch: str, last_line: str) -> str:
    try:
        time = last_line.split('Tempo:')[1].replace('\n', '')
        return f"Changer for Branch:{branch} after{time_change(time)}\n\n"
    except:
        return '\n'


@app.command()
def getFile(repository: str, time_in_minute: int = 5):
    while True:
        with open(f'{date.today()}.txt', 'a+') as file:
            try:
                process = subprocess.Popen('git rev-parse --abbrev-ref HEAD', stdout=subprocess.PIPE,
                                           cwd=repository)
                output, error = process.communicate()
                now = datetime.now()
                branch = output.decode().replace("\n", '')
                last_line = last_line_on_file(file)
                if is_not_same_branch(last_line, branch):
                    file.write(count_time(branch, last_line))
                    file.write(
                        f'Branch:{branch} - Time:{now.hour}:{now.minute}:{now.second}\n')
                time.sleep(time_in_minute)
            except NotADirectoryError:
                print("Diretório não encontrado")
                sys.exit(1)
            except KeyboardInterrupt:
                now = datetime.now()
                file.write(
                    f"FINALIZADO... {now.hour}:{now.minute}:{now.second}\n")
                sys.exit(0)


if __name__ == "__main__":
    app()
