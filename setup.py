from setuptools import setup,find_packages

setup(
    name = "full_bhavcopy",
    version= '0.0.1',
    description="This is a full_bhavcopy package.",
    long_description_content_type="text/markdown",
    LONG_DESCRIPTION = '''
                        [github repo - ](https://github.com/ashishs1407/full_bhavcopy_pipeline)
                        ''',
    author="Ashish Shimpi",
    author_email="a.shimpi93@gmail.com",
    packages = find_packages(),
    py_modules=[],
    keywords=['python', 'tutorial','full_bhavcopy', 'ashish shimpi'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]

)