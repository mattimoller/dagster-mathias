from setuptools import find_packages, setup

setup(
    name="dagster_mathias",
    packages=find_packages(exclude=["tests"]),
    install_requires=["dagster", "dagster-cloud"],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
