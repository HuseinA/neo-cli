.. _installation-from-source:

Installation from Source
########################

Python Version
--------------

neo-cli only support Python 3 or newer.

Don't worry if you don't have Python3 installed. It's save to install
Python3 alongside Python2. Both have different installation location.

You can get python3 from your distro (GNU/Linux distribution) repository.


.. code-block:: bash

    $ sudo apt-get install python3

Use :code:`python3` instead of :code:`python` when you want to use python3.

:code:`which` help you tell you what program you are using (e.g :code:`which python3`)

pip
---

Get the pip for python3 with the following steps

.. code-block:: bash

    $ curl -O https://bootstrap.pypa.io/get-pip.py
    $ sudo python3 get-pip.py

Then use pip with :code:`pip3`.

Another way is to get it from your distro repository

.. code-block:: bash

    $ sudo apt-get install python3-pip

Virtual environments
--------------------

We strongly recommend using virtual environments to manage
dependencies of your project.


.. code-block:: bash

    $ sudo apt-get install python3-venv


Make new virtual environments with

.. code-block:: bash

    $ python3 -m venv yourvenvname

Active the venv (virtual environments) with

.. code-block:: bash

    $ source yourvenvname/bin/activate

Check if it's activated with


.. code-block:: bash

    $ which python3

If the output point to yourvenvname location. Then you are set.

Deactivate venv with

.. code-block:: bash

    $ deactivate

Dependencies
------------

Dependencies are located in requirements.txt

Grab those dependencies with

.. code-block:: bash

    $ pip3 install -r requirements.txt


Install neo-cli from Source
---------------------------

.. code-block:: bash

    $ pip3 install -e .

Test if :code:`neo-cli` installed correctly

.. code-block:: bash

    $ neo --help

If you get the help output from :code:`neo-cli`. Then you are ready to have fun.


