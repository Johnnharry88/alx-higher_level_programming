#include "Python.h"
/**
 * print_python_list_info - functions that prints information about
 * Python lists.
 * @p: A pyObject list.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize a, a_size;
	PyObject *ptr;
	const char *ty_ptr;
	PyListObject *loc = (PyListObject *)p;
	
	a_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", (int) a_size);
	printf("[*] Allocated = %d\n", (int) loc->allocated);
	for (a = 0 , a < a_size; a++)
	{
		ptr = PyList_GetItem(p, a);
		ty_ptr = Py_TYPE(ptr)->tp_name;
		printf("Element %d: %s\n", (int) a, ty_ptr);
	}
}


