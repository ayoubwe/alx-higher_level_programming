#include "lists.h"

/**
 * check_cycle - chels ther's a cycle 
 *
 * @list: the linked list
 * Return:0
*/

int check_cycle(listint_t *list)
{
	listint_t *fixed = list;
	listint_t *temp = list;
	
	if (list == NULL || list->next == NULL)
		return (0);
	while (temp)
	{
		temp = temp->next;
		if (temp == fixed)
			return (1);
	}
	return (0);
}

