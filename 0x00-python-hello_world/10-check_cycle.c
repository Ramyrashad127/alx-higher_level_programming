#include"lists.h"
/**
 * check_cycle - check
 * @list: head
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *st = malloc(sizeof(listint_t));

	st = list->next;
	while(st->next != NULL && st != list)
	{
		st = st->next;
	}
	if (st == list)
	{
		free(st);
		return (1);
	}
	else
	{
		free(st);
		return(0);
	}
}
