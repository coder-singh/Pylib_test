setuptools.setup(
    name="mylib",
    version="1.0",
    author="Thinklink",
    author_email="info@thinklink.io",
    description="This is a test package.",
    long_description="big description",
    long_description_content_type="text/markdown",
    url="package_bitbucket_page",
    packages=['mylib'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: ThinkLink",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)