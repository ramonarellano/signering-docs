Admonitions
***********************
`See more about admonitions here <https://learning-readthedocs.readthedocs.io/en/latest/Options/admonition.html>`_

Example admonitions
#######################

.. code-block:: xml

    .. CAUTION::
       Caution message
    .. DANGER::
       Danger zone!
    .. NOTE::
       Important note!
    .. TIP::
       Just a tip!


.. CAUTION::
   Caution message
.. DANGER::
   Danger zone!
.. NOTE::
   Important note!
.. TIP::
   Just a tip!

Tabs
**********************

Tabs are used via an extension and how to use can be found `here <https://github.com/djungelorm/sphinx-tabs>`_.

The different tabs are `tab`, `group-tab` and `code-tab`.

.. code-block:: xml

   .. tabs::

      .. tab:: Apples

         Apples are green, or sometimes red.

      .. tab:: Pears

         Pears are green.

.. TIP::
   The different tabs are `tab`, `group-tab` and `code-tab`. With `group-tab`, all examples changes tab at the  same time. `code-tab` is self explanatory, but not that it behaves like `group-tab`.

Example tab
#############

.. tabs::

   .. tab:: Apples

      Apples are green, or sometimes red.

   .. tab:: Pears

      Pears are green.

   .. tab:: Oranges

      Oranges are orange.


Code snippets
*****************


.. code-block::

    .. code-block::language

       Some code here ...

