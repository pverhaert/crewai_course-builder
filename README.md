# Course Builder with CrewAI

This repository utilizes [CrewAI](https://www.crewai.com/) to generate comprehensive course materials, particularly suited for
programming language courses.

## Generated Files

The crew produces six key files:

1. `1_outline.md`: A structured outline for a specific subject within the course.
2. `2_content.md`: The core content of the course, based on the outline.
3. `3_extended_content.md`: A more detailed and in-depth version of the content.
4. `4_examples.md`: Practical examples related to the subject.
5. `5_exercises.md`: Hands-on exercises for learners.
6. `6_quiz.md`: Kahoot-style questions to test understanding.
7. `final.md`: A complete version of the course, combining extended content, examples, exercises, and quiz questions.

## Important Notes

- Always verify the generated content for accuracy, as AI models can produce inaccuracies.
- Each run of the crew overwrites previous output files. Back up any content you wish to keep.
- Multiple runs can produce slightly different content, offering variety.
- Experiment with different AI models to find the best fit for your needs.
- For non-English courses, ensure the chosen model supports multiple languages.
- Consider the generated content as a starting point for further refinement.

## Setup Requirements

- [Git](https://git-scm.com/)
- [Python](https://www.python.org) version 3.10.x or 3.11.x

## Installation

1. Clone the repository: `git clone git clone https://github.com/pverhaert/crewai_course-builder`
2. Set up the environment:
    - **Windows**: Run `install.bat` to create the virtual environment, install dependencies, and set up the `.env`
      file.
    - **Linux/macOS**:
        - Create and activate a virtual environment named `.venv`
        - Activate the virtual environment: `source .venv/bin/activate`
        - Install dependencies: `pip install -r requirements.txt`
        - Rename `.env.example` to `.env`

## LLM Configuration

Choose between [Groq](https://groq.com/) or [OpenRouter](https://openrouter.ai/) models. The free [Serper](https://serper.dev/) API is used
for internet searches.

### Serper Setup

1. Get an API key from [Serper](https://serper.dev/api-key)
2. Add the key to the `.env` file: 
```
SERPER_API_KEY=your_key_here`
```

### Groq Setup

1. Obtain an API key from [Groq Console](https://console.groq.com/keys)
2. Select a [model](https://console.groq.com/docs/models)
3. Update `.env` with your API key and chosen model:
````markdown
OPENAI_API_KEY=your_groq_api_key
OPENAI_MODEL_NAME=your_chosen_model
OPENAI_API_BASE=https://api.groq.com/openai/v1
````

### OpenRouter Setup

1. Get an API key from [OpenRouter](https://openrouter.ai/settings/keys)
2. Choose a [model](https://openrouter.ai/models)
3. In `.env`, comment out Groq settings and uncomment OpenRouter settings:
````markdown
OPENAI_API_KEY=your_openrouter_api_key
OPENAI_API_BASE=https://openrouter.ai/api/v1
OPENAI_MODEL_NAME=your_chosen_model
````

## Running the Crew

- **Windows**: Execute `run.bat`
- **Linux/macOS**: Run `python main.py`

## Input Parameters

When running the crew, you'll be prompted to provide:

- Course about (e.g., "JavaScript")
- Subject (e.g., "Functions")
- Do you have special requirements for this course? (optional)
- Language of the course
- Number of examples, exercises, and quiz questions
- Temperature setting for AI generation (0-1)

## Accessing Generated Content

Find the generated course materials in the `course` folder, all in Markdown format.

**Tip**:
- Install
the [Markdown Viewer](https://chromewebstore.google.com/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk) Chrome
extension for easy viewing.
- Remember to [allow access to local files](https://github.com/simov/markdown-viewer?tab=readme-ov-file#manage-origins).
