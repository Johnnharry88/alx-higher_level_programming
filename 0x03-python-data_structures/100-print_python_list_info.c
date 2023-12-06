#include <Python.h>
/**
 * print_python_list_info - functions that prints information about
 * Python lists.
 * @p: A pyObject list.
 */
void print_python_list_info(PyObject *p)
{
	long int amt = PyList_Size(p);
	int x;
	PyListObject *obj = (PyLstObject *)p;

	printf("[*} Size of the Python List = %li\n", amt);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (x = 0; x < amt; x++)
		print("Element %i: %s\n", x, Py_TYPE(obj->ob_item[x])->tp_name);
}

