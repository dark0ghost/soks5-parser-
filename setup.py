from setuptools import setup
requirements = [
"aiohttp",
"bs4"
]

setup(
    name='soks5-parser',
    version='2.0',
    description=" Python aioparser",
    author="dark0ghost",
    url='https://github.com/dark0ghost/soks5-parser/',
    packages=[
        'aiofaceapp',
    ],
    package_dir={'proxy2_0':
                     'proxy2_0'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT License",
    zip_safe=False,
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
