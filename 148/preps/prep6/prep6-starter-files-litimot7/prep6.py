"""CSC148 Prep 6 Synthesize

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh,
Myriam Majedi, and Jaisie Sin.

=== Module Description ===
This module contains a __main__ block that defines some client code.
Define the three classes so that the example __main__ block will
run with all assertions passing and the output as described.

The provided self-test on MarkUs is the FULL test suite for this week!
This is a more robust set of tests, and there are no hidden test cases.

Your grade will correspond to the number of test cases passed. If you
pass all of them, then you will receive full marks for this prep.
As such, any unspecified behaviour that is not in the self-test is left
as a design decision for you.

Your task for this prep is to complete a program that allows a user to create
checklists with items to be done and record when items are completed:
- A checklist has a name (str) and a list of checklist items.
- A checklist item has a description (str), a deadline (date), and
  the name of the user who completed the item.
- A user has a name (str) and the total number items they have completed (int).

You will need to write one class for each of these entities.
See the __main__ block for an example of how we want to use these classes.

You may choose any reasonable way to store the necessary data. Attributes that
are of type int, str, or bool, and date may be public, but all other attributes
must be private. You may add imports from the typing module, but do NOT add any
other imports.

We will be checking for class docstrings that follow the Class Design Recipe.
You must include attribute type annotations and descriptions for all attributes.
Docstrings for your methods are NOT required.
"""
from __future__ import annotations
from datetime import date

# If you need any imports from the typing module, you may import them above.
# (e.g. from typing import Optional)


class User:
    """
    A user of a checklist system.

    === Public Attributes ===
    name: the name of the user.
    total_items_checked: number of items this user has completed.
    """
    name: str
    total_items_checked: int

    def __init__(self, name: str) -> None:
        """
        Initiate a new user with name <name> and 0 completed items,
        i.e. <completed_items_count> = 0.
        """

        self.name = name
        self.total_items_checked = 0


class Item:
    """
    An Item stored in a checklist.

    === Public Attributes ===
    description: a description of the Item.
    deadline: the deadline to complete this Item.
    completed_by: name of the person that completed the Item.
    """
    description: str
    deadline: date
    completed_by: str

    def __init__(self, description: str, deadline: date) -> None:
        """
        Initialize a new Item.
        """
        self.description = description
        self.deadline = deadline
        self.completed_by = None


class Checklist:
    """
    A checklist of Items

    === Public Attributes ===
    name: Name of the checklist.
    items_list: A list of Items in the checklist.
    """
    name: str
    items_list: list[Item]

    def __init__(self, name: str) -> None:
        """
        Initialize an empty Checklist.
        """
        self.name = name
        self.items_list = []

    def create_item(self, description: str, deadline: date) -> None:
        """
        Add an Item to this Checklist.
        """
        self.items_list.append(Item(description, deadline))

    def mark_item_complete(self, description: str, user: User) -> None:
        """
        Mark item with description <description> completed.
        """
        for item in self.items_list:
            if item.description == description:
                item.completed_by = user.name
                user.total_items_checked += 1
                return

    def has_item(self, description: str) -> bool:
        """
        Return true if this Checklist contains an Item
        with description <description>.
        """
        for item in self.items_list:
            if item.description == description:
                return True

        return False

    def __str__(self) -> str:
        """
        Return Checklist in a readable str format.
        """
        s = self.name
        for item in self.items_list:
            if item.completed_by is not None:
                s1 = "[x] " + item.description + " " + "(" \
                     + item.deadline.strftime("%Y-%m-%d") + ")" + \
                     ", completed by " \
                    + item.completed_by
                s = s + "\n" + s1
            else:
                s1 = "[-] " + item.description + " " + "(" \
                     + item.deadline.strftime("%Y-%m-%d") + ")"
                s = s + "\n" + s1

        return s.strip()


if __name__ == "__main__":
    # Instantiate three users
    manila = User('Manila')
    sofija = User('Sofija')
    felix = User('Felix')

    # Instantiate a checklist
    manilas_checklist = Checklist('Planner for M')

    # Manila adds some items to the checklist, the first one she adds is Math
    # Homework due on March 1st.
    manilas_checklist.create_item('Math Homework', date(2021, 3, 1))
    manilas_checklist.create_item('pick up milk', date(2021, 2, 25))
    manilas_checklist.create_item('CSC148 A1', date(2021, 3, 2))

    # Manila finishes her CSC148 assignment and marks it complete
    manilas_checklist.mark_item_complete('CSC148 A1', manila)

    # Sofija attempts to check off an item as complete that isn't in
    # manilas_checklist.  This does nothing.
    manilas_checklist.mark_item_complete('MAT157 Review', sofija)

    # Sofija picks up milk for Manila.
    manilas_checklist.mark_item_complete('pick up milk', sofija)

    print(manilas_checklist)
    # The output is below. Notice that the order is based on the order they
    # were added to manilas_checklist.  Output:
    # Planner for M
    # [-] Math Homework (2021-03-01)
    # [x] pick up milk (2021-02-25), completed by Sofija
    # [x] CSC148 A1 (2021-03-02), completed by Manila

    # confirm the check list items are all present in the checklist
    for item_description in ['Math Homework', 'pick up milk', 'CSC148 A1']:
        assert manilas_checklist.has_item(item_description)

    # Felix completed no checklist items
    assert felix.total_items_checked == 0

    # Manila and Sofija each completed one checklist item
    assert manila.total_items_checked == 1
    assert sofija.total_items_checked == 1

    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['datetime'],
        'disable': ['W0212', 'E1136']
    })
