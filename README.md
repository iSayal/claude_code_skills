# Claude Code Skills Collection

A curated collection of production-ready skills that extend Claude Code's capabilities across professional communication, academic research, and content creation workflows.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude-Code--orange)](https://claude.com/claude-code)

---

## About This Project

This repository contains custom **Claude Code skills** - reusable, domain-specific extensions that enhance Claude's capabilities for specialized tasks. Each skill is designed to be production-ready, zero-shot capable, and focused on solving real-world workflows.

Whether you're a freelancer, researcher, student, or professional, these skills help streamline repetitive tasks and improve output quality across various domains.

---

## Skills Overview

| Skill | Purpose | Key Use Cases |
|-------|---------|---------------|
| **Client Email Writer** | Professional client emails with warm, conversational tone | Follow-ups, status updates, relationship building |
| **English Text Improver** | Transform robotic text into natural, professional language | Business communication, document polishing |
| **Winning Upwork Proposal** | Attention-grabbing freelance proposals | Upwork applications, client pitches |
| **Literature Review Builder** | Comprehensive academic literature reviews | Research synthesis, academic writing |
| **PDF Assessment Generator** | MCQ quizzes from PDF documents | Educational assessments, knowledge testing |

---

## Available Skills

### 1. Client Email Writer (`client-email-writer`)

**Purpose**: Write professional, conversational emails to clients with a soft, approachable tone.

**Features**:
- Professional yet warm tone
- Conversational style that sounds human
- Focus on client relationship building
- Proper email etiquette and structure
- Soft approach to sensitive topics

**Use Cases**:
- Client follow-up emails
- Project status updates
- Professional correspondence
- Relationship-building communications

---

### 2. English Text Improver (`english-text-improver`)

**Purpose**: Improves English text to have a professional and soft tone while maintaining a conversational, natural style.

**Features**:
- Transforms robotic/AI-generated text into natural-sounding language
- Balances professionalism with warmth and approachability
- Maintains original message intent
- Context-aware tone adjustment
- Conversational flow enhancement

**Use Cases**:
- Business communication refinement
- Customer service message improvement
- Professional document polishing
- Content that needs human-like tone

---

### 3. Winning Upwork Proposal (`winning-upwork-proposal`)

**Purpose**: Creates compelling Upwork proposals that grab attention with relevant questions or solution hints in the first paragraph.

**Features**:
- Attention-grabbing opening paragraphs
- Avoids repeating job requirements
- Establishes understanding and showcases expertise
- Outlines clear approach
- High proposal view rate strategies
- Business type-specific adaptations
- Industry-specific language and terminology

**Use Cases**:
- Upwork proposal writing
- Freelance job applications
- Professional pitch creation
- Client acquisition communications

---

### 4. Literature Review Builder (`literature-review-builder`)

**Purpose**: Creates comprehensive literature reviews on any topic by synthesizing research into thematic, coherent analyses.

**Features**:
- Thematic organization (not source-by-source listing)
- Research synthesis and integration
- Identifies research gaps and tensions
- Multiple output formats (.md, .pdf, .docx, .txt, .html)
- Academic and professional audiences supported
- Quality standards with anti-pattern avoidance

**Use Cases**:
- Academic literature reviews
- Research summaries
- Literature synthesis for papers
- Background research for projects

---

### 5. PDF Assessment Generator (`pdf-assessment-generator`)

**Purpose**: Analyzes PDF documents and generates comprehensive 20-question MCQ assessments to test user knowledge.

**Features**:
- Works with textbooks, training materials, technical docs
- Questions ranging from basic to advanced difficulty
- Multiple question types (factual, conceptual, application, analysis)
- Answer key included
- Difficulty level indicators
- Content solely based on PDF material

**Use Cases**:
- Creating assessments from academic textbooks
- Generating quizzes from training materials
- Developing MCQs for certification prep
- Practice test creation

---

## Installation

### Prerequisites
- [Claude Code](https://claude.com/claude-code) installed on your machine
- Git installed (for cloning this repository)

### Install All Skills

```bash
# Clone this repository
git clone https://github.com/iSayal/claude_code_skills.git
cd claude_code_skills

# Copy all skills to your Claude skills directory
cp -r client-email-writer ~/.claude/skills/
cp -r english-text-improver ~/.claude/skills/
cp -r winning-upwork-proposal ~/.claude/skills/
cp -r literature-review-builder ~/.claude/skills/
cp -r pdf-assessment-generator ~/.claude/skills/
```

### Install Individual Skills

```bash
# Navigate to your Claude skills directory
cd ~/.claude/skills/

# Clone only the skill you need
git clone https://github.com/iSayal/claude_code_skills.git temp
cp -r temp/skill-name .
rm -rf temp
```

---

## Usage

Once installed, skills are automatically available in Claude Code. Reference them by name when working with Claude.

### Example Usage

**Client Email Writer**:
```
Claude, use client-email-writer to draft a follow-up email to my client about the project delay.
```

**Literature Review Builder**:
```
Use literature-review-builder to create a review on remote work productivity trends from 2020-2025.
```

**PDF Assessment Generator**:
```
Use pdf-assessment-generator to create a quiz from this textbook PDF.
```

---

## Skill Structure

Each skill follows the standard Claude Code structure:

```
skill-name/
├── SKILL.md          # Main skill definition and instructions
├── references/       # Supporting documentation and guidelines
├── assets/           # Templates and reusable resources
└── scripts/          # (Optional) executable scripts
```

---

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** this repository
2. **Create** a new branch (`git checkout -b feature/amazing-skill`)
3. **Commit** your changes (`git commit -m 'Add amazing skill'`)
4. **Push** to the branch (`git push origin feature/amazing-skill`)
5. **Open** a Pull Request

### Adding New Skills

When contributing a new skill, please ensure:
- Follows the standard skill structure
- Includes comprehensive documentation
- Has clear use cases and examples
- Follows the [Skill Validator](https://github.com/anthropics/claude-code/tree/main/docs/skills) guidelines

---

## Roadmap

- [ ] Add more specialized writing skills (grant proposals, technical docs)
- [ ] Expand language support beyond English
- [ ] Add integration examples and templates
- [ ] Create video tutorials for each skill
- [ ] Develop skill performance benchmarks

---

## Changelog

### v1.1.0 (February 2026)
- Added Literature Review Builder skill
- Improved documentation across all skills

### v1.0.1 (January 2026)
- Added PDF Assessment Generator skill

### v1.0.0 (January 2026)
- Initial release with 3 core skills
- Client Email Writer, English Text Improver, Winning Upwork Proposal

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Built for [Claude Code](https://claude.com/claude-code) by Anthropic
- Inspired by real-world workflows and user needs
- Community contributions and feedback

---

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the [Claude Code documentation](https://claude.com/claude-code/docs)
- Join the community discussions

---

<div align="center">

**Made with care for the Claude Code community**

[GitHub](https://github.com/iSayal/claude_code_skills) • [Claude Code](https://claude.com/claude-code) • [Report Issue](https://github.com/iSayal/claude_code_skills/issues)

</div>
