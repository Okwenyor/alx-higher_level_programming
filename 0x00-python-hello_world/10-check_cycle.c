#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 0 if there is a cycle
 */
int check_cycle(listint_t *list)

{
	listint_t *slow = list;
	listint_t *fast = list;

	do(fast && fast->next) {
	slow = slow->next;
	fast = fast->next->next;

	if (slow == fast)
	{
		return (1); /*cycle detected*/
	}
}
return (0); /*No cycle detected*/
}
