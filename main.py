import os
import subprocess
import shutil

VENV_NAME = ".venv"
REQUIREMENTS_FILE = "requirements.txt"
OLD_REQUIREMENTS_FILE = ".requirements_old.txt"

def runCommand(command):
    try:
        res = subprocess.run(command,
                            check=True, 
                            shell=True, 
                            stdout=subprocess.PIPE, 
                            stderr=subprocess.PIPE)
        if res.stdout:
            print(res.stdout.decode())
        if res.stderr:
            print(res.stderr.decode())
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command failed with exit code {e.returncode}")
        if e.stderr:
            print(f"Error: {e.stderr.decode()}")
        return False

def installDependencies():
    if os.path.exists(REQUIREMENTS_FILE):
        print(f"Installing dependencies.")
        runCommand(f"{VENV_NAME}/bin/pip install -r {REQUIREMENTS_FILE}")
    else:
        print(f"No {REQUIREMENTS_FILE} file found. Skipping dependency installation.")

def createVenv():
    if os.path.exists(VENV_NAME):
        print(f"[Error] {VENV_NAME} already exists.")
        return
    print(f"Creating {VENV_NAME}.")
    runCommand(f"python3 -m venv {VENV_NAME}")
    
    installDependencies()

    if not os.path.exists(OLD_REQUIREMENTS_FILE):
        print(f"Creating {OLD_REQUIREMENTS_FILE}.")
        shutil.copy(REQUIREMENTS_FILE, OLD_REQUIREMENTS_FILE)

    print(f"Activate your venv by running")
    print(getActivateCommand())

def deleteVenv():
    if not os.path.exists(VENV_NAME):
        print(f"[Error] {VENV_NAME} does not exist.")
        return
    print(f"Deleting {VENV_NAME}.")
    shutil.rmtree(VENV_NAME)

    if os.path.exists(OLD_REQUIREMENTS_FILE):
        print(f"Deleting {OLD_REQUIREMENTS_FILE}.")
        os.remove(OLD_REQUIREMENTS_FILE)

def resetVenv():
    deleteVenv()
    createVenv()

def updateVenv():
    if not os.path.exists(VENV_NAME):
        print(f"[Error] {VENV_NAME} does not exist.")
        return
    
    if not os.path.exists(REQUIREMENTS_FILE):
        print(f"[Error] {REQUIREMENTS_FILE} does not exist.")
        return
    
    with open(REQUIREMENTS_FILE, "r") as new_file, open(OLD_REQUIREMENTS_FILE, "r") as old_file:
        new_packages = set([line.strip() for line in new_file.readlines()])
        old_packages = set([line.strip() for line in old_file.readlines()])

        added_packages = new_packages - old_packages
        removed_packages = old_packages - new_packages

        if added_packages:
            added_packages_str = ' '.join(added_packages)
            print(f"Installing added packages: {added_packages_str}")
            runCommand(f"{VENV_NAME}/bin/pip install {added_packages_str}")
        if removed_packages:
            removed_packages_str = ' '.join(removed_packages)
            print(f"Uninstalling removed packages: {removed_packages_str}")
            runCommand(f"{VENV_NAME}/bin/pip uninstall -y {removed_packages_str}")

        if not added_packages and not removed_packages:
            print("No changes to dependencies.")
        else:
            print(f"Updating {OLD_REQUIREMENTS_FILE}.")
            shutil.copy(REQUIREMENTS_FILE, OLD_REQUIREMENTS_FILE)

def getActivateCommand():
    return f". {VENV_NAME}/bin/activate"

def getDeactivateCommand():
    return f"deactivate"

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Manage your Python virtual environment.")
    parser.add_argument("--create", action="store_true", help="Create the virtual environment and install dependencies if requirements.txt exists.")
    parser.add_argument("--delete", action="store_true", help="Delete the virtual environment.")
    parser.add_argument("--reset", action="store_true", help="Reset the virtual environment by deleting and recreating it.")
    parser.add_argument("--update", action="store_true", help="Update the dependencies in the virtual environment.")
    parser.add_argument("--activate", action="store_true", help="Get command to activate the virtual environment.")
    parser.add_argument("--deactivate", action="store_true", help="Get command to deactivate the virtual environment.")
    args = parser.parse_args()

    if args.create:
        createVenv()
    elif args.delete:
        deleteVenv()
    elif args.reset:
        deleteVenv()
        createVenv()
    elif args.update:
        updateVenv()
    elif args.activate:
        print(getActivateCommand())
    elif args.deactivate:
        print(getDeactivateCommand())
    else:
        print("No action specified. Use --help for more information.")

if __name__ == "__main__":
    main()