#include <Python.h>
#include <stdio.h>

/**
* print_python_list_info - Funtion that prints the basic info on python list
* @p: the object to get the info from
*/
void print_puthon_list_infor(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize-t i;

	printf("[*] Size of the Python List = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf('Element %zd: '',i);
		PyObject_Print(PyList_GetItem(p, i), stdout, Py_PRINT_RAW);
		printf("\n");
	}
}
