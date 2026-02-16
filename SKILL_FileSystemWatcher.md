# File System Watcher Skill

## Description
This skill creates a complete Python script for a File System Watcher that monitors a drop folder (e.g., /Inbox), copies new files to /Needs_Action, and creates a metadata .md file. It uses the watchdog library and runs in an infinite loop.

## Prompt Logic
```
Generate a complete Python script for a File System Watcher based on the hackathon template. It should monitor a drop folder (e.g., /Inbox), copy new files to /Needs_Action, and create a metadata .md file. Use the watchdog library. Make it run in an infinite loop.
```

## Implementation Details
- Monitors a designated inbox folder for new files
- Automatically copies new files to a Needs_Action folder
- Creates detailed metadata .md files for tracking
- Runs continuously in an infinite loop
- Handles duplicate filenames gracefully
- Includes error handling for robust operation

## Required Dependencies
- watchdog library (`pip install watchdog`)

## Files Created
- filesystem_watcher.py: Main script with complete implementation
- Inbox/: Directory created for monitoring (if it doesn't exist)
- Needs_Action/: Directory created for copied files (if it doesn't exist)

## Usage
1. Install dependencies: `pip install watchdog`
2. Run the script: `python filesystem_watcher.py`
3. Place files in the Inbox folder to trigger the watcher
4. Monitor the Needs_Action folder for copied files and metadata

## Features
- Real-time file monitoring
- Automatic file copying
- Metadata generation with timestamps and file properties
- Duplicate file handling
- Error logging
- Graceful shutdown with Ctrl+C