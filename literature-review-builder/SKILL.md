---
name: literature-review-builder
description: |
  Creates comprehensive literature reviews on any topic by synthesizing research into thematic, coherent analyses.
  Use this skill when users ask for literature reviews, research summaries, academic literature synthesis,
  or reviews of existing research on a specific topic or question.
model: sonnet
---

# Literature Review Builder

Creates literature reviews that synthesize research into coherent, theme-based analyses rather than simple source listings.

## Before Implementation

Gather context to ensure successful literature review:

| Source | Gather |
|--------|--------|
| **Codebase** | Existing writing templates, citation styles, formatting conventions |
| **Conversation** | User's research question, intended audience, specific angles to explore |
| **Skill References** | Structure patterns, best practices, anti-patterns from `references/` |
| **User Guidelines** | Academic standards, preferred citation format, length requirements |

Ensure all required context is gathered before implementing.
Only ask user for THEIR specific requirements (domain expertise is in this skill).

---

## Clarification Workflow

Before generating, ask these questions to produce quality output:

### Required Questions

**1. Topic & Research Question**
- What is the primary topic or research question?
- What specific aspect should the review focus on?

**2. Target Audience**
- Who will read this? (academic, professional, general public, students)
- What is their familiarity with the topic?

**3. Scope Parameters**
- Timeframe for sources? (e.g., last 5 years, 2020-2025, historical scope)
- Geographic/regional focus?
- Any specific types of sources required? (peer-reviewed only, industry reports, etc.)

### Optional Questions (ask if not specified)

**4. Depth & Length**
- Approximate word count or length?
- Level of detail? (overview, comprehensive, deep-dive)

**5. Structure Preference**
- Thematic (grouped by ideas/themes) - **recommended**
- Chronological (by historical development)
- Methodological (by research methods)
- Source-by-source (not recommended - produces weaker synthesis)

**6. Specific Angles**
- Any particular themes, debates, or tensions to explore?
- Key concepts or variables to examine?

**7. Output Format**
- Markdown document
- Academic paper format (with abstract, citations)
- Professional report
- Presentation slides

**8. Output File Type**
- Markdown (.md) - Default, plain text with formatting
- PDF (.pdf) - Formatted document, portable
- Word Document (.docx) - Microsoft Word compatible
- Plain Text (.txt) - Unformatted plain text
- HTML (.html) - Web-ready document

---

## Implementation Steps

### 1. Analyze the Research Scope

Define clear boundaries based on user responses:
- **In-scope**: Timeframe, source types, specific themes
- **Out-of-scope**: What will NOT be covered

### 2. Select Structure

Use **thematic structure** unless user specifies otherwise:

| Structure | When to Use | Pattern |
|-----------|-------------|---------|
| **Thematic** | Default, extensive literature | Group by concepts/ideas/debates |
| Chronological | Limited studies, historical evolution | Trace development over time |
| Methodological | Comparing research methods | Group by methodology type |

### 3. Identify Key Themes

Extract 3-6 core themes from the research area:
- Major debates or tensions in the literature
- Recurring concepts or variables
- Methodological approaches
- Populations/settings studied

### 4. Draft Section by Section

**Introduction** (~10-15% of total)
- Define scope and boundaries
- State research question/focus
- Preview structure and key themes
- For academic: identify research gap

**Body Sections** (thematic organization)
- Each section = one theme
- Synthesize sources, don't list them
- Compare and contrast findings
- Highlight tensions and contradictions
- Use subheadings for clarity

**Conclusion** (~10-15% of total)
- Synthesize key findings across themes
- Identify consensus vs. disagreement
- Highlight research gaps
- Suggest directions for future research

### 5. Apply Quality Standards

Reference `references/best-practices.md` and `references/anti-patterns.md` to avoid common mistakes.

### 6. Generate Output

Produce document in requested format with:
- Clear section headings
- Logical flow and transitions
- Proper citations (or indicate where they belong)
- Executive summary (if professional audience)
- **File type** per user specification (.md, .pdf, .docx, .txt, .html)

---

## Quality Checklist

Before delivering, verify:

### Structure & Organization
- [ ] Clear introduction defining scope and research question
- [ ] Body organized thematically (not source-by-source listing)
- [ ] Logical flow with clear transitions between sections
- [ ] Conclusion synthesizes findings across themes

### Content Quality
- [ ] Sources synthesized and integrated (not just summarized)
- [ ] Contradictions and tensions in research highlighted
- [ ] Research gaps identified
- [ ] Critical evaluation of sources (not uncritical acceptance)

### Scope & Audience
- [ ] Timeframe and source boundaries respected
- [ ] Depth appropriate for target audience
- [ ] Length matches user requirements
- [ ] Technical level appropriate for audience

### Common Anti-Patterns Avoided
- [ ] No "source-by-source" listing (see `references/anti-patterns.md`)
- [ ] Not just summarizing each source independently
- [ ] Research question clearly stated, not implicit
- [ ] Goes beyond description to analysis and synthesis

---

## When to Use References

| Reference File | When to Consult |
|----------------|-----------------|
| `references/structure-patterns.md` | Selecting and applying organization methods |
| `references/best-practices.md` | Ensuring quality standards and common patterns |
| `references/anti-patterns.md` | Checking for and avoiding common mistakes |
| `references/examples.md` | Reviewing structural examples and templates |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Too few sources for themes | Use chronological or methodological structure |
| Contradictory findings | Highlight tensions - this is valuable content |
| Unclear research question | Ask user to clarify focus before proceeding |
| Audience unclear | Default to academic readership with clear explanations |
| User wants "everything" | Push back - define scope for quality synthesis |
