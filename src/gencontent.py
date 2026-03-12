from pathlib import Path
from forge_ssg.markdown.markdon_blocks import markdown_to_html_node
import os


def extract_title(markdown: str) -> str:
    for line in markdown.strip().split("\n\n"):
        if line.startswith("# "):
            title = line[2:]
            return title

    raise ValueError("Title not found")


def generate_page(from_path: Path, template_path: Path, dest_path: Path, basepath: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = Path.read_text(from_path)
    template = Path.read_text(template_path)
    title = extract_title(markdown)
    html = markdown_to_html_node(markdown)
    content = template.replace("{{ Title }}", title).replace(
        "{{ Content }}", html.to_html()
    )
    normalized_content = content.replace('href="/', f'href="{basepath}')
    normalized_content = normalized_content.replace('src="/', f'src="{basepath}')
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(normalized_content)


def generate_pages_recursive(
    dir_path_content: Path,
    template_path: Path,
    dest_dir_path: Path,
    basepath: str = "/",
):
    for item in os.listdir(dir_path_content):
        if Path.is_dir(dir_path_content / item):
            generate_pages_recursive(
                dir_path_content / item, template_path, dest_dir_path / item, basepath
            )
        elif item.endswith(".md"):
            generate_page(
                dir_path_content / item,
                template_path,
                dest_dir_path / f"{item[:-3]}.html",
                basepath,
            )
