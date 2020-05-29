from setuptools import setup

setup(
    license="MIT",
    name="ProTJec_backend",
    version='0.1',
    description=("developed by skyleaworlder"),

    author="skyleaworlder 1852409 ljg",
    author_email="skyleaworlder@outlook.com",

    install_requires= [
        'flask',
        'flask_cors>=3.0',
        'pyjwt>=1.7',
        'python-dotenv>=0.13',
        'PyMySQL>=0.9',
        'gunicorn>=20.0'
    ],

    packages=[
        'ProTJec_backend',        # source
        'ProTJec_backend/db',     # database operations
        'ProTJec_backend/routes'  # blueprint
    ],
    zip_safe=False
)
