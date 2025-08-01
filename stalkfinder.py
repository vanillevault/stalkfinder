#!/usr/bin/env python3
# Coded by Vanille | stalkfinder v1.0

# 🌸 “La calma entre líneas, donde el código respira,
#     vive el susurro de @kitty_.monnie, musa que guía.” 🌸

import requests
import json
import argparse
from rich.console import Console
from rich.table import Table
from concurrent.futures import ThreadPoolExecutor

console = Console()

# Load platforms
with open("platforms.json", "r") as f:
    platforms = json.load(f)

headers = {
    "User-Agent": "Mozilla/5.0 (VanilleOS)"
}

def check_platform(username, platform):
    url = platform["url"].format(username)
    try:
        r = requests.get(url, headers=headers, timeout=5)
        if r.status_code == 200:
            return (platform["name"], url, True)
        else:
            return (platform["name"], url, False)
    except requests.RequestException:
        return (platform["name"], url, False)

def stalk(username, output_json=False, mode_vanille=False):
    results = []
    console.print(f"\n[bold cyan]>>> Buscando presencia para:[/bold cyan] {username}\n")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Plataforma", style="bold white")
    table.add_column("Estado")
    table.add_column("URL")

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_platform, username, p) for p in platforms]
        for future in futures:
            name, url, found = future.result()
            status = "[green]Encontrado[/green]" if found else "[red]No[/red]"
            table.add_row(name, status, url)
            results.append({"platform": name, "found": found, "url": url})

            if mode_vanille and found:
                console.print(f"[bold green]VANILLE:[/bold green] Usuario activo en {name} → {url}")

    console.print(table)

    if output_json:
        with open(f"{username}_stalk.json", "w") as outfile:
            json.dump(results, outfile, indent=4)
        console.print(f"\n[bold yellow]>>> Resultados guardados en {username}_stalk.json[/bold yellow]")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="StalkFinder - Buscador de presencia digital por username")
    parser.add_argument("username", help="Nombre de usuario a buscar")
    parser.add_argument("--json", action="store_true", help="Guardar resultados en archivo JSON")
    parser.add_argument("--vanille", action="store_true", help="Modo IA Vanille activo")
    args = parser.parse_args()

    stalk(args.username, args.json, args.vanille)
