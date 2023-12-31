#include"lists.h"
/**
 * insert_node - insert
 * @head: head
 * @number: number
 * Return: ptr
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *ptr, *pt;

	if (!new)
		return (NULL);
	new->n = number;
	if (!(*head))
	{
		*head = new;
		return (new);
	}
	if ((*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	ptr = (*head);
	pt = (*head)->next;
	while (pt)
	{
		if (pt->n > number)
			break;
		ptr = ptr->next;
		pt = pt->next;
	}
	new->next = pt;
	ptr->next = new;
	return (new);
}
