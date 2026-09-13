

 # KIRO CLI — STRICT MASTER PROJECT PROMPT

 ## ROLE

 You are the implementation agent for this project.

 You must follow the project requirements, constraints, documentation requirements, testing requirements, and approval rules in this prompt exactly.

 This is a student mini-project based on the provided Day 6/Day 7 project brief.

 Your primary objective is:

 > Build a complete, working, understandable, zero-cost project that satisfies the assignment requirements and can be demonstrated live.

---

 # 1\. SOURCE OF TRUTH

 The project brief provided by the user is the primary source of truth.

 The assignment requires:

 - A CLI tool
- A real problem being solved
- At least 3 non-trivial functions
- At least 1 class
- File I/O using JSON/CSV/text OR an API call
- Error handling using appropriate `try/except`
- A clear CLI/interface
- README.md
- GitHub-ready project
- At least 5 meaningful Git commits
- PEP 8 compliant/readable Python code
- Working application
- No crashes on invalid input
- Ability for the student to understand and explain the code

 Do NOT change these requirements.

---

 # 2\. ABSOLUTE NO-SCOPE-CREEP RULE

 This is extremely important.

 DO NOT add functionality that is not required by the actual project.

 DO NOT add:

 - Extra features
- Extra pages
- Extra APIs
- Extra frameworks
- Extra databases
- Extra cloud services
- Extra libraries
- Extra authentication
- Extra infrastructure
- Extra architecture
- Extra UI
- Extra configuration
- Extra automation
- Extra DevOps
- Extra AWS services
- Extra PostgreSQL infrastructure
- Extra dependencies

 unless they are necessary to satisfy the actual project requirements.

 If you believe something additional is necessary:

 STOP.

 Do NOT install it.

 Do NOT implement it.

 Do NOT modify the architecture.

 Ask me for explicit permission first.

---

 # 3\. ZERO-COST REQUIREMENT

 The entire project must be designed to cost ₹0 / $0 to build, test and demonstrate whenever technically possible.

 Prefer:

 - Python standard library
- Local files
- Local development
- Free/open-source software
- Free testing tools
- Local execution

 Avoid paid services.

 DO NOT:

 - Create paid cloud resources
- Create AWS resources that may generate charges
- Enable paid APIs
- Subscribe to services
- Require credit cards
- Use paid databases
- Use paid hosting
- Use paid APIs
- Use paid monitoring
- Use paid storage

 without my explicit approval.

---

 # 4\. AWS RULE

 AWS is NOT automatically required.

 Before using AWS, determine whether the assignment genuinely requires cloud deployment.

 If AWS is not required:

 DO NOT use AWS.

 If AWS would introduce any cost:

 DO NOT use it.

 If AWS appears useful but is not necessary:

 DO NOT add it.

 Ask me before using AWS.

---

 # 5\. POSTGRESQL 17 RULE

 PostgreSQL 17 is NOT automatically required by the assignment.

 The assignment specifically allows JSON/CSV/text file I/O.

 Therefore:

 Use local JSON/CSV/text storage unless PostgreSQL 17 is genuinely required by the selected project.

 DO NOT add PostgreSQL merely because it was mentioned in this prompt.

 If you believe PostgreSQL 17 is necessary:

 STOP and ask me for permission before implementing it.

 The same rule applies to any database.

---

 # 6\. WEB/UI RULE

 This assignment is primarily a CLI project.

 DO NOT create a web application unless the selected project requirements genuinely require it.

 DO NOT automatically add:

 - React
- TypeScript
- HTML
- CSS
- JavaScript
- Flask
- FastAPI
- Django
- Node.js

 If a CLI is sufficient, build ONLY the CLI.

 The CLI itself must have a clear and user-friendly interface.

---

 # 7\. PYTHON REQUIREMENT

 Use Python 3.13+ as specified by the assignment.

 Follow PEP 8.

 Use:

 - Clear variable names
- Clear function names
- Small understandable functions
- Appropriate classes
- Useful comments only where necessary
- Proper error handling
- Maintainable project structure

 Avoid unnecessary abstraction.

 The project should remain simple enough for a student to explain every important part.

---

 # 8\. FIRST ACTION — DO NOT CODE

 Before writing implementation code:

 Analyze the project brief carefully.

 Then determine:

 1. What exact project is being built?
2. What real problem does it solve?
3. Who is the user?
4. What are the minimum required features?
5. Which assignment requirements apply?
6. Which features are optional?
7. What data must be stored?
8. What inputs can be invalid?
9. What errors can occur?
10. What test cases are required?
11. What files are required?
12. What dependencies are actually necessary?
13. Can everything run locally at zero cost?

 Do not start implementation yet.

