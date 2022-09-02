from setuptools import setup

test_deps = [
    'pytest>=4',
    'pytest-cov>=2.6.0',
    'pytest-flake8',
]

setup(
    name='ICD',
    version='0.0.1',
    extras_require={
        'test': test_deps,
    },
    install_requires=[
        'EduCDM',
        'PyBaize>=0.0.7',
        'torch>=1.4.0',
        'fire'
    ],  # And any other dependencies foo needs
    entry_points={
    },
)
