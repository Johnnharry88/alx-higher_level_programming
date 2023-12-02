#include "lists.h"
/**
 * reverse_listint - function that reverses a singly linked list
 * @head: A pointer to the first node of list
 * Return: Pointer to head of reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *ptr_1 = *head;
	listint_t *nxt;
	listint_t *foma;

	while(ptr_1)
	{
		nxt = ptr_1->next;
		ptr_1->next = foma;
		foma = ptr_1;
		ptr_1 = nxt;
	}
	*head = foma;
	return (*head);
}

/**
 * is_palindrome - function that checks if a singly linked has a palindome.
 * @head: A pointer to the first node of the linked list
 * Return: 1 if there is pallindrome otherwise, 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *ram, *inv;
	listint_t *centre;
	size_t x, y = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	ram = *head;
	while (ram)
	{
		y = y + 1;
		ram = ram->next;
	}
	ram = *head;
	for (x = 0; x < (y / 2) - 1; x++)
		ram = ram->next;
	if ((y % 2) == 0 && ram->n != ram->next->n)
		return (0);
	ram = ram->next->next;
	inv = reverse_listint(&ram);
	centre = inv;

	ram = *head;
	while (inv)
	{
		if (ram->n != inv->n)
			return (0);
		ram = ram->next;
		inv = inv->next;
	}
	reverse_listint(&centre);
	return (1);
}

