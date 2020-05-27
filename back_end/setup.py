from setuptools import setup

setup(
    license="MIT",
    name="ProTJec-backend",
    version='0.1',
    description=("developed by skyleaworlder"),

    author="skyleaworlder 1852409 ljg",
    author_email="skyleaworlder@outlook.com",

    install_requires= [
        'flask',
        'flask_cors>=3.0',
        'pyjwt>=1.7',
        'python-dotenv>=0.13'
    ],

    packages=[
        'src',        # source
        'src/db',     # database operations
        'src/routes'  # blueprint
    ],
    zip_safe=False
)