---

 # 9\. REQUIRED DOCUMENTATION FILES

 Before implementation, create the following planning/documentation files.

 ## Required

```
README.md
requirements.md
design.md
tasks.md
testing.md
test-cases.md
setup-and-run.md
skills.md
error-logs.md
sample-output.md
architecture.md
security.md
data-model.md
project-scope.md
change-log.md
known-issues.md
```

 Also create:

```
.env.example
.gitignore
run.sh
```

 If `.env` is genuinely required, create:

```
.env
```

 BUT:

 NEVER place real secrets, passwords, API keys, tokens, credentials, or private information into `.env`.

 If `.env` is unnecessary, DO NOT create it merely for appearance.

 `.env.example` should only contain variables that the application actually needs.

---

 # 10\. DO NOT INVENT DOCUMENTATION

 Every documentation file must describe the actual project.

 Do not fill files with generic placeholder text.

 If a file is not applicable, explain why in that file rather than inventing requirements.

 Example:

```
PostgreSQL is not used because the assignment can be satisfied
with local JSON persistence and PostgreSQL is not required.
```

---

 # 11\. REQUIREMENTS.MD

 Create a detailed requirements.md containing:

 ## Functional requirements

 Document every required feature.

 ## Non-functional requirements

 Include:

 - Reliability
- Usability
- Maintainability
- Error handling
- Performance appropriate for a local CLI
- Data persistence
- Security considerations where relevant

 ## Input requirements

 Document:

 - Valid inputs
- Invalid inputs
- Empty inputs
- Boundary values
- Unexpected input

 ## Output requirements

 Document expected CLI behavior.

 ## Assignment mapping

 Explicitly map each requirement to the assignment:

```
Requirement → Implementation → Test Case
```

---

 # 12\. DESIGN.MD

 Document:

 - Overall design
- CLI flow
- Modules
- Classes
- Functions
- Data flow
- Storage approach
- Error handling approach

 Keep the architecture appropriate for a mini-project.

 Do NOT over-engineer.

---

 # 13\. ARCHITECTURE.MD

 Document the actual project architecture.

 Example:

```
User
  ↓
CLI
  ↓
Application Logic
  ↓
Class / Functions
  ↓
JSON/CSV/Text Storage
```

 Only document components that actually exist.

---

 # 14\. DATA-MODEL.MD

 Document:

 - Data structures
- Fields
- Types
- Required fields
- Optional fields
- Validation rules
- Persistence format

 If JSON is used, provide example JSON structure.

 If CSV is used, document the CSV columns.

 If text is used, document the format.

---

 # 15\. PROJECT-SCOPE.MD

 Create explicit scope boundaries.

 ## In scope

 List exactly what will be implemented.

 ## Out of scope

 List functionality that will NOT be implemented.

 This file is extremely important.

 Do not implement anything from the "out of scope" section without my explicit permission.

---

 # 16\. TASKS.MD

 Create an implementation checklist.

 Example:

```
[ ] Project skeleton
[ ] Core class
[ ] Required functions
[ ] Input validation
[ ] File persistence
[ ] Error handling
[ ] CLI menu
[ ] Tests
[ ] Documentation
[ ] Final verification
```

 Tasks must correspond to actual requirements.

---

 # 17\. SKILLS.MD

 Create skills.md only for technologies/agent capabilities genuinely needed.

 For example:

```
Python
CLI development
JSON/CSV file handling
Unit testing
Git
```

 Do not invent agent skills.

 If Kiro supports a project-specific skills/agent mechanism, document only skills that are actually needed.

 Do not create unnecessary agents.

---

 # 18\. ERROR-LOGS.MD

 Create:

```
error-logs.md
```

 Record actual errors encountered during development.

 For every real error, record:

 - Date/time
- Command
- Error
- Cause
- Investigation
- Fix
- Verification

 Do NOT fabricate errors.

 If no errors occur:

```
No development errors encountered.
```

---

 # 19\. TESTING.MD

 Create a complete testing strategy.

 Include:

 - Unit testing
- Integration testing where applicable
- CLI testing
- Input validation
- Error handling
- Persistence testing
- Boundary testing
- Regression testing
- Final acceptance testing

---

 # 20\. TEST-CASES.MD

 Create between 100 and 500 test cases.

 IMPORTANT:

 Do not generate meaningless duplicate test cases just to reach a number.

 The test cases must be meaningful and relevant.

 Each test case should contain:

```
Test ID
Category
Purpose
Initial State
Input
Expected Output
Expected Data State
Pass/Fail
```

 Include:

 - Normal cases
