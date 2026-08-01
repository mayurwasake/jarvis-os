from pathlib import Path

PROJECT_NAME = "jarvis-os"

FOLDERS = [
    ".github/workflows","docs","docs/adr","docs/architecture","docs/api","docs/diagrams","docs/developer-guide",
    "docker","scripts","examples","tests","infrastructure","frontend","desktop","mobile",
    "backend","backend/app","backend/app/api","backend/app/api/routes","backend/app/kernel",
    "backend/app/events","backend/app/contracts","backend/app/registry","backend/app/services",
    "backend/app/plugins","backend/app/lifecycle","backend/app/config","backend/app/logging",
    "backend/app/core","backend/app/utils","backend/app/tests"
]

FILES = {
"README.md":"# JARVIS OS\n\nAI Operating System.\n",
"CONTRIBUTING.md":"# Contributing\n",
"CODE_OF_CONDUCT.md":"# Code of Conduct\n",
"SECURITY.md":"# Security Policy\n",
"CHANGELOG.md":"# Changelog\n",
"LICENSE":"Apache License 2.0\n",
".gitignore":"__pycache__/\n*.pyc\n.venv/\n.env\n",
".env.example":"APP_NAME=JARVIS OS\nENV=development\n",
"docker-compose.yml":"version: '3.9'\nservices: {}\n",
".pre-commit-config.yaml":"repos: []\n",
"ruff.toml":"",
"mypy.ini":"[mypy]\npython_version = 3.12\n",
"pytest.ini":"[pytest]\n",
".github/workflows/ci.yml":"name: CI\non: [push, pull_request]\n",
"backend/pyproject.toml":"[project]\nname='jarvis-os'\nversion='0.1.0'\n",
"backend/app/__init__.py":"",
"backend/app/main.py":"""JARVIS bootstrap."""}

def main():
    print("Starting JARVIS OS...")
    print("✓ Configuration Loaded")
    print("✓ Logger Initialized")
    print("✓ Event Bus Started")
    print("✓ Registry Started")
    print("✓ Kernel Started")
    print("✓ Plugin Loader Ready")
    print("JARVIS OS is operational.")

if __name__ == "__main__":
    main()
{
"docs/adr/ADR-0001-project-vision.md":"# ADR-0001\n\nBuild a modular AI Operating System.\n",
"docs/architecture/system-overview.md":"# System Overview\n\nKernel -> Event Bus -> Registry -> Plugins\n",
"docs/developer-guide/getting-started.md":"# Getting Started\n",
"docs/api/README.md":"# API\n",
"docs/diagrams/architecture.mmd":"flowchart TD\nA[Kernel]-->B[Event Bus]\nB-->C[Registry]\nC-->D[Plugins]\n"
}

PACKAGE_DIRS = [
"backend/app/api","backend/app/api/routes","backend/app/kernel","backend/app/events",
"backend/app/contracts","backend/app/registry","backend/app/services","backend/app/plugins",
"backend/app/lifecycle","backend/app/config","backend/app/logging","backend/app/core",
"backend/app/utils","backend/app/tests"
]

root=Path(PROJECT_NAME)
for folder in FOLDERS:
    (root/folder).mkdir(parents=True, exist_ok=True)

for rel,content in FILES.items():
    p=root/rel
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content,encoding="utf-8")

for pkg in PACKAGE_DIRS:
    (root/pkg/"__init__.py").touch(exist_ok=True)

print(f"Created {PROJECT_NAME}")
