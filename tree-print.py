import os

EXCLUDED_DIRS = {'node_modules', 'build', '.git', '.cache', 'dist', '.next'}

def list_directories(path='.'):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and d not in EXCLUDED_DIRS and not d.startswith('.')]

def print_tree(root, prefix=''):
    if os.path.basename(root) in EXCLUDED_DIRS or os.path.basename(root).startswith('.'):
        return
    print(prefix + os.path.basename(root) + '/')
    prefix = prefix.replace('├── ', '│   ').replace('└── ', '    ')
    entries = sorted(os.listdir(root))
    for index, name in enumerate(entries):
        full_path = os.path.join(root, name)
        if os.path.isdir(full_path):
            if name not in EXCLUDED_DIRS and not name.startswith('.'):
                connector = '├── ' if index < len(entries) - 1 else '└── '
                print_tree(full_path, prefix + connector)
        else:
            connector = '├── ' if index < len(entries) - 1 else '└── '
            print(prefix + connector + name)

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    directories = list_directories(current_dir)
    if not directories:
        print("No hay directorios disponibles.")
        exit()
    
    print("Directorios disponibles:")
    for i, directory in enumerate(directories, 1):
        print(f"{i}. {directory}")
    
    choice = int(input("Selecciona el número del directorio del que deseas imprimir el árbol: "))
    if 1 <= choice <= len(directories):
        selected_directory = directories[choice - 1]
        print(f"\nÁrbol de directorios para '{selected_directory}':")
        print_tree(os.path.join(current_dir, selected_directory))
    else:
        print("Selección inválida.")