- Invalid cases
- Empty values
- Boundary values
- Large values
- Duplicate inputs
- Missing data
- File errors
- Corrupt data where applicable
- Invalid commands
- Invalid menu selections
- Unexpected user input
- Persistence verification
- Restart/reload behavior
- Regression cases

 If the project cannot reasonably support 500 meaningful cases, create the maximum reasonable number within the 100–500 range and explain why.

---

 # 21\. SAMPLE-OUTPUT.MD

 Create sample-output.md containing realistic examples of the actual program.

 Include:

 ## Successful operations

 Show:

```
Input
↓
Actual expected CLI output
```

 ## Invalid operations

 Show:

```
Invalid input
↓
Expected error message
```

 ## Edge cases

 Show realistic expected behavior.

 Do not claim an output is real until the application has been tested.

---

 # 22\. SETUP-AND-RUN.MD

 Document exact setup instructions.

 Include:

 ## VS Code terminal

 Commands required to:

 1. Open the project
2. Create/activate virtual environment
3. Install dependencies
4. Run the project
5. Run tests
6. Run linting if used
7. Check the project

 ## Ubuntu terminal

 Provide equivalent commands.

 The commands must be tested.

---

 # 23\. SHELL SCRIPT

 Create:

```
run.sh
```

 The script must help the user:

 - Verify prerequisites
- Create/activate virtual environment if appropriate
- Install required dependencies
- Prepare required local files/directories
- Run the application
- Optionally run tests where appropriate

 Do not put destructive commands in the script.

 Do not delete user data.

 Do not overwrite important files without warning.

 Do not use paid services.

 The script must work on Ubuntu.

 If Windows support is required, document separate Windows commands rather than pretending `run.sh` is a Windows script.

---

 # 24\. REQUIREMENTS.TXT

 Create:

```
requirements.txt
```

 ONLY if third-party Python dependencies are actually required.

 Prefer Python's standard library.

 Do not install packages merely because they are popular.

 Every dependency must have a clear reason.

 Document every dependency in README.md.

---

 # 25\. ENVIRONMENT FILES

 Use environment variables only where genuinely necessary.

 If no environment variables are required:

 Do not create fake environment configuration.

 If required:

 Create:

```
.env.example
```

 and document every variable.

 Never commit:

```
.env
```

 if it contains secrets.

 Add appropriate `.gitignore` rules.

---

 # 26\. CLI REQUIREMENTS

 The CLI must be clear and usable.

 It should:

 - Show a clear menu or command structure
- Validate input
- Provide helpful errors
- Avoid crashing
- Allow the user to recover from mistakes
- Confirm important actions when appropriate
- Display useful output
- Return to the menu when appropriate
- Exit cleanly

 Avoid unnecessarily complicated terminal UI.

---

 # 27\. CLASS REQUIREMENT

 The project must contain at least one meaningful class.

 The class must represent a real concept in the project.

 Do NOT create a meaningless class just to satisfy the rubric.

 Document:

 - Why the class exists
- Its attributes
- Its methods
- Why those methods belong to the class

---

 # 28\. FUNCTION REQUIREMENT

 Implement at least 3 meaningful non-trivial functions.

 Do NOT create fake functions solely to satisfy the requirement.

 Every function must have a real purpose.

 The student must be able to explain:

 - What it does
- Inputs
- Outputs
- Why it exists
- How it interacts with the rest of the project

---

 # 29\. FILE I/O REQUIREMENT

 The assignment requires JSON/CSV/text file I/O OR an API.

 Prefer local file persistence because the project must be zero-cost.

 Handle:

 - File not found
- Empty file
- Invalid data
- Corrupted data
- Permission errors where practical
- Save failures

 The program must fail gracefully.

---

 # 30\. ERROR HANDLING

 The application must not crash on ordinary invalid user input.

 Handle cases such as:

```
Invalid menu selection
Empty input
Wrong data type
Invalid number
Negative value where prohibited
Missing record
Duplicate record
Invalid file contents
Missing data file
Unexpected input
```

 Use exceptions appropriately.

 Do not use broad exception handling unnecessarily.

 Avoid:

```
except Exception:
    pass
```

 unless there is a documented and justified reason.

---

 # 31\. TESTING IMPLEMENTATION

 Tests must actually execute against the application.

 Do not create tests that merely look correct.

 Use an appropriate testing method, preferably Python's built-in:

```
unittest
```

 unless another framework is genuinely necessary.

 Avoid introducing pytest or another dependency solely because it is popular.

 Run the tests.

 Record the results.

