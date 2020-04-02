Usage
=====

You can list all NEO command with ``help``

.. code:: bash

   $ neo --help

Authentication
--------------

Use ``neo login`` to log in. ``neo logout`` to do the opposite.

Creation
--------

.. code:: bash

   $ neo create

NEO creates ``neo.yml`` for you if it doesn’t find one. Then it will
guide you trough questions to do the right job for you.

It will ask you the ‘stack’ and ‘template’ you want to create. Then fill
‘key-pairs’ and ‘network’ configuration. The last step is to setup your
‘vm’ where you are asked to choose ‘image name’ and ‘flavor’.

When you sure with the configuration. Hit ‘y/yes’ to continue to deploy.

List your stuffs
----------------

To see all availiable commands to list your stuffs:

.. code:: bash

   $ neo ls --help

Some of them are ``stack``,  ``vm``, and   ``network``.

Remove your stuffs
------------------

.. code:: bash

   $ neo rm

It will delete your stack, network and machine

Update
~~~~~~

.. code:: bash

   $ neo update

Use ``update`` to see your changes.

Attach
------

Attach local standard input, output, and error streams to a running
stack or virtual machine

.. code:: bash

   $ neo attach vm

``neo attach`` will read neo.yml configuration automatically if you
didn’t pass the of your vm.

You can also specify your running vm id manually with

.. code:: bash

   $ neo attach vm <your-vm-id>


Troubleshooting
===============

Unable to locate package python3-venv
-------------------------------------

Try to check the python3 venv module name provided by your distro

.. code:: bash

   $ apt-cache search python3 | grep venv

The results

.. code:: bash

   python3-venv - pyvenv-3 binary for python3 (default python3 version)
   python3.5-venv - Interactive high-level object-oriented language (pyvenv binary, version 3.5)

It might be differ on your machine. So please make sure you get the
correct name.

No command ‘neo’ found
----------------------

Make sure you virtual environments is activated
