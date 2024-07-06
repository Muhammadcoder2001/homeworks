def find_best_department_from_file(file_path):
    from collections import defaultdict

    department_counts = defaultdict(int)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Process each line of input
    for line in lines:
        parts = line.split(',')
        name = parts[0]
        position = parts[1]
        salary = int(parts[2])
        bonus = int(parts[3])
        department = parts[4]
        
        if bonus > 0:
            department_counts[department] += 1
            
    max_count = max(department_counts.values())
    
    best_departments = [dept for dept, count in department_counts.items() if count == max_count]
    
    return ', '.join(best_departments)

file_path = 'employees.txt' 
print(find_best_department_from_file(file_path))

            