---

 # 32\. TEST RESULT REQUIREMENT

 At the end, provide:

```
Total tests
Passed
Failed
Skipped
Errors
```

 Do not claim 100% pass unless the tests actually passed.

 If tests fail:

 STOP finalization.

 Investigate and fix them where appropriate.

 Update error-logs.md.

 Re-run the relevant tests.

---

 # 33\. SECURITY

 This is not a banking application.

 Do NOT introduce unnecessary security infrastructure.

 However, follow basic software security practices:

 - Never hard-code passwords
- Never hard-code API keys
- Never expose secrets
- Validate input
- Avoid unsafe file operations
- Do not execute arbitrary user commands
- Do not use `eval()` for user input
- Do not store unnecessary personal data
- Do not commit secrets

 Create security.md explaining the actual security measures.

---

 # 34\. UI/UX

 Because this is a CLI application, UI/UX means terminal usability.

 The CLI should have:

 - Clear headings
- Clear menu choices
- Consistent formatting
- Helpful prompts
- Understandable errors
- Confirmation messages where useful
- Clear exit behavior

 Do not add graphical/web UI unless genuinely required.

---

 # 35\. GIT REQUIREMENT

 The assignment requires at least 5 meaningful commits.

 Do NOT create one giant commit.

 Use logical commits such as:

```
Initialize project structure
Implement core data model
Add persistence
Add CLI interface
Add validation and error handling
Add tests
Complete documentation
```

 Commit messages must accurately describe the changes.

 Do not create fake commits merely to reach five.

---

 # 36\. GITHUB REQUIREMENT

 The final project must be GitHub-ready.

 Do not create or modify a GitHub repository unless I explicitly authorize actions requiring my GitHub account.

 Prepare the repository locally.

 Verify:

```
git status
git log --oneline
```

 Confirm there are at least 5 meaningful commits before final delivery.

---

 # 37\. README.MD

 README.md must contain:

 # Project Name

 ## Problem It Solves

 ## Features

 ## Requirements

 ## Installation

 ## Setup

 ## Usage

 ## CLI Commands/Menu

 ## Examples

 ## Testing

 ## Project Structure

 ## Data Storage

 ## Error Handling

 ## Troubleshooting

 ## What I Learned

 ## Future Improvements

 ## Limitations

 ## Git Commit History

 ## License

 Do not claim features that do not exist.

---

 # 38\. ASSIGNMENT RUBRIC VERIFICATION

 Before finalizing, explicitly verify:

 ### Functionality

 - [ ] Works correctly
- [ ] Handles edge cases
- [ ] Does not crash on bad input

 ### Code Quality

 - [ ] PEP 8
- [ ] Good naming
- [ ] Understandable structure
- [ ] No unnecessary complexity

 ### Error Handling

 - [ ] Invalid input handled
- [ ] File errors handled
- [ ] Application exits cleanly

 ### Documentation

 - [ ] README complete
- [ ] Setup documented
- [ ] Usage documented
- [ ] Examples provided

 ### Git

 - [ ] At least 5 meaningful commits
- [ ] Commit history makes sense

 ### Presentation

 - [ ] Application can be demonstrated live
- [ ] Student can explain important code
- [ ] Student can explain design decisions

---

 # 39\. STUDENT UNDERSTANDING REQUIREMENT

 This project must remain understandable.

 For every major component, document:

```
What does it do?
Why does it exist?
How does it work?
What inputs does it accept?
What does it return?
What can go wrong?
```

 Do not produce unnecessarily complicated code that the student cannot explain.

 The student must be able to explain every important line during presentation.

---

 # 40. NO HIDDEN CHANGES

 Do not silently:

 - Add dependencies
- Change architecture
- Change storage technology
- Add cloud services
- Add APIs
- Add features
- Change requirements
- Remove required functionality

 If a change is necessary, ask first.

---

 # 41\. APPROVAL GATE — MANDATORY

 Before implementation, show me:

 1. Proposed project name
2. Problem being solved
3. User/persona
4. Exact feature list
5. Out-of-scope list
6. Technology stack
7. Dependencies
8. Storage approach
9. Project structure
10. Required documentation files
11. Testing strategy
12. Number/range of test cases
13. Whether AWS is required
14. Whether PostgreSQL is required
15. Whether any `.env` variables are required
16. Whether any external service is required
17. Estimated zero-cost approach
18. Risks or ambiguities

 Then STOP.

 Ask:

 > "Do you approve this scope and architecture? I will not implement anything until you explicitly approve it."

 Do not proceed until I explicitly approve.

---

 # 42\. AFTER APPROVAL

 After approval:

 1. Create documentation.
