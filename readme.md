# Meta Transforms Framework

![py version](https://img.shields.io/badge/python-3.10+-blue) ![Version 0.20.0](https://img.shields.io/badge/version-0.20.0-brightgreen) 

# Events

### 1. EventLog
**Purpose:** Handles event logging and saving of events during pipeline execution.

**Features:**
- Manages the logging of events generated during the data pipeline's execution.
- Provides methods to save events to a JSON file for auditing and tracking purposes.
- Supports different logging levels and destinations.

![UML diagram](../diagrams/events.png)

### 2. PipelineEvent
**Purpose:** Represents an event (e.g., loading a table, applying a transform).

**Features:**
- Stores detailed information about each event, including event type, message, description, timestamp, and a unique UUID.
- Provides methods to format the event information as a JSON object.
- Can be extended to represent specific types of events, such as load events or transform events.
- Includes a log_location attribute to track where the event is logged.
- Serves as a base class for all pipeline events, ensuring a consistent structure and interface.

**Example JSON output for a load event:**
```json
{
  "event_type": "load",
  "message": "Loaded table from test.csv as csv (pyspark)",
  "description": "Loaded test_table from test.csv",
  "uuid": "b2e7c8e2-7d4e-4c7e-8b8e-2f6e7c8e2d4e",
  "timestamp": "2025-08-10T12:34:56.789012",
  "log_location": "events_log/job_1/test_table_events.json"
}
```

## Building

Prerequisites:
- Python 3.10 or newer
- pip, setuptools, and wheel

On Windows PowerShell:

```powershell

# Ensure build tools are available
pip install -U setuptools wheel

# If you have project dependencies, install them (optional for building)
pip install -r requirements.txt

# Build the package
python build.py
```

What the build script does (python build.py):
1. Pre-renders setup.py
   - Reads requirements.txt (if present) and inlines them into install_requires
   - Reads readme.md as the long_description for the package
   - Writes a fully-populated setup.py with the package metadata (name, version, etc.)
2. Cleans previous artifacts
   - Deletes the build/ and dist/ folders if they exist
3. Builds distributions
   - Runs: python setup.py sdist bdist_wheel
   - Outputs artifacts to the dist/ directory (e.g., .tar.gz and .whl files)
4. Builds documentation
   - If a docs/ folder exists, changes into docs/ and executes builddocs.bat
   - Returns to the project root when finished
   - For detailed instructions on building the documentation, see [Documentation Build Process](docs/docsbuild.md).

After a successful build, you should see the generated distribution files under `dist/`.
