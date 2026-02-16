#!/usr/bin/env python3
"""
AI Employee File System Watcher

Monitors a drop folder (Inbox), copies new files to Needs_Action,
and creates metadata .md files for tracking.
"""

import os
import shutil
import time
from datetime import datetime
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class InboxHandler(FileSystemEventHandler):
    """Handles file system events in the inbox folder."""

    def __init__(self, inbox_dir, needs_action_dir):
        self.inbox_dir = Path(inbox_dir)
        self.needs_action_dir = Path(needs_action_dir)

        # Create destination directory if it doesn't exist
        self.needs_action_dir.mkdir(parents=True, exist_ok=True)

    def on_created(self, event):
        """Handle file creation events."""
        if not event.is_directory:
            self.process_new_file(event.src_path)

    def on_moved(self, event):
        """Handle file move events."""
        if not event.is_directory and event.dest_path:
            self.process_new_file(event.dest_path)

    def process_new_file(self, file_path):
        """Process a new file by copying it and creating metadata."""
        try:
            file_path = Path(file_path)

            # Wait briefly to ensure file is completely written
            time.sleep(0.5)

            if not file_path.exists():
                return

            # Copy file to Needs_Action directory
            dest_path = self.needs_action_dir / file_path.name
            counter = 1

            # Handle duplicate filenames
            original_dest_path = dest_path
            while dest_path.exists():
                stem = original_dest_path.stem
                suffix = original_dest_path.suffix
                dest_path = self.needs_action_dir / f"{stem}_{counter}{suffix}"
                counter += 1

            shutil.copy2(file_path, dest_path)
            print(f"Copied {file_path.name} to {dest_path}")

            # Create metadata .md file
            self.create_metadata_file(file_path, dest_path)

        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")

    def create_metadata_file(self, original_path, copied_path):
        """Create a metadata .md file for the copied file."""
        try:
            original_path = Path(original_path)
            copied_path = Path(copied_path)

            # Create metadata filename
            meta_filename = f"{original_path.stem}_metadata.md"
            meta_path = self.needs_action_dir / meta_filename

            # Get file stats
            stat = original_path.stat()
            file_size = stat.st_size
            created_time = datetime.fromtimestamp(stat.st_ctime)
            modified_time = datetime.fromtimestamp(stat.st_mtime)

            # Write metadata file
            with open(meta_path, 'w', encoding='utf-8') as f:
                f.write(f"# Metadata for {original_path.name}\n\n")
                f.write(f"- **Original Path:** {original_path}\n")
                f.write(f"- **Copied To:** {copied_path}\n")
                f.write(f"- **Size:** {file_size} bytes\n")
                f.write(f"- **Created:** {created_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"- **Modified:** {modified_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"- **Processed At:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"- **Status:** New - Needs Action\n")
                f.write(f"- **Priority:** Medium\n\n")
                f.write("## Notes\n\n")
                f.write("- File requires review and action\n")

            print(f"Created metadata file: {meta_path.name}")

        except Exception as e:
            print(f"Error creating metadata for {original_path}: {str(e)}")


def main():
    """Main function to run the file system watcher."""
    # Define directories
    inbox_dir = Path("./Inbox")
    needs_action_dir = Path("./Needs_Action")

    # Create directories if they don't exist
    inbox_dir.mkdir(parents=True, exist_ok=True)
    needs_action_dir.mkdir(parents=True, exist_ok=True)

    # Create event handler and observer
    event_handler = InboxHandler(inbox_dir, needs_action_dir)
    observer = Observer()
    observer.schedule(event_handler, str(inbox_dir), recursive=False)

    # Start the observer
    observer.start()
    print(f"File System Watcher started.")
    print(f"Monitoring: {inbox_dir.absolute()}")
    print(f"Copying to: {needs_action_dir.absolute()}")
    print("Press Ctrl+C to stop.")

    try:
        # Run indefinitely
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopping File System Watcher...")

    observer.join()
    print("File System Watcher stopped.")


if __name__ == "__main__":
    main()