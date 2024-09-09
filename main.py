#!/usr/bin/env python
import os
from crew import CourseBuilderCrew


def get_required_input(prompt):
    """
    Prompt the user for input until a non-empty value is provided.
    """
    while True:
        user_input = input(f"{prompt}: ").strip()
        if user_input:
            return user_input
        else:
            print(f"{prompt} is required. Please enter a value.")


def get_user_input(prompt, default):
    """
    Prompt the user for input, returning a default value if no input is provided.
    """
    user_input = input(f"{prompt} (default: {default}): ")
    return user_input if user_input.strip() else default

def create_index_file(course, subject):
    """
    Create "course/index.md" file
    """
    # Check if the 'course' directory exists
    if not os.path.exists('course'):
        os.mkdir('course')

    # Proceed to create the 'course/index.md' file
    with open('course/index.md', 'w') as f:
        f.write(f"# {course}: {subject}\n\n")
        f.write(f"- <a href='./1_outline.md' target='course'>1_outline.md</a>\n")
        f.write(f"- <a href='./2_content.md' target='course'>2_content.md</a>\n")
        f.write(f"- <a href='./3_extended_content.md' target='course'>3_extended_content.md</a>\n")
        f.write(f"- <a href='./4_examples.md' target='course'>3_examples.md</a>\n")
        f.write(f"- <a href='./5_exercises.md' target='course'>4_exercises.md</a>\n")
        f.write(f"- <a href='./6_quiz.md' target='course'>5_quiz.md</a>\n\n")
        f.write(f"## Finale course chapters\n\n")
        f.write(f"- <a href='./final.md' target='course'>final.md</a>\n")

def replace_placeholders():
    # Define file paths
    content_file = 'course/2_content.md'
    extended_content_file = 'course/3_extended_content.md'
    examples_file = 'course/4_examples.md'
    exercises_file = 'course/5_exercises.md'
    quiz_file = 'course/6_quiz.md'
    output_file = 'course/final.md'

    # Read the content of the files
    # with open(content_file, 'r') as file:
    #     content = file.read()

    with open(extended_content_file, 'r') as file:
        content = file.read()

    with open(examples_file, 'r') as file:
        examples = file.read()

    with open(exercises_file, 'r') as file:
        exercises = file.read()

    with open(quiz_file, 'r') as file:
        quiz = file.read()

    # Replace placeholders with actual content
    content = content.replace('%examples%', examples)
    content = content.replace('%exercises%', exercises)
    content = content.replace('%quiz%', quiz)

    # Write the updated content to the output file
    with open(output_file, 'w') as file:
        file.write(content)


def run():
    """
    Run the crew.
    """
    inputs = {
        'course': get_required_input("Course about"),
        'subject': get_required_input("Subject"),
        "special_requirements": get_user_input("Do you have special requirements for this course? (is optional)", ''),
        'language': get_user_input("Language", 'English'),
        'examples': get_user_input("Number of examples", '20'),
        'exercises': get_user_input("Number of exercises", '20'),
        'quiz': get_user_input("Number of quiz questions", '20'),
        'temperature': float(get_user_input("Temperature between 0 and 1", '0.3')),
    }
    # print(f"Inputs: {inputs}")
    create_index_file(inputs['course'], inputs['subject'])
    CourseBuilderCrew(temperature=inputs['temperature']).crew().kickoff(inputs=inputs)
    # Call the function to replace placeholders
    replace_placeholders()




# Run the main function
if __name__ == "__main__":
    run()
