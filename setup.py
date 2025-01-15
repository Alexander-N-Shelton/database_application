from setuptools import setup, find_packages

setup(
    name='database_application',
    version='0.1',
    py_modules=['presentation_layer', 'business_layer', 'styles', 'main'],
    install_requires=[
        'psycopg2',
    ],
    entry_points={
        'console_scripts': [
            'start_app = main:main'
        ]
    },
    package_data={
        '': ['sql/*.sql', 'data/*.csv'],
    },
    include_package_data=True,
)