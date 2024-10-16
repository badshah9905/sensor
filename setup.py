from setuptools import setup,find_packages


setup(
    name="project",
    version=0.0,
    author="hamid",
    author_email="mh9040206@gmail.com",
    url="https://github.com/badshah9905/sensor",
    projects_url={
        "bug_tracker":"https://github.com/badshah9905/sensor/issue"
    },
    package_dir={"":"src"},
    packages=find_packages(where="scr")
)
