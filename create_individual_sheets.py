#!/usr/bin/env python3
"""
Create individual solution files for each exercise sheet.
Each file contains all exercises from that sheet with questions and solutions.
"""

import os
import re
from pathlib import Path

# Exercise sheet information
EXERCISE_SHEETS = [
    {"num": "01", "title": "Intelligent Agents", "filename": "agents"},
    {"num": "02", "title": "Constraint Satisfaction Problems", "filename": "csp"},
    {"num": "03", "title": "Reasoning Under Uncertainty", "filename": "uncertainty"},
    {"num": "04", "title": "Bayesian Network Inference", "filename": "bn-inference"},
    {"num": "05", "title": "Supervised Learning", "filename": "supervised-learning"},
    {"num": "06", "title": "Neural Networks", "filename": "neural-networks"},
    {"num": "07", "title": "Learning Evaluation", "filename": "learning-evaluation"},
    {"num": "08", "title": "Clustering", "filename": "clustering"},
    {"num": "09", "title": "Search", "filename": "search"},
    {"num": "10", "title": "Planning", "filename": "planning"},
    {"num": "11", "title": "Multi-Agent Systems", "filename": "multi-agent"},
    {"num": "12", "title": "Markov Decision Processes", "filename": "mdps"},
    {"num": "13", "title": "Reinforcement Learning", "filename": "reinforcement-learning"},
]

def read_file(filepath):
    """Read file content."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read()
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return ""

def clean_text(text):
    """Clean up extracted text."""
    # Remove multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove page markers
    text = re.sub(r'\n\s*Page \d+\s*\n', '\n', text)
    # Remove repeated headers
    text = re.sub(r'M\s+ACHINE\s+I\s+NTELLIGENCE\s*\n', '', text)
    text = re.sub(r'E\s+XERCISE\s+S\s+HEET\s+\d+\s*:.*?\n', '', text)
    return text.strip()

def extract_exercises_detailed(question_text, solution_text, sheet_num):
    """Extract individual exercises with their questions and solutions."""
    exercises = []
    
    # Split by "Exercise N :" pattern
    exercise_pattern = r'Exercise\s+(\d+)\s*(?:\(.*?\))?\s*:'
    
    # Find all exercise starts in questions
    question_matches = list(re.finditer(exercise_pattern, question_text))
    
    for i, q_match in enumerate(question_matches):
        ex_num = q_match.group(1)
        
        # Extract question content
        q_start = q_match.end()
        q_end = question_matches[i+1].start() if i+1 < len(question_matches) else len(question_text)
        question_content = question_text[q_start:q_end].strip()
        
        # Find corresponding solution in the solution text
        solution_content = ""
        
        # Look for this exercise number in solution text
        solution_pattern = rf'Exercise\s+{ex_num}\s*(?:\(.*?\))?\s*:'
        solution_matches = list(re.finditer(solution_pattern, solution_text))
        
        if solution_matches:
            s_match = solution_matches[0]
            s_start = s_match.end()
            
            # Find the next exercise or end of file
            next_ex_pattern = r'Exercise\s+\d+\s*(?:\(.*?\))?\s*:'
            remaining_text = solution_text[s_start:]
            next_match = re.search(next_ex_pattern, remaining_text)
            
            if next_match:
                s_end = s_start + next_match.start()
            else:
                s_end = len(solution_text)
            
            solution_raw = solution_text[s_start:s_end].strip()
            
            # Parse sub-parts if they exist
            solution_content = parse_solution_parts(solution_raw, question_content)
        
        exercises.append({
            'sheet': sheet_num,
            'number': ex_num,
            'question': clean_text(question_content),
            'solution': clean_text(solution_content) if solution_content else "*Solution not available*"
        })
    
    return exercises

def parse_solution_parts(solution_text, question_text):
    """Parse solutions with multiple parts (a), (b), (c), etc."""
    # Check if question has parts
    has_parts = bool(re.search(r'\([a-z]\)', question_text))
    
    if has_parts:
        # Split solution by parts
        parts = re.split(r'\n\s*\(([a-z])\)', solution_text)
        
        if len(parts) > 1:
            formatted_solution = ""
            for i in range(1, len(parts), 2):
                if i < len(parts):
                    part_letter = parts[i]
                    part_content = parts[i+1].strip() if i+1 < len(parts) else ""
                    
                    # Extract the actual solution (after "Solution:")
                    solution_match = re.search(r'Solution\s*:\s*(.*)', part_content, re.DOTALL)
                    if solution_match:
                        part_content = solution_match.group(1).strip()
                    
                    formatted_solution += f"**({part_letter})**\n\n{part_content}\n\n"
            
            return formatted_solution.strip()
    
    # Single solution or no parts
    solution_match = re.search(r'Solution\s*:\s*(.*)', solution_text, re.DOTALL)
    if solution_match:
        return solution_match.group(1).strip()
    
    return solution_text

def create_sheet_markdown(sheet_info, exercises):
    """Create markdown file for a single sheet."""
    md = f"""# Exercise Sheet {sheet_info['num']}: {sheet_info['title']}

