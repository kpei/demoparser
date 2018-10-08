``csgo-demoparser`` is a library for parsing CS:GO demo files.  This is a forked verison of Ryan Moe's original demoparser, it has a few additional events that the user can subscribe to as well as some additional player properties.  This is being maintained as a library for automated demo parsing and analysis.

Quick start
-----------

1. Install::

        git clone https://github.com/kpei/demoparser.git
        python setup.py install

2. Parse a demo::

   >>> from demoparser.demofile import DemoFile
   >>> data = open('/path/to/demofile', 'rb').read()
   >>> df = DemoFile(data)
   >>> df.parse()
