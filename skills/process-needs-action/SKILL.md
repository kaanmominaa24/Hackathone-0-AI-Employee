---
name: process-needs-action
description: Process files dropped by watcher in Needs_Action folder
---

# Process Needs Action Skill

Process files dropped by watcher in Needs_Action folder.

## Core rules from Company_Handbook.md (follow strictly):
- Always be polite and clear.
- Create simple, actionable markdown notes.
- Update Dashboard.md with recent activity.
- Move processed files to /Done when finished.
- Never delete files — only move or copy.

## Step-by-step workflow for each .md file in /Needs_Action:
1. List all .md files in /Needs_Action (use ls or file system tools).
2. For each file:
   a. Read its full content.
   b. Determine what it is (file drop from watcher, so usually type: file_drop, original_name, size).
   c. Create a new markdown file in the root folder called 'Task-[date]-[original_name].md' (use current date like 2026-02-13).
   d. In the new Task file, write:
      ---
      type: task
      source: Needs_Action/[original_filename]
      created: [current ISO date/time]
      status: pending
      priority: medium
      ---
      # Task from dropped file: [original_name]

      ## Original Metadata
      [paste the full content of the Needs_Action .md here]

      ## Suggested Actions
      - [ ] Review the dropped file: [original_name]
      - [ ] Decide what to do with it (categorize, respond, archive, etc.)
      - [ ] Update relevant project note if needed
      - [ ] Mark as done when finished

      Human should review this task in Obsidian.
   e. Append a log entry to Dashboard.md under '## Recent Activity' like:
      - [ ] New task created from [original_name] – [short description] – [current time]
   f. Move the original .md file from /Needs_Action to /Done/[same name]
3. If no files in /Needs_Action, just write to Dashboard.md: 'No pending actions – last check [current time]'
4. After processing everything, confirm completion.

## Examples

### Example of processing a metadata file:
When a file like "sample_metadata.md" is found in Needs_Action, create a corresponding "Task-2026-02-13-sample_metadata.md" file with the template structure shown above, then move the original file to the Done folder.