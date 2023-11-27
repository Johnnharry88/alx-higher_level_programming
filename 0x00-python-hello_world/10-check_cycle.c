#include "lists.h"
/**
 * check_cycle - function that checks for a reapetition or cycle
 * in a singly linked list
 * @lx: pointer to head of singly linked lists
 * Return: 0 if no cycle otherwise, 1.
 */
int check_cycle(listint_t *lx)
{
	listint_t *check_1 = NULL, *check_2 = NULL;

	if (lx == NULL)
		return (0);
	check_1 = lx;
	check_2 = lx->next;
	while (check_1 && check_2->next)
	{
		check_1 = check_1->next;
		check_2 = check_2->next->next;

		if (check_1 == check_2)
			return (1);
	}
	return (0);
}
