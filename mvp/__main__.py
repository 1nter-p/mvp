import os
import sys
import shutil
import pathlib

from .color import Color


def get_sources_and_destination() -> tuple[list[str], str]:
    """Get the sources and destination from :code:`sys.argv`"""
    return (sys.argv[1:-1], sys.argv[-1])


def log_move(source_path: str, source_to_destination_path: str) -> None:
    """Log when files are moved."""
    print(f"{Color.YELLOW}{source_path} {Color.RESET}→ {Color.GREEN}{source_to_destination_path}{Color.RESET}")


def log_not_found(path: str) -> None:
    """Log when a path/file doesn't exist."""
    print(f"{Color.RED}Could not find {Color.YELLOW}{path}{Color.RESET}.")


def main() -> None:
    if len(sys.argv) < 3:
        return

    sources, destination = get_sources_and_destination()

    for source in sources:
        if not os.path.exists(source):
            log_not_found(source)
            continue

        log_move(str(pathlib.Path(source)), shutil.move(source, destination))


if __name__ == "__main__":
    main()
