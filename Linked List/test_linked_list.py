from linked_list import LinkedList, merge_two_lists
def main():
    llist1 = LinkedList(3)
    llist1.append(7)
    llist1.append(9)
    llist1.append(14)

    llist2 = LinkedList(1)
    llist2.append(9)
    llist2.append(10)
    llist2.append(12)

    llist1.print_list()
    llist2.print_list()

    merged = LinkedList(node = merge_two_lists(llist1, llist2))
    merged.print_list()
    merged.remove_duplicates()
    merged.print_list()
    merged.print_nth_from_last(3)


if __name__ == "__main__":
    main()