#include "lists.h"

/**
 * check_cycle - find loop
 * @list: head
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (!list)
		return (0);
	second = list;
	first = list->next;
	while (first && second && first->next)
	{
		if (first == second)
			return (1);
		second = second->next;
		first = first->next->next;
	}
	return (0);
}
