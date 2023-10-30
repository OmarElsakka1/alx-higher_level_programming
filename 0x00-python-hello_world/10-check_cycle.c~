#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if list has a cycle (Floyd's Cycle O(1))
 * @list: pointer to head of list
 * Return: 0 if no cycles, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		/* This will always be the case since if there was a
		cycle they will eventually meet*/
		if (slow == fast)
			return (1);
	}
	return (0);
}
