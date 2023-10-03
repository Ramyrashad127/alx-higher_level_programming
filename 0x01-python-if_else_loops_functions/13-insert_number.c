#include"lists.h"
/**
 * insert_node - insert
 * @head: head
 * @number: number
 * Return: ptr
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t)), *ptr;

	if (!new)
		return (NULL);
	new->n = number;
	if (!(*head))
	{
		*head = new;
		return (new);
	}
	ptr = *head;
	while ((ptr->next->n < number) && (ptr))
	{
		if (ptr->next == NULL && ptr->n < number)
		{
			add_nodeint_end(head, number);
			return (new);
		}
		ptr = ptr->next;
	}
	new->next = ptr->next;
	ptr->next = new;
	return (new);
}
