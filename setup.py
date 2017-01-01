from setuptools import setup, find_packages

setup(
    name='sageone-api-client',
    version='0.0.2',
    description='Sage One API Client',
    author='Max Naude',
    author_email='maxnaude@gmail.com',
    url='https://github.com/maxnaude/sageone-api-client',
    packages=find_packages(),
    dependency_links=[],
    install_requires=[
        'hammock==0.2.4'
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
    ],
)
