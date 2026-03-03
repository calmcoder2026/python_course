# Virtual Environments in Python

## What is a Virtual Environment?
An isolated Python environment for a specific project.
It has its own installed packages, separate from system Python and other projects.

## Why Do You Need It?
Without virtual environments:
- Project A needs requests==2.25.0
- Project B needs requests==2.31.0
Both share one requests - one will break.
Virtual environments give each project its own packages.

## Create and Activate

    # Create virtual environment
    python -m venv venv

    # Activate (Mac / Linux)
    source venv/bin/activate

    # Activate (Windows)
    venv\Scripts\activate

    # Deactivate (any OS)
    deactivate

## Manage Packages

    pip install requests                # install a package
    pip install requests==2.31.0       # specific version
    pip uninstall requests              # remove package
    pip list                            # see all installed
    pip freeze > requirements.txt      # save all dependencies
    pip install -r requirements.txt    # install from file

## Real-World Use Cases
- Every professional Python project uses one
- Ensures teammates install exact same package versions
- Prevents "works on my machine" issues in deployment
- Required by most tutorials and documentation

## Common Mistakes and Tips
| Mistake | Problem | Fix |
|---|---|---|
| Committing venv/ to Git | Large unnecessary files | Add venv/ to .gitignore |
| No requirements.txt | Others cannot replicate env | Run pip freeze > requirements.txt |
| Installing globally | Conflicts between projects | Always activate venv first |

## Sample .gitignore for Python
    venv/
    __pycache__/
    *.pyc
    .env
    dist/
    build/

Tip: Think of requirements.txt as the recipe for your project dependencies.
