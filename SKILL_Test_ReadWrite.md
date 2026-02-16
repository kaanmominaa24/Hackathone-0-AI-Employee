# Test Read/Write Skill

## Description
This skill reads the Dashboard.md file, adds a new section called 'Test Update' with the current date, and writes the updated content back to the file.

## Prompt Logic
```
Read the file Dashboard.md in the current directory. Add a new section at the end called 'Test Update' with the text: '- System test successful on [current date]'. Write the updated file back to Dashboard.md.
```

## Implementation Steps
1. Check if Dashboard.md exists in the current directory
2. Read the content of Dashboard.md
3. Add 'Test Update' section with current date to the file
4. Write the updated content back to Dashboard.md
5. Confirm the update was successful

## Parameters
- Current date: Automatically inserted as YYYY-MM-DD format

## Expected Outcome
- Dashboard.md will have a new section titled 'Test Update'
- The section will contain a bullet point with the test success message and current date