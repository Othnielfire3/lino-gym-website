import os

def check_paths():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(current_dir)
    
    print("Current directory (back-end):", current_dir)
    print("Root directory:", root_dir)
    print("HTML files in root:", [f for f in os.listdir(root_dir) if f.endswith('.html')])
    print("Static folders:", [f for f in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, f))])

if __name__ == '__main__':
    check_paths()