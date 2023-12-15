from honeydew import pypi

latest_honeydew_version = pypi.get_latest_pypi_version(package_name='honeydew')
print(f"Latest honeydew version: {latest_honeydew_version}")
