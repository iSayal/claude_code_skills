---
name: pdf-assessment-generator
description: |
  This skill analyzes PDF documents (academic textbooks, training materials, technical documentation) and generates comprehensive 20-question MCQ assessments to test user knowledge. It extracts key concepts, identifies important topics, and creates questions ranging from basic to advanced difficulty levels based solely on the PDF content.
allowed-tools: Read, Grep, Glob, Bash, WebSearch, WebFetch
---

# PDF Assessment Generator

This skill analyzes PDF documents and generates comprehensive 20-question MCQ assessments to test user knowledge. It works with academic textbooks, training materials, and technical documentation, creating questions ranging from basic to advanced difficulty levels based solely on the PDF content.

## When to Use This Skill

Use this skill when you need to:
- Create assessments from academic textbooks to test comprehension
- Generate quizzes from training materials for knowledge validation
- Develop MCQs from technical documentation for certification prep
- Assess understanding of content in PDF format
- Create practice tests based on provided study materials

## Prerequisites

- A PDF file containing educational content (textbooks, training materials, technical documentation)
- Access to PDF processing tools
- Understanding of the subject matter in the PDF for context

## Before Implementation

Gather context to ensure successful implementation:

| Source | Gather |
|--------|--------|
| **Codebase** | Existing PDF processing patterns, document structure, file access methods |
| **Conversation** | User's specific PDF file, subject area, target audience, desired difficulty range |
| **Skill References** | PDF extraction techniques, MCQ generation patterns, assessment best practices from `references/` |
| **User Guidelines** | Specific requirements for question types, format preferences, timing constraints |

Ensure all required context is gathered before implementing.
Only ask user for THEIR specific requirements (domain expertise is in this skill).

## Workflow

### Step 1: PDF Analysis and Content Extraction
1. Extract text content from the PDF document
2. Identify document structure (chapters, sections, headings)
3. Analyze content for key concepts, definitions, and important information
4. Categorize content by complexity level (basic, intermediate, advanced)

### Step 2: Question Generation Strategy
1. Determine question distribution across difficulty levels (e.g., 6 basic, 8 intermediate, 6 advanced)
2. Identify key terms, concepts, and facts that can form the basis of questions
3. Select appropriate question types from the following categories:
   - Factual recall questions
   - Conceptual understanding questions
   - Application-based questions
   - Analysis questions

### Step 3: MCQ Creation
1. Generate 20 multiple-choice questions based on the PDF content
2. Ensure each question has:
   - Clear, unambiguous stem
   - One correct answer
   - Three plausible distractors
   - Proper difficulty level alignment
3. Verify questions are based solely on information provided in the PDF
4. Randomize answer order to prevent pattern recognition

### Step 4: Quality Assurance
1. Review questions for accuracy and relevance to PDF content
2. Ensure questions test understanding rather than memorization
3. Verify answer choices are clear and unambiguous
4. Confirm questions span key topics from the document

## MCQ Generation Guidelines

### Question Types
- **Factual Questions**: Test recall of specific information from the PDF
- **Conceptual Questions**: Assess understanding of key concepts and principles
- **Application Questions**: Evaluate ability to apply concepts from the PDF to new situations
- **Analysis Questions**: Require synthesis and evaluation of information from the PDF

### Difficulty Levels
- **Basic**: Direct recall of facts, definitions, or simple concepts from the PDF
- **Intermediate**: Understanding of relationships, processes, or multi-step concepts
- **Advanced**: Analysis, synthesis, or application of complex ideas from the PDF

### Quality Standards
- Questions must be based solely on information provided in the PDF
- Avoid questions that require external knowledge
- Ensure answer choices are grammatically consistent with the question stem
- Distractors should be plausible but clearly incorrect
- Avoid negative phrasing where possible

## Output Format

The assessment will include:
1. 20 multiple-choice questions with four options each (A, B, C, D)
2. Difficulty level indicated for each question (Basic, Intermediate, Advanced)
3. Brief topic area or chapter reference where applicable
4. Answer key with correct responses

## Sample MCQ Structure

**Question [Number] ([Difficulty Level]):**
[Question text based on PDF content]

A) [Distractor option]
B) [Distractor option]
C) [Correct answer]
D) [Distractor option]

---

**Answer Key:**
- Question 1: C
- Question 2: A
- ...

## Error Handling

- If PDF cannot be processed, inform user of file format issues
- If insufficient content exists for 20 questions, indicate minimum content requirements
- If content is too dense or complex, suggest focus areas for question generation
- If content is too basic, adjust difficulty expectations accordingly

## Customization Options

Based on user requirements:
- Adjust difficulty distribution (more basic vs. advanced questions)
- Focus on specific chapters or sections of the PDF
- Emphasize certain types of questions (conceptual vs. factual)
- Modify number of questions if needed