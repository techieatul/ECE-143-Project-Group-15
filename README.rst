.. -*- mode: rst -*-

.. |PythonVersion| image:: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue
.. _PythonVersion: https://img.shields.io/badge/python-3.8%20%7C%203.9-blue



.. |PythonMinVersion| replace:: 3.8.8
.. |NumPyMinVersion| replace:: 1.20.1
.. |PandasMinVersion| replace:: 1.2.4
.. |PlotlyMinVersion| replace:: 5.1.0



World Expenditure Analysis
===========

ECE-143-Project-Group-15

The project is aimed at analysing the government expenditure, studying the trends and relate it
to the various development indices. We aim to derive meaningful relations between expenditure and
growth of a country and use those relations to study if a given country is spending its GDP efficiently
to ensure growth.

Installation
--------------

Dependencies
~~~~~~~~~~~~

Main third-party modules:

- Python (>= |PythonMinVersion|)
- NumPy (>= |NumPyMinVersion|)
- Pandas (>= |PandasMinVersion|)
- Plotly (>= |PlotlyMinVersion|)

--------------

To reproduce the results of the repository, you can follow these steps:

1. Clone the repository using   ::

    git clone https://github.com/techieatul/ECE-143-Project-Group-15.git

2. Create a Python Virtual Environment using   ::

    python -m venv env

3. Activate the Environment using   ::

    source  env/bin/activate

4. Install all the dependencies using   ::

    pip install requirements.txt

5. Use the Jupyter Notebook to explore the repository. Deactivate, once done, using   ::

    deactivate

Contents
---------------
The collected raw data has been stored in the
`data <https://github.com/techieatul/ECE-143-Project-Group-15/tree/main/data>`_ folder.

Data Visualization
~~~~~~~~~~~~
All the visualizations have been shown in the `Data Visualization
<https://nbviewer.org/github/techieatul/ECE-143-Project-Group-15/blob/main/Data%20Visualization.ipynb>`_
jupyter notebook and is being rendered using `Nbviewer<https://nbviewer.org/>`_. You can further explore the data using the utility functions provided in
`util <https://github.com/techieatul/ECE-143-Project-Group-15/tree/main/utils>`_ folder.
