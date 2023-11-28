#include "lists.h"
/**
 * insert_node - function that inserts a number into a linked list
 * @head: pointer to the head of linked list
 * @number: Number to be inserted
 * Return: NULL if it fails otherwise pointer to a new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr_1, *ptr_2 = *head;

	ptr_1 = malloc(sizeof(listint_t));
	if(ptr_1 == NULL)
		return (NULL);
	ptr_1->n = number;
	if (ptr_2 == NULL || ptr_2->n >= number)
	{
		ptr_1->next = ptr_2;
		*head = ptr_1;
		return(ptr_1);
	}
	while (ptr_2 && ptr_2->next && ptr_2->next->n < number)
		ptr_2 = ptr_2->next;
	ptr_1->next = ptr_2->next;
	ptr_2->next = ptr_1;
	return (ptr_1);
}
