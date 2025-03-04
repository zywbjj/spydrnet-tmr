.. _contents:

.. figure:: figures/spydrnet_tmr_logo.*
    :align: center

.. only:: html

    :Release: |version|
    :Date: |today|    

Welcome to SpyDrNet TMR!
==========================

SpyDrNet TMR is a package of netlist analysis and transformation 
applications. Here are some of the capabilities of SpyDrNet TMR's current state:

 * Triple Modular Redundancy and Duplication With Compare for netlists across hierarchy

This Python package depends on `SpyDrNet <https://byuccl.github.io/spydrnet>`_. As new features are constantly being added to SpyDrNet, using the latest version is recommended.

History
-------
Previous tools could not handle doing TMR and DWC on netlists with hierarchy. They required the netlists to be flattened before triplicaiton. SpyDrNet TMR addresses this issue, and can perform TMR and DWC on netlists without flattening.

Due to findings in the paper by Jonathon Mark Johnson, [Johnson01]_, the SpyDrNet TMR tools uses algorithms that put voters on flip flops.

The application of DWC also follows the findings from a paper by Daniel McMurtrey, [McMurtrey01]_.

License
-------

Please see :ref:`LICENSE`

Bibliography
------------

.. [Johnson01] Johnson, Jonathan Mark, "Synchronization Voter Insertion 
   Algorithms for FPGA Designs Using Triple Modular Redundancy" (2010). Theses \
   and Dissertations. 2068. https://scholarsarchive.byu.edu/etd/2068

.. [McMurtrey01] McMurtrey, Daniel L., "Using Duplication with Compare for 
   On-line Error Detection in FPGA-based Designs" (2006). Theses and 
   Dissertations. 1094. https://scholarsarchive.byu.edu/etd/1094

.. toctree::
   :maxdepth: 2
   
   install
   tutorial
   reference/index.rst
   auto_examples/index
   simpleCounter/index.rst
   f4pga/index
   developer/index.rst
   license
