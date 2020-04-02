Contributing
############

We'd be happy for you to contribute to neo-cli.

To learn more about support questions, project organization, opening a new issue
and submitting a pull request, see `BiznetGio Project Contribution Guide <https://biznetgio.github.io/guide/contrib-guide/>`_.

First time setup
----------------

Please refer to installation from source :ref:`installation-from-source` guide.

Running the tests
-----------------

You can run the test with your own credentials

Run the basic test suite with:

.. code-block:: bash

    $ pytest

You can add more parameter to get more details.

.. code-block:: bash

    $ pytest --cov=neo -vv -s

If your test script get 'aborted' by the server. Try login manually
with :code:`neo login` before running test.

Running test coverage
---------------------

You can generate coverage report with:

.. code-block:: bash

    $ coverage report -m
    # or
    $ coverage html



