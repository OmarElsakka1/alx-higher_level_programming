#include "lists.h"
/**
 * insert_node - insert node in sorted linked list
 * @head: head
 * @number: new data
 * Return: pointer to the new node or NULL
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!curr || new->n < curr->n)
	{
		new->next = curr;
		return (*head = new);
	}
	while (curr)
	{
		if (!curr->next || new->n < curr->next->n)
		{
			new->next = curr->next;
			curr->next = new;
			return (curr);
		}
		curr = curr->next;
	}
	return (NULL);
}
