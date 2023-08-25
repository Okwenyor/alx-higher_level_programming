#include <Python.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)

{
	int size, alloc, i;
	const char *type;
	PyListObject *list = (PyListobject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;
	{

	type = list->ob_item[i]->ob_type->tp_name;
	printf("Elemenr %d: %s\n". i, type);
	if (strcmp(type, "bytes") == 0)

		printf("[*} Python list info\n);
		printf("[*] Allocated = %d\n", alloc);
		printf("[*] Size of the Python List = %d\n", size);

		for (i = 0; i < size; i++)

{
	print_python_bytes(list->ob_item[i]);
}
}
}
