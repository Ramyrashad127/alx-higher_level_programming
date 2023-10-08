#include"lists.h"
#include<stdlib.h>
/**
 * is_palindrome - check
 * @head: head
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int i = 0, j = 0, k;
	int arr[50000];
	listint_t *ptr = *head;
	if(!head)
		return (1);
	if (!(*head))
		return (1);
	while (ptr)
	{
		arr[i] = ptr->n;
		i++;
		ptr = ptr->next;
	}
	for (j = 0, k = i - 1; j < i; j++, k--)
	{
		if(arr[j] != arr[k])
		{
			return (0);
		}
	}
	return (1);
}
