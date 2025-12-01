from setuptools import setup, find_packages

requirements = ['adaptiveio>=1.0.2']
long_description = '# Meta Transforms Framework\n\n![py version](https://img.shields.io/badge/python-3.10+-blue) ![Version 1.0.2](https://img.shields.io/badge/version-1.0.2-brightgreen) \n\n# Events\n\n### 1. EventLog\n**Purpose:** Handles event logging and saving of events during pipeline execution.\n\n**Features:**\n- Manages the logging of events generated during the data pipeline\'s execution.\n- Provides methods to save events to a JSON file for auditing and tracking purposes.\n- Supports different logging levels and destinations.\n\n![UML diagram](../diagrams/events.png)\n\n### 2. PipelineEvent\n**Purpose:** Represents an event (e.g., loading a table, applying a transform).\n\n**Features:**\n- Stores detailed information about each event, including event type, message, description, timestamp, and a unique UUID.\n- Provides methods to format the event information as a JSON object.\n- Can be extended to represent specific types of events, such as load events or transform events.\n- Includes a log_location attribute to track where the event is logged.\n- Serves as a base class for all pipeline events, ensuring a consistent structure and interface.\n\n**Example JSON output for a load event:**\n```json\n{\n  "event_type": "load",\n  "message": "Loaded table from test.csv as csv (pyspark)",\n  "description": "Loaded test_table from test.csv",\n  "uuid": "b2e7c8e2-7d4e-4c7e-8b8e-2f6e7c8e2d4e",\n  "timestamp": "2025-08-10T12:34:56.789012",\n  "log_location": "events_log/job_1/test_table_events.json"\n}\n```\n\n## Building\n\nPrerequisites:\n- Python 3.10 or newer\n- pip, setuptools, and wheel\n\nOn Windows PowerShell:\n\n```powershell\n\n# Ensure build tools are available\npip install -U setuptools wheel\n\n# If you have project dependencies, install them (optional for building)\npip install -r requirements.txt\n\n# Build the package\npython build.py\n```\n\nWhat the build script does (python build.py):\n1. Pre-renders setup.py\n   - Reads requirements.txt (if present) and inlines them into install_requires\n   - Reads readme.md as the long_description for the package\n   - Writes a fully-populated setup.py with the package metadata (name, version, etc.)\n2. Cleans previous artifacts\n   - Deletes the build/ and dist/ folders if they exist\n3. Builds distributions\n   - Runs: python setup.py sdist bdist_wheel\n   - Outputs artifacts to the dist/ directory (e.g., .tar.gz and .whl files)\n4. Builds documentation\n   - If a docs/ folder exists, changes into docs/ and executes builddocs.bat\n   - Returns to the project root when finished\n   - For detailed instructions on building the documentation, see [Documentation Build Process](docs/docsbuild.md).\n\nAfter a successful build, you should see the generated distribution files under `dist/`.\n'

setup(
    name="transforms_events",
    version="1.0.2",
    author="",
    author_email="",
    description="A python package of a working transforms framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(include=["transforms_events", "transforms_events.*"]),
    package_data={
        "transforms_events.templates": ["*.html", "*.txt", "*.json", "*.css", "*.js"],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=requirements
)
