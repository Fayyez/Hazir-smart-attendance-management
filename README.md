# Hazir-IO: Smart AI Attendance Management System
## Introduction
**Hazir-IO** is a state-of-the-art AI attendance management which powered by computer vision and facial recogniton capabilities to faciliate seemless attendance management and classroom management for teachers and tutors.

They can create multiple classes, add students to those classes, student faces can be registered and then attendance sessions can be initiated which seemlessly detect and compare faces with registered faces and mark attendance, automating the trivial and difficult task of managing daily attendance. The project caters to the **HCI** and **Universal Design** principles by catering diverse audiences and socio-cultural or enviornmental constraints such as poor lighting or covered clothing such as hijab, the option of teacher-verified manual entry i provided, while to cater for different disabilities, text-to-speech functionality has also been provided.


## Set-up & Installation
[Python](python.org/downloads) is a pre-requisite for the project. Click on the hyper-link to install Python. Follow the steps listed below to setup our state-of-the-art AI attendance management system onto your local computer:

1. Clone the repository using:
```shell
git clone https://github.com/Fayyez/Hazir-smart-attendance-management/
```
> ***Note:** You need to have `git` installed for this command to run. You can either go install git first, or click on the download button in the top-left corner to install the project onto your local computer.*

2. Now either move to the project directory through the terminal using `cd` or just open the terminal in the root folder `.../Hazir-smart-attendance-management/` and create a virtual environment (venv):
```sh
py -m venv venv # this creates the venv
```
> ***Note:** This step is only for the first time setup.*
3. Activate the `venv` in the root directory (always activate the venv when you are working on the project, this is to ensure that the dependencies are propery packaged without any clash):
```sh
.\venv\Scripts\activate # this activates the venv
```

4. All the required project dependencies are listed in `requirements.txt` file. To download all the project dependencies, run the following command while having the venv activated and being in the root folder: 
```sh
pip install -r requirements.txt
```
> ***Note:** This step is only for the first time, do not repeat unless new dependencies are added to the ```requirements.txt``` file. **ALWAYS** remember to add any new dependency/library in the ```requirements.txt``` file.*

5. To run the application, move the the ```/src``` folder and run the ```app.py``` file using python

## Collaboration Guidelines

You must follow the following workflow guidelines to approve your changes to the final build aka stable production (aka the main branch) and hence collaborate.

1. **Review your assigned Issues** from the `Issues` tab on the top and check the checkboxes in the issue description to publicly track your progress on that task/issue, simultaneously as you work on its implementation. It is crucial for the progress to be transparent for efficient project progress tracking. 
2. Before starting working on an issue, **create a branch** and commit your changes to that branch. **Create one branch for one issue only**. Be sure to abide by branch naming convention. The branch name, although should be created with the name specified in your Issue, should be done in all lowercase, sould be short, meaningful and hyphen separated. E.g. "*add-login-screen*".
3. **Commit your changes to your branch** either in the case of showcasing your work for reference or updating your branch in consistency with the changes done at your local repository. **Adding a concise message to outline the commit theme is mandatory**. Sub-branches may be created in the case of a branch being dependant on the othr branch.
```sh
git commit -m "your message"
```
4. **Update your branch periodically** to stay in-sync with the main branch, especially whenever you observe a change done to the main repsitory to avoid future merge conflicts and to avoid using outdated code. If you are using Git, you may do this via:
```sh
git checkout your-branch # switching to your branch
git pull origin main # pull & merge remote main to local 
```
5. When your feature/task is completed and ready to be merged with the main branch, **submit a pull request (PR)**. Remember to include a meaningful title and description for your pull request. And **remember to include either *"fixes #n"* or *"resolves #n"* in your PR title**, where "*n*" is the Issue ID assigned to your Issue. For example: "*added login screen, resolves #3*" would automatically close Issue #3, submitting the associated pull request to be submitted for a **code review**.
6. The **code will then be reviewed** by the repository owner and feedback, if needed for the PR, would be given back for changes on the PR for code change & PR update, else it would be approved and **merged with the main**.

The process may then be iteratively used for every Issue resolved or feature added. 

## Coding Guidelines
Every collarborator is advised to write well indented and documented code. This includes writing explanatory code comments and docstrings for every function and class defined. Be sure to write efficient and concise code with meaningful names and type hints where possible. You can view the already submitted code for reference. A vscode extension was used to auto-generate docstrings in google formate, hence providing automation.

This would not only improve the code's readability and understandability but also improve the code's maintainibility and malleability.


## License
This project is licensed under the MIT License - see the LICENSE: ```LICENSE.txt``` file for details.
