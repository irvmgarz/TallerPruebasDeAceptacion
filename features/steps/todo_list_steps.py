from behave import given, when, then
from todo_list import ToDoList  # Adjust the import to where your classes are defined

# Scenario: Add a new task to the to-do list
@given('I have an empty to-do list')
def step_given_empty_todo_list(context):
    context.todo_list = ToDoList()

@when('I add a task with title "{title}" and description "{description}"')
def step_when_add_task(context, title, description):
    context.todo_list.add_task(title, description)

@then('the task list should contain {count} task')
def step_then_task_list_contains_count(context, count):
    assert len(context.todo_list.tasks) == int(count), f"Expected {count} tasks but found {len(context.todo_list.tasks)}."

@then('the task should have title "{title}" and description "{description}"')
def step_then_task_should_have_details(context, title, description):
    task = context.todo_list.tasks[-1]  # Assuming last added task
    assert task.title == title, f"Expected title '{title}' but found '{task.title}'."
    assert task.description == description, f"Expected description '{description}' but found '{task.description}'."

# Scenario: List all tasks in the to-do list
@given('I have a to-do list with tasks')
def step_given_todo_list_with_tasks(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['title'], row['description'])

# Scenario: List all tasks in the to-do list
@when('I list all tasks')
def step_when_list_all_tasks(context):
    # Redirect print statements to a string (list) for checking the output
    import io
    import sys

    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    context.todo_list.list_tasks()

    sys.stdout = old_stdout
    context.list_output = new_stdout.getvalue().split('\n')

@then('the output should contain')
def step_then_output_contains(context):
    # Extract expected lines from context.table
    expected_lines = []
    for i, row in enumerate(context.table, start=1):
        # Format the row with task number, title, and description
        formatted_row = f"|Task {i}: {row['title']:<25} | {row['description']:<20} (Pending)|"
        expected_lines.append(formatted_row)

    # Check if each expected line is in the output list
    for expected_line in expected_lines:
        assert any(expected_line in output for output in context.list_output), f"Output does not contain '{expected_line}'."

# Scenario: Mark a task as completed
@given('I have a to-do list with tasks to mark')
def step_given_todo_list_with_tasks_to_mark(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['title'], row['description'])

@when('I mark the task "{title}" as completed')
def step_when_mark_task_completed(context, title):
    for i, task in enumerate(context.todo_list.tasks):
        if task.title == title:
            context.todo_list.mark_task_completed(i)
            break

@then('the task "{title}" should be marked as completed')
def step_then_task_marked_completed(context, title):
    for task in context.todo_list.tasks:
        if task.title == title:
            assert task.completed, f"Task '{title}' is not marked as completed."
            return
    assert False, f"Task '{title}' not found in the list."

# Scenario: Remove a specific task from the list by index
@given('I have a to-do list with tasks to remove')
def step_given_todo_list_with_tasks_for_removal(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['title'], row['description'])

@when('I remove the task at index {index}')
def step_when_remove_task(context, index):
    context.todo_list.remove_task(int(index))

@then('the task list should contain {count} task remove')
def step_then_task_list_contains_count_after_removal(context, count):
    assert len(context.todo_list.tasks) == int(count), f"Expected {count} tasks but found {len(context.todo_list.tasks)}."

@then('the remaining task should have title "{title}"')
def step_then_remaining_task_has_title(context, title):
    remaining_tasks = [task for task in context.todo_list.tasks]
    assert len(remaining_tasks) == 1, "Expected exactly 1 task in the list."
    assert remaining_tasks[0].title == title, f"Expected remaining task title '{title}' but found '{remaining_tasks[0].title}'."

# Scenario: Clear the entire to-do list
@given('I have a to-do list with tasks to clear')
def step_given_todo_list_with_tasks_to_clear(context):
    context.todo_list = ToDoList()
    for row in context.table:
        context.todo_list.add_task(row['title'], row['description'])

@when('I clear all tasks')
def step_when_clear_all_tasks(context):
    context.todo_list.clear_tasks()

@then('the task list should be empty')
def step_then_task_list_empty(context):
    assert len(context.todo_list.tasks) == 0, "The task list is not empty."