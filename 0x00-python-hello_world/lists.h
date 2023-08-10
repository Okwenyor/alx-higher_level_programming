#ifndef LISTS_H
#define LISTS_H

/*
 * struct Node: structure to show the singly linked list node
 * @value: The value stored in the node
 * @next_node: pointer to next node
 */
typedef struct Node
{
	int value;
	struct Node *next_node;
}
listint_t;

/*
 * check_cysle - Function to check for the cycle in the linked list
 * @list: pointer to the head of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list);
#endif /*LISTS_H */
