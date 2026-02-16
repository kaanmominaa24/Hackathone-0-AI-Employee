#!/usr/bin/env python3
"""
AI Employee - Process Needs Action

Checks the /Needs_Action folder for any .md files, reads each one,
thinks about what to do based on Company_Handbook.md, creates a
simple Plan.md in the root with steps (checkboxes), moves the file
to /Done when processed, and updates Dashboard.md with a log entry.
"""

import os
import shutil
from datetime import datetime
from pathlib import Path
import glob


def process_needs_action_files():
    """Process all .md files in the Needs_Action folder."""

    # Define directories
    needs_action_dir = Path("./Needs_Action")
    done_dir = Path("./Done")
    root_dir = Path(".")

    # Create directories if they don't exist
    needs_action_dir.mkdir(exist_ok=True)
    done_dir.mkdir(exist_ok=True)

    # Find all .md files in Needs_Action folder
    md_files = list(needs_action_dir.glob("*.md"))

    if not md_files:
        print("No .md files found in Needs_Action folder.")
        return

    print(f"Found {len(md_files)} .md file(s) to process.")

    for md_file in md_files:
        print(f"Processing: {md_file.name}")

        # Read the content of the .md file
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        print(f"Content: {content[:200]}...")  # Print first 200 chars

        # Read Company_Handbook.md to understand company policies
        handbook_path = Path("./Company_Handbook.md")
        if handbook_path.exists():
            with open(handbook_path, 'r', encoding='utf-8') as f:
                handbook_content = f.read()
            print("Company Handbook loaded for reference.")
        else:
            print("Company_Handbook.md not found!")
            handbook_content = ""

        # Create Plan.md with steps based on the file content and handbook
        create_plan_file(content, handbook_content, md_file.name)

        # Move the processed file to /Done folder
        move_to_done(md_file, done_dir)

        # Update Dashboard.md with log entry
        update_dashboard_log(md_file.name)

        print(f"Completed processing: {md_file.name}")


def create_plan_file(content, handbook_content, filename):
    """Create Plan.md with steps based on the file content and handbook."""
    plan_path = Path("./Plan.md")

    # Extract key elements from the content to create action items
    # This is a simplified version - in a real implementation,
    # this would involve more sophisticated analysis
    action_items = [
        f"Review content of {filename}",
        "Analyze requirements based on Company Handbook",
        "Determine appropriate actions to take",
        "Execute planned actions",
        "Verify completion of tasks"
    ]

    # Read existing plan if it exists to append new items
    existing_content = ""
    if plan_path.exists():
        with open(plan_path, 'r', encoding='utf-8') as f:
            existing_content = f.read()

    # Create new plan content
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    new_content = f"""# Action Plan
Generated on: {timestamp}

## Tasks from: {filename}

"""

    for item in action_items:
        new_content += f"- [ ] {item}\n"

    new_content += "\n"

    # Combine with existing content if any
    final_content = existing_content + new_content if existing_content else new_content

    # Write to Plan.md
    with open(plan_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

    print(f"Created/updated Plan.md with tasks from {filename}")


def move_to_done(md_file, done_dir):
    """Move the processed file to the Done folder."""
    dest_path = done_dir / md_file.name

    # Handle duplicate filenames in Done folder
    counter = 1
    original_dest_path = dest_path
    while dest_path.exists():
        stem = original_dest_path.stem
        suffix = original_dest_path.suffix
        dest_path = done_dir / f"{stem}_{counter}{suffix}"
        counter += 1

    # Move the file
    shutil.move(str(md_file), str(dest_path))
    print(f"Moved {md_file.name} to Done folder as {dest_path.name}")


def update_dashboard_log(filename):
    """Update Dashboard.md with a log entry."""
    dashboard_path = Path("./Dashboard.md")

    # Read current dashboard content
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create the log entry
    date_str = datetime.now().strftime('%Y-%m-%d')
    log_entry = f"- Processed {filename} on {date_str}"

    # Find the Recent Activity section and add the log entry
    lines = content.split('\n')
    new_lines = []
    inserted = False

    for line in lines:
        new_lines.append(line)
        if line.strip() == "## Recent Activity" and not inserted:
            # Insert the log entry after the first item in Recent Activity
            # Or if there's only a placeholder, replace it
            if len(new_lines) > 0 and "No activity yet." in new_lines[-1]:
                new_lines[-1] = f"- {log_entry}"
            else:
                new_lines.append(f"- {log_entry}")
            inserted = True

    # If Recent Activity section wasn't found, append the log entry at the end
    if not inserted:
        new_lines.extend(["", "## Recent Activity", f"- {log_entry}", ""])

    # Write back to Dashboard.md
    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

    print(f"Updated Dashboard.md with log entry: {log_entry}")


def main():
    """Main function to run the needs action processor."""
    print("Starting AI Employee - Process Needs Action...")
    process_needs_action_files()
    print("Processing complete.")


if __name__ == "__main__":
    main()