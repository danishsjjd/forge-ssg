from pathlib import Path
import shutil
import os


def clean_dir(dir: Path):
    if Path.exists(dir):
        shutil.rmtree(dir)


def clean_copytree(source: Path, dest: Path):
    if Path.is_dir(source):
        clean_dir(dest)
        Path.mkdir(dest)
        source_dir = os.listdir(source)
        for item in source_dir:
            clean_copytree(source / item, dest / item)
    else:
        print("COPY", source, "->", dest)
        shutil.copy(source, dest)
