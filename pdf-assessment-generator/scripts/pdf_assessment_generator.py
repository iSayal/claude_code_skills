#!/usr/bin/env python3
"""
PDF Content Analyzer for Assessment Generation
This script extracts content from PDFs and prepares it for MCQ generation.
"""

import sys
import re
from typing import List, Dict, Tuple

def extract_pdf_content(pdf_path: str) -> Dict:
    """
    Extract content from PDF file for assessment generation.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        Dictionary containing extracted content organized by sections
    """
    try:
        import PyPDF2
    except ImportError:
        print("PyPDF2 library is required. Install with: pip install PyPDF2")
        return {}

    content = {
        "title": "",
        "sections": [],
        "key_terms": [],
        "concepts": [],
        "text": ""
    }

    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            # Extract all text
            all_text = []
            for page_num, page in enumerate(pdf_reader.pages):
                text = page.extract_text()
                all_text.append(text)

            full_text = "\n".join(all_text)
            content["text"] = full_text

            # Identify potential sections based on headers (simple heuristic)
            # Look for patterns that might indicate section headers
            lines = full_text.split('\n')
            sections = []
            current_section = {"title": "Introduction", "content": []}

            for line in lines:
                line = line.strip()
                if len(line) < 150:  # Potential header (short line)
                    # Check if it looks like a header (capitalized, no punctuation at end, etc.)
                    if line.isupper() or (line.istitle() and not line.endswith('.')):
                        if current_section["content"]:  # Save previous section
                            sections.append(current_section)
                        current_section = {"title": line, "content": []}
                    else:
                        current_section["content"].append(line)
                else:
                    current_section["content"].append(line)

            if current_section["content"]:
                sections.append(current_section)

            content["sections"] = sections

            # Extract key terms (words that appear frequently and might be important)
            words = re.findall(r'\b[A-Za-z]{4,}\b', full_text.lower())
            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1

            # Get top 50 most frequent words as potential key terms
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            content["key_terms"] = [word for word, freq in sorted_words[:50]]

            return content

    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return {}

def analyze_content_for_questions(content: Dict) -> List[Dict]:
    """
    Analyze content and identify potential question topics.

    Args:
        content: Content dictionary from extract_pdf_content

    Returns:
        List of potential question topics with difficulty levels
    """
    questions_topics = []

    # Simple heuristics for identifying question-worthy content
    text = content["text"]

    # Look for definition patterns: "X is defined as..." or "X refers to..."
    definitions = re.findall(r'([A-Z][a-zA-Z\s]{4,100})\s+(?:is defined as|refers to|are|is)\s+([^.\n]{10,150})\.', text)

    for term, definition in definitions:
        topic = {
            "type": "definition",
            "term": term.strip(),
            "definition": definition.strip(),
            "difficulty": "basic",
            "section": "General"
        }
        questions_topics.append(topic)

    # Look for numbered lists which often indicate important points
    lists = re.findall(r'\d+\.\s*([^.!?]{10,100})', text)
    for item in lists:
        topic = {
            "type": "factual",
            "content": item.strip(),
            "difficulty": "intermediate",
            "section": "General"
        }
        questions_topics.append(topic)

    # Look for cause and effect relationships for application questions
    causation_patterns = re.findall(r'([^.!?]{5,100}?)\s+(?:because|since|due to|as a result of|therefore|thus)\s+([^.!?]{5,100}?)', text)
    for cause, effect in causation_patterns:
        topic = {
            "type": "application",
            "cause": cause.strip(),
            "effect": effect.strip(),
            "difficulty": "advanced",
            "section": "General"
        }
        questions_topics.append(topic)

    return questions_topics