**Course:** Machine Intelligence  
**Sheet Number:** {sheet_info['num']}  
**Total Exercises:** {len(exercises)}

---

## Overview

This document contains all exercises from Sheet {sheet_info['num']} with complete solutions.
Each exercise includes:
- 📝 **Question**: The complete problem statement
- ✅ **Solution**: Step-by-step solution with explanations

---

## Table of Contents

"""
    
    # Add TOC
    for ex in exercises:
        md += f"- [Exercise {ex['number']}](#exercise-{ex['number']})\n"
    
    md += "\n---\n\n"
    
    # Add each exercise
    for i, ex in enumerate(exercises, 1):
        md += f"## Exercise {ex['number']}\n\n"
        
        # Question section
        md += "### 📝 Question\n\n"
        md += ex['question'] + "\n\n"
        
        # Solution section
        md += "### ✅ Solution\n\n"
        md += ex['solution'] + "\n\n"
        
        # Separator between exercises
        if i < len(exercises):
            md += "---\n\n"
    
    # Footer
    md += f"""
---

## Summary

**Sheet {sheet_info['num']}: {sheet_info['title']}**  
✅ Total Exercises: {len(exercises)}  
📚 All solutions provided with detailed explanations

---

*Machine Intelligence Course - Exercise Solutions*
"""
    
    return md

def main():
    print("="*80)
    print("Creating Individual Sheet Solution Files")
    print("="*80)
    print()
    
    # Create output directory
    output_dir = "Solutions_By_Sheet"
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}/")
    print()
    
    total_exercises = 0
    total_sheets = 0
    
    for sheet in EXERCISE_SHEETS:
        sheet_num = sheet['num']
        sheet_title = sheet['title']
        filename = sheet['filename']
        
        print(f"Processing Sheet {sheet_num}: {sheet_title}...")
        
        # Read question and solution files
        question_file = f"extracted_content/exercises-{sheet_num}-{filename}.txt"
        solution_file = f"extracted_content/exercises-{sheet_num}-{filename}-solutions.txt"
        
        if not os.path.exists(question_file):
            print(f"  ⚠️  Question file not found: {question_file}")
            continue
        
        if not os.path.exists(solution_file):
            print(f"  ⚠️  Solution file not found: {solution_file}")
            continue
        
        # Read files
        question_text = read_file(question_file)
        solution_text = read_file(solution_file)
        
        if not question_text or not solution_text:
            print(f"  ⚠️  Empty file(s)")
            continue
        
        # Extract exercises
        exercises = extract_exercises_detailed(question_text, solution_text, sheet_num)
        
        if not exercises:
            print(f"  ⚠️  No exercises found")
            continue
        
        print(f"  ✓ Found {len(exercises)} exercises")
        
        # Create markdown
        md_content = create_sheet_markdown(sheet, exercises)
        
        # Save markdown file
        output_filename = f"Sheet{sheet_num}_{filename.replace('-', '_')}_solutions.md"
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"  ✓ Created: {output_filename}")
        
        total_exercises += len(exercises)
        total_sheets += 1
    
    print()
    print("="*80)
    print(f"✅ Successfully processed {total_sheets} exercise sheets")
    print(f"   Total exercises: {total_exercises}")
    print(f"   Output directory: {os.path.abspath(output_dir)}/")
    print("="*80)
    
    # Create index file
    create_index(output_dir, EXERCISE_SHEETS)

def create_index(output_dir, sheets):
    """Create an index/README file."""
    index_content = """# Machine Intelligence - Exercise Solutions by Sheet

This directory contains individual solution files for each exercise sheet.
Each file includes all exercises from that sheet with complete questions and step-by-step solutions.

## Files

"""
    
    for sheet in sheets:
        filename = f"Sheet{sheet['num']}_{sheet['filename'].replace('-', '_')}_solutions.md"
        filepath = os.path.join(output_dir, filename)
        
        if os.path.exists(filepath):
            # Count exercises in file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                ex_count = len(re.findall(r'^## Exercise \d+', content, re.MULTILINE))
            
            index_content += f"### {sheet['num']}. [{sheet['title']}]({filename})\n"
            index_content += f"   - {ex_count} exercises with complete solutions\n\n"
    
    index_content += """
## How to Use

1. **Select a sheet** from the list above
2. **Read each exercise** carefully
3. **Try solving it yourself** first
4. **Check the solution** for detailed explanations
5. **Review concepts** you find challenging

## Additional Resources

- **COMPREHENSIVE_SOLUTIONS.md** - All exercises in one document
- **COMPREHENSIVE_SOLUTIONS.pdf** - PDF version of all exercises

---

*Machine Intelligence Course Materials*
"""
    
    index_path = os.path.join(output_dir, "README.md")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"\n✓ Created index: {output_dir}/README.md")

if __name__ == '__main__':
    main()

