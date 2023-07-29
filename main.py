import concurrent.futures

def run_script(script):
    subprocess.run(['python', script])

# Replace 'script1.py' and 'script2.py' with the actual filenames of your scripts
scripts = ['getprocs', 'app.py']

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(run_script, script) for script in scripts]

# Wait for all the concurrent scripts to finish (optional)
for future in concurrent.futures.as_completed(futures):
    pass


