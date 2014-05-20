#ditaa sphinx-doc extension

This adds a basic ditaa builder for sphinx.

Supports html and latex and latexpdf output.

##Usage:

    .. ditaa::
      +--------+   +-------+    +-------+
      |        | --+ ditaa +--> |       |
      |  Text  |   +-------+    |diagram|
      |Document|   |!magic!|    |       |
      |     {d}|   |       |    |       |
      +---+----+   +-------+    +-------+
          :                         ^
          |       Lots of work      |
          +-------------------------+

##Instalation

it has got a setup.py script so just usual 'python setup.py build' and
'install' will suffice.
