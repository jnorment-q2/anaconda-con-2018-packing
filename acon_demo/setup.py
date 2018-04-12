from setuptools import setup

requirements = [
    # package requirements go here
]

setup(
    name='acon_demo',
    version='0.1.0',
    description="acon demo",
    author="Mike Sarahan",
    author_email='msarahan@anaconda.com',
    url='https://github.com/msarahan/acon_demo',
    packages=['acon_demo'],
    entry_points={
        'console_scripts': [
            'acon_demo=acon_demo.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='acon_demo',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ]
)
