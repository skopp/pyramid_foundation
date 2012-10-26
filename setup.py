import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
]

setup(
    name='PyramidFoundation',
    version='0.1',
    author='Parker Pinette',
    author_email='parker@parkerpinette.com',
    packages=['pyramid_foundation'],
    scripts=[''],
    url='https://github.com/ppinette/pyramid_foundation',
    license='LICENSE.txt',
    description='A Pyramid scaffold including Zurb Foundation',
    long_description=open('README.txt').read(),
    install_requires=[
        'Pyramid',
    ],
    entry_points="""\
        [pyramid.scaffold]
        pyramid_foundation=pyramid_foundation.scaffolds:PyramidFoundationTemplate
    """,
)
