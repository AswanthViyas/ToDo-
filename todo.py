#!/usr/bin/env python3
from colorama import init, Fore, Style, Back

# Initialize colorama
init()

def show_menu():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}=== TO-DO LIST ==={Style.RESET_ALL}")
    print(f"{Fore.GREEN}1. Add task{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}2. View tasks{Style.RESET_ALL}")
    print(f"{Fore.RED}3. Mark task as done{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}4. Exit{Style.RESET_ALL}")
    return input(f"{Fore.BLUE}Choose an option (1-4): {Style.RESET_ALL}")

def add_task(todo_list):
    task = input(f"{Fore.GREEN}Enter task: {Style.RESET_ALL}")
    todo_list.append({"task": task, "done": False})
    print(f"{Fore.GREEN}{Style.BRIGHT}Task added successfully!{Style.RESET_ALL}")
    
def view_tasks(todo_list):
    if not todo_list:
        print(f"{Fore.YELLOW}No tasks in the list!{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}Your To-Do List:{Style.RESET_ALL}")
    for i, task in enumerate(todo_list, 1):
        status = "✓" if task["done"] else " "
        if task["done"]:
            print(f"{Fore.GREEN}{i}. [{status}] {task['task']}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}{i}. [{status}] {task['task']}{Style.RESET_ALL}")
        
def mark_done(todo_list):
    view_tasks(todo_list)
    if not todo_list:
        return
    
    try:
        task_num = int(input(f"\n{Fore.BLUE}Enter task number to mark as done: {Style.RESET_ALL}"))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num-1]["done"] = True
            print(f"{Fore.GREEN}{Style.BRIGHT}Task {task_num} marked as done!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Invalid task number!{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.RED}Please enter a valid number!{Style.RESET_ALL}")

def main():
    print(f"{Back.WHITE}{Fore.BLACK}{Style.BRIGHT} Welcome to Your Colorful To-Do List App! {Style.RESET_ALL}")
    todo_list = []
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            mark_done(todo_list)
        elif choice == "4":
            print(f"{Fore.MAGENTA}{Style.BRIGHT}Goodbye!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid option, please try again.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()