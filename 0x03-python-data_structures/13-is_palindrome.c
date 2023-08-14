#include "lists.h"

/**
 * reverse - reverse list
 * @head: pointer
 */
void reverse(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * is_palindrome - is list palindrome?
 * @head: pointer
 * Return: 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *second = *head, *first = *head, *temp = *head, *dup = NULL;

	if (!*head || !(*head)->next)
		return (1);

	while (1)
	{
		first = first->next->next;
		if (!first)
		{
			dup = second->next;
			break;
		}
		if (!first->next)
		{
			dup = second->next->next;
			break;
		}
		second = second->next;
	}
	reverse(&dup);

	while (dup && temp)
	{
		if (temp->n == dup->n)
		{
			dup = dup->next;
			temp = temp->next;
		}
		return (0);
	}
	if (!dup)
		return (1);
	return (0);
}
