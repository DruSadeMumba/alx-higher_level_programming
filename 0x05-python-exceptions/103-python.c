#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - print float
 * @p: object
 */
void print_python_float(PyObject *p)
{
	char *str = NULL;

	PyFloatObject *obj = (PyFloatObject *)p;
	fflush(stdout);
	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	str = PyOS_double_to_string(obj->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
	PyMem_Free(str);
}

/**
 * print_python_bytes - print python bytes
 * @p: object
 */
void print_python_bytes(PyObject *p)
{
	char *c;
	long int n, i, max;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	n = ((PyVarObject *)(p))->ob_size;
	c = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", n);
	printf("  trying string: %s\n", c);

	if (n >= 10)
		max = 10;
	else
		max = n + 1;
	printf("  first %ld bytes:", max);

	for (i = 0; i < max; i++)
	{
		if (c[i] >= 0)
			printf(" %02x", c[i]);
		else
			printf(" %02x", 256 + c[i]);
	}
	printf("\n");
}

/**
 * print_python_list - print list
 * @p: object
 */
void print_python_list(PyObject *p)
{
	long int n, i;
	PyListObject *list;
	PyObject *obj;

	n = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", n);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < n; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		else if (PyFloat_Check(obj))
			print_python_float(obj);
	}
}
