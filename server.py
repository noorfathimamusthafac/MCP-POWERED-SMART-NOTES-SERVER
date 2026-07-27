import re
from pathlib import Path

from mcp.server.fastmcp import FastMCP


# Create the MCP server
mcp = FastMCP("Notes MCP Server")

# Directory where all note files will be stored
NOTES_DIR = Path(__file__).parent / "notes"

# Make sure the notes directory exists
NOTES_DIR.mkdir(exist_ok=True)


def generate_filename(title: str) -> str:
    """
    Generate a safe Markdown filename from a note title.

    Example:
        "Project Meeting" -> "project_meeting.md"
    """
    filename = title.strip().lower()
    filename = re.sub(r"[^a-z0-9]+", "_", filename)
    filename = filename.strip("_")

    return f"{filename}.md"

@mcp.tool()
def create_note(title: str, content: str) -> dict:
    """
    Create a new note as a Markdown file.

    Args:
        title: The title of the note.
        content: The content to store in the note.

    Returns:
        A dictionary containing the status and filename.
        If the note already exists, it will not be created again.
    """

    filename = generate_filename(title)
    file_path = NOTES_DIR / filename

    # Prevent duplicate notes
    if file_path.exists():
        return {
            "status": "already_exists",
            "file": filename
        }

    # Create Markdown content
    note_content = f"# {title.strip()}\n\n{content.strip()}\n"

    # Save note to file
    file_path.write_text(note_content, encoding="utf-8")

    return {
        "status": "created",
        "file": filename
    }
@mcp.tool()
def read_note(title: str) -> dict:
    """
    Read an existing note from the notes directory.

    Args:
        title: The title of the note to read.

    Returns:
        A dictionary containing the note title and content.
        If the note does not exist, returns a not found status.
    """

    filename = generate_filename(title)
    file_path = NOTES_DIR / filename

    # Check whether the note exists
    if not file_path.exists():
        return {
            "status": "not_found",
            "file": filename
        }

    # Read the note
    content = file_path.read_text(encoding="utf-8")

    return {
        "status": "found",
        "title": title,
        "content": content
    }
@mcp.tool()
def search_notes(keyword: str) -> list[dict]:
    """
    Search all notes for a keyword or phrase.

    Args:
        keyword: The word or phrase to search for.

    Returns:
        A list of matching notes with filename and matched content.
    """

    results = []
    search_term = keyword.strip().lower()

    # Go through every Markdown file in the notes directory
    for file_path in NOTES_DIR.glob("*.md"):

        content = file_path.read_text(encoding="utf-8")

        # Check whether keyword exists in the note
        if search_term in content.lower():
            results.append({
                "file": file_path.name,
                "match": content
            })

    return results

@mcp.tool()
def update_note(title: str, content: str, mode: str = "append") -> dict:
    """
    Update an existing note by appending or replacing its content.

    Args:
        title: The title of the note to update.
        content: The new content to add or replace.
        mode: Update mode. Use "append" to add content or
              "replace" to replace the existing content.

    Returns:
        A dictionary containing the update status and filename.
    """

    filename = generate_filename(title)
    file_path = NOTES_DIR / filename

    # Check whether the note exists
    if not file_path.exists():
        return {
            "status": "not_found",
            "file": filename
        }

    # Validate update mode
    if mode not in ["append", "replace"]:
        return {
            "status": "error",
            "message": "Mode must be 'append' or 'replace'."
        }

    # Append new content
    if mode == "append":
        with file_path.open("a", encoding="utf-8") as file:
            file.write(f"\n{content.strip()}\n")

    # Replace existing content
    elif mode == "replace":
        new_content = f"# {title.strip()}\n\n{content.strip()}\n"
        file_path.write_text(new_content, encoding="utf-8")

    return {
        "status": "updated",
        "file": filename,
        "mode": mode
    }
@mcp.tool()
def delete_note(title: str) -> dict:
    """
    Delete an existing note from the notes directory.

    Args:
        title: The title of the note to delete.

    Returns:
        A dictionary containing the deletion status and filename.
    """

    filename = generate_filename(title)
    file_path = NOTES_DIR / filename

    # Check whether the note exists
    if not file_path.exists():
        return {
            "status": "not_found",
            "file": filename
        }

    # Delete the note file
    file_path.unlink()

    return {
        "status": "deleted",
        "file": filename
    }                

if __name__ == "__main__":
    mcp.run()