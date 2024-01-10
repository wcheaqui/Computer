
def start_project():
    # Importing the necessary libraries
    import os
    import sys
    import subprocess
    import venv

    from Comms import speak, listen
    from fileutils.CamelCase import camel_case

    # Creating a new directory with the given name
    speak("What would you like to call the project")
    project_name = camel_case(listen())
    os.mkdir(project_name)

    # Set the path to the directory where you want to create the virtual environment
    # os.chdir(project_name)
    venv_dir = os.path.join(os.getcwd(), project_name + '/venv')

    # Create the virtual environment
    venv.create(venv_dir, system_site_packages=False, clear=True)

    # Deactivate the current virtual environment
    deactivate_script = os.path.join('deactivate')
    subprocess.call('deactivate', shell=True)

    # Activate the virtual environment
    activate_script = os.path.join(venv_dir, 'bin', 'activate')
    subprocess.call(f'source {activate_script}', shell=True)

    # Installing the necessary packages for the project
    packages = ['pip', 'virtualenv', 'numpy', 'pandas']
    speak("is this for work?")
    if 'yes' in listen():
        packages.append('NikeCA')
    for package in packages:

        # Install required packages using pip
        subprocess.call([sys.executable, '-m', 'pip', 'install', package])

    print("Virtual environment created and packages installed successfully!")


