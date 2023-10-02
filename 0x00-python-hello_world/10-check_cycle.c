#include"lists.h"
/**
 * check_cycle - check
 * @list: head
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *st;

	if (!list)
		return (0);
	st = list->next;
	while ((st != NULL) && (st != list))
		st = st->next;
	if (st == list)
		return (1);
	return (0);
}
