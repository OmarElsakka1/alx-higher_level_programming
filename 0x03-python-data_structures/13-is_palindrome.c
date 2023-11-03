#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks id a linked list is palindrome
 * @head: head ptr
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	if (!head)
		return (1);
	return (is_palindrome_helper(head, *head));
}
/**
 * is_palindrome_helper - recursive helper func
 * @head: head ptr
 * @end: end ptr
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome_helper(listint_t **head, listint_t *end)
{
	if (end == NULL) /* We've reached the end */
		return (1);

	if (is_palindrome_helper(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
