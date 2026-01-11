#!/usr/bin/env python3
"""
Parse the exercises-content.txt file and create individual markdown files
for each exercise with questions and solutions.
"""

import re
import os

def read_content(filename):
    """Read the entire content file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def extract_exercises_improved(content):
    """
    Extract exercises from the content using improved logic.
    Returns a list of dicts with sheet_num, exercise_num, and content.
    """
    exercises = []
    lines = content.split('\n')
    
    # First pass: identify all sheet headers and exercise starts
    sheet_headers = {}
    exercise_starts = []
    
    for i, line in enumerate(lines):
        # Match exercise sheet headers
        sheet_match = re.search(r'E\s*XERCISE\s+S\s*HEET\s+(\d+)\s*:\s*(.+)', line)
        if sheet_match:
            sheet_num = int(sheet_match.group(1))
            sheet_title = sheet_match.group(2).strip()
            sheet_headers[i] = {
                'line': i,
                'sheet_num': sheet_num,
                'title': sheet_title
            }
        
        # Match exercise starts
        ex_match = re.match(r'^Exercise\s+(\d+)\s*(\(.*?\))?\s*:', line.strip())
        if ex_match:
            exercise_starts.append({
                'line': i,
                'exercise_num': int(ex_match.group(1)),
                'optional': ex_match.group(2) if ex_match.group(2) else "",
                'full_line': line.strip()
            })
    
    # Second pass: associate exercises with sheets and extract content
    for idx, ex_start in enumerate(exercise_starts):
        # Find which sheet this exercise belongs to
        current_sheet = None
        for sheet_line, sheet_info in sorted(sheet_headers.items(), reverse=True):
            if sheet_line < ex_start['line']:
                current_sheet = sheet_info
                break
        
        if not current_sheet:
            continue
        
        # Determine end of this exercise (start of next exercise or end of file)
        start_line = ex_start['line']
        if idx + 1 < len(exercise_starts):
            end_line = exercise_starts[idx + 1]['line']
        else:
            end_line = len(lines)
        
        # Extract content for this exercise
        exercise_content = []
        for i in range(start_line, end_line):
            line = lines[i]
            # Skip page markers
            if re.match(r'^\s*Page \d+\s*$', line):
                continue
            # Skip repeated sheet headers
            if re.search(r'E\s*XERCISE\s+S\s*HEET', line):
                continue
            exercise_content.append(line)
        
        # Join and clean content
        content_text = '\n'.join(exercise_content)
        
        # Only add if there's substantial content
        if len(content_text.strip()) > 50:
            exercises.append({
                'sheet_num': current_sheet['sheet_num'],
                'sheet_title': current_sheet['title'],
                'exercise_num': ex_start['exercise_num'],
                'optional': ex_start['optional'],
                'full_title': ex_start['full_line'],
                'content': content_text
            })
    
    return exercises

def split_question_solution(content):
    """Split content into question and solution parts."""
    # Find "Solution:" marker
    solution_pattern = r'\n\s*Solution\s*:\s*\n'
    match = re.search(solution_pattern, content, re.IGNORECASE)
    
    if match:
        question = content[:match.start()].strip()
        solution = content[match.end():].strip()
        return question, solution
    else:
        return content.strip(), ""

def clean_content(text):
    """Clean up text content."""
    # Remove excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove "M ACHINE I NTELLIGENCE" headers
    text = re.sub(r'M\s+ACHINE\s+I\s+NTELLIGENCE\s*\n', '', text)
    return text.strip()

def create_markdown(exercise):
    """Create markdown content for an exercise."""
    sheet_num = exercise['sheet_num']
    ex_num = exercise['exercise_num']
    optional = exercise['optional']
    
    # Create header
    md = f"# Exercise Sheet {sheet_num:02d}: {exercise['sheet_title']}\n\n"
    md += f"## Exercise {ex_num}{optional}\n\n"
    
    # Split into question and solution
    question, solution = split_question_solution(exercise['content'])
    
    # Remove the "Exercise X:" line from question since we already have it in header
    question = re.sub(r'^Exercise\s+\d+\s*(\(.*?\))?\s*:\s*\n?', '', question, flags=re.IGNORECASE)
    question = clean_content(question)
    
    # Add question
    md += "---\n\n"
    md += "## Question\n\n"
    md += question + "\n\n"
    
    # Add solution if exists
    if solution:
        md += "---\n\n"
        md += "## Solution\n\n"
        solution = clean_content(solution)
        md += solution + "\n"
    
    return md

def save_markdown(exercise, output_dir):
    """Save markdown file for an exercise."""
    filename = f"Sheet{exercise['sheet_num']:02d}_Exercise{exercise['exercise_num']:02d}.md"
    filepath = os.path.join(output_dir, filename)
    
    md_content = create_markdown(exercise)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return filepath

def main():
    # Read content
    print("Reading exercises-content.txt...")
    content = read_content('exercises-content.txt')
    
    # Extract exercises
    print("Extracting exercises from content...")
    exercises = extract_exercises_improved(content)
    print(f"Found {len(exercises)} exercises")
    
    # Group by sheet for summary
    sheets = {}
    for ex in exercises:
        sheet_num = ex['sheet_num']
        if sheet_num not in sheets:
            sheets[sheet_num] = []
        sheets[sheet_num].append(ex['exercise_num'])
    
    print("\nExercises by sheet:")
    for sheet_num in sorted(sheets.keys()):
        print(f"  Sheet {sheet_num:02d}: {len(sheets[sheet_num])} exercises (Ex {min(sheets[sheet_num])}-{max(sheets[sheet_num])})")
    
    # Create output directory
    output_dir = 'exercises_individual'
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each exercise
    print(f"\nCreating markdown files in '{output_dir}/'...")
    success_count = 0
    
    for exercise in exercises:
        try:
            md_file = save_markdown(exercise, output_dir)
            print(f"✓ Created: {os.path.basename(md_file)}")
            success_count += 1
        except Exception as e:
            print(f"✗ Error processing Sheet {exercise['sheet_num']} Ex {exercise['exercise_num']}: {e}")
    
    print(f"\n{'='*60}")
    print(f"Successfully created {success_count} markdown files!")
    print(f"Files saved in: {os.path.abspath(output_dir)}/")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
