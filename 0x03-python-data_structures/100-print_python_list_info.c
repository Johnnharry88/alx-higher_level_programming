#include <Python.h>
/**
 * print_python_list_info - functions that prints information about
 * Python lists.
 * @p: A pyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int s;
	int a;
	int x;
	PyObject *v;

	s = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);

	for (x = 0; x < s; x++)
	{
		printf("Element %d:", x);
		v = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(v)->tp_name);
	}
}
