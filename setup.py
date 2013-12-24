from distutils.core import setup

def get_version(version, _):
    return version

setup(
    name = "TastyTopping",
    version = "1.0.5",
    description = "An ORM for tastypie's API on the client-side.",
    author = "Christian Boelsen",
    author_email="christian.boelsen@hds.com",
    url = 'https://github.com/cboelsen/tastytopping',
    packages = ['tastytopping'],
    license = "LICENSE",
    long_description = open('README.rst', 'r').read(),
    install_requires = [
        'requests >= 1.0.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
