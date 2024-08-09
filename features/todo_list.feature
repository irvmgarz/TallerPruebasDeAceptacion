Feature: To-Do List Management

Scenario: Add a new task to the to-do list
Given I have an empty to-do list
When I add a task with title "Buy groceries" and description "Milk, bread, and eggs"
Then the task list should contain 1 task
And the task should have title "Buy groceries" and description "Milk, bread, and eggs"

Scenario: List all tasks in the to-do list
Given I have a to-do list with tasks:
    | title          | description            |
    | Buy groceries  | Milk, bread, and eggs  |
    | Call the plumber| Fix the kitchen sink  |
When I list all tasks
Then the output should contain:
    | title          | description            |
    | Buy groceries  | Milk, bread, and eggs  |
    | Call the plumber| Fix the kitchen sink  |

Scenario: Mark a task as completed
Given I have a to-do list with tasks to mark:
    | title          | description            |
    | Buy groceries  | Milk, bread, and eggs  |
When I mark the task "Buy groceries" as completed
Then the task "Buy groceries" should be marked as completed

Scenario: Remove a specific task from the list by index
Given I have a to-do list with tasks to remove:
    | title          | description            |
    | Buy groceries  | Milk, bread, and eggs  |
    | Call the plumber| Fix the kitchen sink  |
When I remove the task at index 1
Then the task list should contain 1 task
And the remaining task should have title "Buy groceries"

Scenario: Clear the entire to-do list
Given I have a to-do list with tasks to clear:
    | title          | description            |
    | Buy groceries  | Milk, bread, and eggs  |
    | Call the plumber| Fix the kitchen sink  |
When I clear all tasks
Then the task list should be empty