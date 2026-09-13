# Security

## Overview

This is a local CLI application with no network access, no authentication,
and no sensitive user data. Security requirements are minimal but basic
software security practices are followed throughout.

---

## Measures Implemented

### No secrets or credentials
The application has no API keys, passwords, database credentials, or tokens.
Nothing sensitive is stored anywhere in the codebase.

### Input validation
All user input is validated before use:
- Menu choices are checked against a known set of valid options
- Task titles are checked to be non-empty
- Priority values are checked against an allowed list
- Due dates are validated with datetime.strptime before being stored
- Task IDs are checked to be integers and to exist in the list

This prevents bad data from being stored or causing unexpected behaviour.

### No use of eval() or exec()
User input is never passed to eval(), exec(), or any function that executes
arbitrary code. All input is treated as plain text.

### No unsafe file operations
File paths are not constructed from user input, so path traversal attacks
are not possible. The data file path is a fixed constant in storage.py.

### No personal data stored
The application stores only task content entered by the user (title,
description, priority, due date). No names, emails, passwords, or other
personal data are collected or stored.

### No secrets committed to Git
The .gitignore excludes .env files. No credentials exist to commit.

---

## What Is Not Applicable

| Security Concern         | Status        | Reason                               |
|--------------------------|---------------|--------------------------------------|
| Authentication/login     | NOT NEEDED    | Single-user local application        |
| HTTPS/TLS                | NOT NEEDED    | No network communication             |
| SQL injection            | NOT NEEDED    | No database used                     |
| API key management       | NOT NEEDED    | No external APIs used                |
| Rate limiting            | NOT NEEDED    | No server or API                     |
| Data encryption          | NOT NEEDED    | No sensitive data stored             |
