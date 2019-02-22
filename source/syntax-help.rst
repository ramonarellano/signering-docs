Links
******

.. code-block:: bash

   `link text <http://google.com>`_

Will generate the following url:

`link text <http://google.com>`_

Headers
*******

.. code-block:: xml

   Innhold restructured text 1
   *****************************

   Innhold restructured text 2
   =============================

   Innhold restructured text 3
   _____________________________

   Innhold restructured text 4
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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


.. code-block:: bash

    .. code-block:: language

       Some code here ...

Numbered lists
###############

.. code-block:: xml

    3. First numbered item starts with three.
    4. The next numbered item, four.
    #. Auto numbering. Will be 5.

Will generate the following list:

3. Double-click on the actual certificate file (CertificateName.p12)
4. Save the certificate in Current User or Local Machine and click Next
5. Use the suggested filename. Click Next.