def generate_mcq_questions(topics: List[Dict], num_questions: int = 20) -> List[Dict]:
    """
    Generate MCQ questions from topic list.

    Args:
        topics: List of potential question topics
        num_questions: Number of questions to generate (default 20)

    Returns:
        List of MCQ questions with options
    """
    questions = []

    # Distribute questions by difficulty: 30% basic, 40% intermediate, 30% advanced
    difficulty_dist = {
        "basic": int(num_questions * 0.3),
        "intermediate": int(num_questions * 0.4),
        "advanced": int(num_questions * 0.3)
    }

    # Group topics by difficulty
    topics_by_difficulty = {"basic": [], "intermediate": [], "advanced": []}
    for topic in topics:
        difficulty = topic.get("difficulty", "intermediate")
        if difficulty in topics_by_difficulty:
            topics_by_difficulty[difficulty].append(topic)

    # Generate questions for each difficulty level
    for difficulty, count in difficulty_dist.items():
        available_topics = topics_by_difficulty[difficulty]
        for i in range(min(count, len(available_topics))):
            topic = available_topics[i]

            question_data = {
                "question": "",
                "options": ["", "", "", ""],
                "correct_answer": "",
                "difficulty": difficulty,
                "topic_category": topic.get("type", "general")
            }

            # Generate question based on topic type
            if topic["type"] == "definition":
                question_data["question"] = f"What is {topic['term']}?"
                question_data["options"] = [
                    topic["definition"],
                    "Another possible definition",
                    "Yet another possible definition",
                    "One more possible definition"
                ]
                question_data["correct_answer"] = topic["definition"]
            elif topic["type"] == "factual":
                question_data["question"] = f"Which of the following is true about {topic['content'][:50]}...?"
                question_data["options"] = [
                    topic["content"],
                    "Another fact",
                    "Different fact",
                    "Additional fact"
                ]
                question_data["correct_answer"] = topic["content"]
            elif topic["type"] == "application":
                question_data["question"] = f"What is the result of {topic['cause']}?"
                question_data["options"] = [
                    topic["effect"],
                    "Alternative outcome",
                    "Different result",
                    "Other possibility"
                ]
                question_data["correct_answer"] = topic["effect"]
            else:
                # General question type
                question_data["question"] = f"According to the content, which statement is correct about {topic.get('term', 'the topic')}?"
                question_data["options"] = [
                    topic.get("content", "Main content"),
                    "Alternative statement",
                    "Different perspective",
                    "Opposing view"
                ]
                question_data["correct_answer"] = topic.get("content", "Main content")

            # Shuffle options to randomize correct answer position
            import random
            options = question_data["options"]
            correct = question_data["correct_answer"]

            # Ensure correct answer is in options and shuffle
            if correct in options:
                idx = options.index(correct)
                random.shuffle(options)
                # Update correct answer index after shuffle
                correct_idx = options.index(question_data["correct_answer"])
                # Keep the correct answer as a reference
                question_data["options"] = options
                question_data["answer_index"] = correct_idx  # Store index of correct answer (0-3)

            questions.append(question_data)

    return questions

def main():
    if len(sys.argv) != 2:
        print("Usage: python pdf_analyzer.py <pdf_file_path>")
        sys.exit(1)

    pdf_path = sys.argv[1]

    print(f"Analyzing PDF: {pdf_path}")
    content = extract_pdf_content(pdf_path)

    if not content:
        print("Failed to extract content from PDF")
        sys.exit(1)

    print(f"Extracted content with {len(content['sections'])} sections")

    topics = analyze_content_for_questions(content)
    print(f"Identified {len(topics)} potential question topics")

    questions = generate_mcq_questions(topics, 20)
    print(f"\nGenerated {len(questions)} MCQ questions:")

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i} ({q['difficulty'].title()}): {q['question']}")
        print(f"  A) {q['options'][0]}")
        print(f"  B) {q['options'][1]}")
        print(f"  C) {q['options'][2]}")
        print(f"  D) {q['options'][3]}")
        correct_option = ['A', 'B', 'C', 'D'][q.get('answer_index', 0)]
        print(f"  Correct Answer: {correct_option}")

if __name__ == "__main__":
    main()