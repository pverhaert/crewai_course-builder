import os

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.tools import DuckDuckGoSearchRun
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI


@CrewBase
class CourseBuilderCrew():
    """CourseBuilder crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # web_search = DuckDuckGoSearchRun()

    def __init__(self, temperature=0.3) -> None:
        self.llm = ChatOpenAI(
            api_key=os.environ['OPENAI_API_KEY'],
            base_url=os.environ['OPENAI_API_BASE'],
            model=os.environ['OPENAI_MODEL_NAME'],
            temperature=temperature,
        )
        self.search_tool = SerperDevTool()

    @agent
    def course_outline_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['course_outline_creator'],
            allow_delegation=False,
            tools=[],
            verbose=True
        )

    @agent
    def course_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['course_writer'],
            allow_delegation=False,
            # tools=[DuckDuckGoSearchRun()],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def course_enhancer(self) -> Agent:
        return Agent(
            config=self.agents_config['course_enhancer'],
            allow_delegation=False,
            # tools=[],
            verbose=True
        )

    @agent
    def example_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['example_creator'],
            allow_delegation=False,
            tools=[],
            verbose=True
        )

    @agent
    def exercise_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['exercise_creator'],
            allow_delegation=False,
            tools=[],
            verbose=True
        )

    @agent
    def quiz_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['quiz_creator'],
            allow_delegation=False,
            tools=[],
            verbose=True
        )

    @task
    def create_course_outline(self) -> Task:
        return Task(
            config=self.tasks_config['create_course_outline_task'],
            output_file='course/1_outline.md'
        )

    @task
    def write_course_content(self) -> Task:
        return Task(
            config=self.tasks_config['write_course_content_task'],
            output_file='course/2_content.md'
        )

    @task
    def enhance_course_content(self) -> Task:
        return Task(
            config=self.tasks_config['enhance_course_content_task'],
            output_file='course/3_extended_content.md'
        )
    @task
    def create_examples(self) -> Task:
        return Task(
            config=self.tasks_config['create_examples_task'],
            output_file='course/4_examples.md'
        )

    @task
    def create_exercises(self) -> Task:
        return Task(
            config=self.tasks_config['create_exercises_task'],
            output_file='course/5_exercises.md'
        )

    @task
    def create_quizzes(self) -> Task:
        return Task(
            config=self.tasks_config['create_quiz_task'],
            output_file='course/6_quiz.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CourseBuilder crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
