import papermill as pm
pm.execute_notebook(
 'CuadernoParametros.ipynb',
 'CuadernoParametros_out.ipynb',
 parameters=dict(cantNumeros='2000'),
 kernel_name='python3'
)