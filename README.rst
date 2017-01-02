|travis| |pypi|

sageone-api-client
==================

A simple Python client for interacting with the Sage One API.


Installation
------------

.. code-block:: bash

    $ pip install sageone-api-client


Usage
-----

1. Register for a Sage One account and request an API key by following the instructions at https://accounting.sageone.co.za/Marketing/DeveloperProgram.aspx
2. Review the supported Sage One API documentation at https://accounting.sageone.co.za/api/1.1.1/Help
3. Use the Python API client to interact with the API:

    .. code-block:: python

        >>> from sageone.client import APIClient
        >>> c = APIClient(
        ...     'https://accounting.sageone.co.za',
        ...     '{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}',
        ...     'your-sage-one-username',
        ...     'your-password')
        >>> r = c('get', 'Company', 'Get')
        >>> print(r)


Testing
-------

.. code-block:: bash

    $ python setup.py test


.. |travis| image:: https://travis-ci.org/maxnaude/sageone-api-client.svg?branch=master
    :target: https://travis-ci.org/maxnaude/sageone-api-client
.. |pypi| image:: https://badge.fury.io/py/sageone-api-client.svg
    :target: https://badge.fury.io/py/sageone-api-client