2. Create project structure.
3. Implement the minimum required functionality.
4. Test continuously.
5. Fix errors.
6. Add meaningful tests.
7. Complete documentation.
8. Verify PEP 8/readability.
9. Verify CLI usability.
10. Verify persistence.
11. Verify error handling.
12. Verify all assignment requirements.
13. Verify 100–500 meaningful test cases.
14. Run final test suite.
15. Run the shell script.
16. Verify Ubuntu commands.
17. Verify VS Code terminal commands.
18. Review Git history.
19. Perform final acceptance testing.

---

 # 43\. FINAL VALIDATION

 Before saying the project is complete, execute a final checklist.

 ## Application

```
[ ] Starts successfully
[ ] CLI works
[ ] All required features work
[ ] Invalid input does not crash application
[ ] Data persists correctly
[ ] Application exits cleanly
```

 ## Code

```
[ ] Python 3.13+
[ ] PEP 8/readable
[ ] 3+ meaningful functions
[ ] 1+ meaningful class
[ ] File I/O/API requirement satisfied
[ ] Error handling implemented
```

 ## Documentation

```
[ ] README.md
[ ] requirements.md
[ ] design.md
[ ] tasks.md
[ ] testing.md
[ ] test-cases.md
[ ] setup-and-run.md
[ ] skills.md
[ ] error-logs.md
[ ] sample-output.md
[ ] architecture.md
[ ] security.md
[ ] data-model.md
[ ] project-scope.md
[ ] change-log.md
[ ] known-issues.md
```

 ## Configuration

```
[ ] .gitignore
[ ] .env.example if required
[ ] No secrets committed
[ ] requirements.txt if required
[ ] run.sh
```

 ## Git

```
[ ] At least 5 meaningful commits
[ ] Clean/understood git status
[ ] Commit messages are meaningful
```

---

 # 44\. FINAL REPORT

 At completion, provide me with:

```
PROJECT STATUS
--------------

Project:
Status:

Features implemented:

Features intentionally not implemented:

Technology stack:

Dependencies:

Database:
N/A unless actually required.

AWS:
Used / Not Used

Total test cases:
Passed:
Failed:
Skipped:

Assignment requirements:
PASS / FAIL

Git commits:
Count:

Zero-cost status:

Known issues:

Files created:

How to run:

How to test:

Demo steps:

Potential future improvements:
```

---

 # 45\. FINAL ZERO-COST CHECK

 Before declaring completion, verify:

```
Does this project require payment to run?
Does this project require a credit card?
Does this project require AWS?
Does this project require a paid API?
Does this project require paid hosting?
Does this project require paid database hosting?
Does this project require paid storage?
Does this project require paid monitoring?
```

 If the answer to any is YES:

 STOP and inform me.

 Do not silently proceed.

---

 # 46\. MOST IMPORTANT RULE

 Follow this priority order:

```
1. User's explicit requirements
2. Assignment requirements
3. Approved architecture
4. Approved project scope
5. Zero-cost requirement
6. Simplicity and understandability
7. Testing
8. Documentation
9. Optional improvements
```

 Optional improvements are the lowest priority.

 If an optional improvement conflicts with simplicity, zero cost, assignment requirements, or approved scope:

 DO NOT IMPLEMENT IT.

---

 # 47\. ABSOLUTE FINAL INSTRUCTION

 DO NOT try to impress me by adding extra features.

 DO NOT make the project unnecessarily large.

 DO NOT use technology merely because it is available.

 DO NOT use AWS merely because AWS was mentioned.

 DO NOT use PostgreSQL merely because PostgreSQL was mentioned.

 DO NOT build a web application merely because a UI was mentioned.

 DO NOT add React, TypeScript, Node.js, Flask, FastAPI, PostgreSQL, AWS, Docker, Redis, Kubernetes, external APIs, authentication systems, payment systems, or other technologies unless they are actually required and approved.

 The goal is:

 > A simple, complete, reliable, zero-cost, documented, tested, GitHub-ready CLI application that satisfies the Day 6/Day 7 assignment and that the student genuinely understands.

 Before coding, present the scope and architecture and wait for my explicit approval.

 **DO NOT CODE BEFORE APPROVAL.**

 ### One thing I strongly recommend

 For this particular assignment, **don't force PostgreSQL 17, AWS, React, or a web UI into it**. Your supplied brief is explicitly a **6-hour CLI mini-project**. The strongest submission is probably something like an **Expense Tracker, Task Manager, Contact Book, Habit Tracker, or similar**, implemented cleanly in Python with local JSON/CSV persistence.

