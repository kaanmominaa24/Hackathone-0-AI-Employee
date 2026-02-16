# Process Needs Action Skill

## Description
This skill implements an AI Employee functionality that checks the /Needs_Action folder for any .md files, reads each one, thinks about what to do based on Company_Handbook.md, creates a simple Plan.md in the root with steps (checkboxes), moves the file to /Done when processed, and updates Dashboard.md with a log entry.

## Prompt Logic
```
Check the /Needs_Action folder for any .md files. For each, read it, think about what to do based on Company_Handbook.md, create a simple Plan.md in the root with steps (e.g., checkboxes), then move the file to /Done when processed. Update Dashboard.md with a log entry like '- Processed [file] on [date]'.
```

## Implementation Details
- Scans the Needs_Action folder for .md files
- Reads each .md file and analyzes its content
- References Company_Handbook.md for company policies
- Creates Plan.md with actionable steps (checkbox format)
- Moves processed files to the Done folder
- Updates Dashboard.md with processing logs
- Handles duplicate filenames appropriately
- Includes error handling for robust operation

## Files Created/Modified
- process_needs_action.py: Main script with complete implementation
- Plan.md: Created with actionable steps when processing files
- Dashboard.md: Updated with log entries
- Files in Needs_Action/: Moved to Done/ after processing

## Usage
1. Place .md files in the Needs_Action folder
2. Run the script: `python process_needs_action.py`
3. Check Plan.md for generated action steps
4. Verify that processed files moved to Done folder
5. Check Dashboard.md for log entries

## Features
- Automated file processing workflow
- Actionable plan generation
- Proper file organization (Needs_Action → Done)
- Detailed logging in Dashboard
- Reference to company handbook for policy compliance