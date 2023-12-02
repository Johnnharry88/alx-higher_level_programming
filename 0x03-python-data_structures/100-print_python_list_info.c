#include <Python.h>
/**
 * print_python_list_info - functions that prints information about
 * Python lists.
 * @p: A pyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int x, y, z;
	PyObject *v;

	x = Py_SIZE(p);
	y = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = d\n", x);
	printf("[*] Allocated = %d\n", y);

	for (z = 0; z < x; z++)
	{
		printf("Element %d: ", z);
		v = PyList_GetItem(p, z);
		printf("%s\n", Py_TYPE(v)->typ_name);
	}
}
