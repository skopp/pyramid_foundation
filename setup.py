from distutils import setup

setup(
    name='PyFo',
    version='0.0',
    author='Parker Pinette',
    author_email='parker@parkerpinette.com',
    packages=['towelstuff'],
    scripts=[''],
    url='',
    license='LICENSE.txt',
    description='A Pyramid scaffold including Zurb Foundation',
    long_description=open('README.txt').read(),
    entry_points="""\
        [pyramid.scaffold]
        pyfo=pyfo.scaffolds.PyramidFoundationTemplate
    """,
    install_requires=[
        'Pyramid',
    ],
)
