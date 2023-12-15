import os
with open('version', 'r') as f:
    version = f.read()
    print(f"Current version: {version}")
    segments = version.split('.')
    last_segment = int(segments[-1])
    last_segment = last_segment + 1
    segments[-1] = str(last_segment)
    new_version = '.'.join(segments)
    with open('version', 'w') as f:
        f.write(new_version)
        print(f"New version: {new_version}")
        # os.system(f"git commit -m 'Version {new_version}'")
        # os.system(f"git push")
        # os.system(f"git tag {new_version}")
        # os.system(f"git push --tags")