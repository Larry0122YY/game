import os
import sys
import subprocess
import TOOLS_COMMON as common

def main(arg):

    # This ALWAYS returns the fgo folder path, no matter where you run the script from
    script_folder = os.path.join(os.path.dirname(arg[0]), arg[1])
    script_name = arg[2]

    print('--------------------------------')
    print(f'current script folder: {script_folder}')
    print('--------------------------------')
    print()

    file_dict = get_file_list(script_folder)

    if script_name in file_dict.keys():
        script_path = os.path.join(script_folder, file_dict[script_name])
        # 获取项目根目录（run.py所在目录）
        project_root = os.path.dirname(os.path.abspath(__file__))
        
        # Use sys.executable to use the same Python interpreter
        exe_file_path = f'"{sys.executable}" "{script_path}"'
        print(f'Executing: {exe_file_path}')
        print()
        # 使用 subprocess 运行，传入环境变量
        subprocess.run(exe_file_path, shell=True, env=get_sub_process_env(project_root))     
    else:
        print(f'Error: Key "{script_name}" not found!')
        print()
        print('Available keys:')
        for key, filename in file_dict.items():
            print(f'  {key} -> {filename}')
        sys.exit(1)


def get_sub_process_env(project_root):

    # 设置 PYTHONPATH 环境变量，让 Python 能找到根目录的 TOOLS_COMMON
        env = os.environ.copy()
        if 'PYTHONPATH' in env:
            env['PYTHONPATH'] = project_root + os.pathsep + env['PYTHONPATH']
        else:
            env['PYTHONPATH'] = project_root
        
        return env

def get_file_list(script_folder):

    # Process all Python files in the folder
    result_dict = {}
    
    for filename in os.listdir(script_folder):
        filepath = os.path.join(script_folder, filename)
        
        # condition: only process Python files
        if os.path.isfile(filepath) and filename.endswith('.py'):
            # Remove .py extension and split by underscore
            name_without_ext = filename[:-3]  # Remove '.py'
            segments = name_without_ext.split('_')  # Split by underscore
            # Extract first letter of each word, convert to lowercase, and join (this is the key)
            key = ''.join([segment[0].lower() for segment in segments if segment])
            # The value is the complete filename
            result_dict[key] = filename
    
    return result_dict


if __name__ == '__main__':
    # Check if parameters are exactly three (excluding script name)
    if len(sys.argv) != 3:
        print('Error: please input the correct script name.')
        sys.exit(1)
    else:
        main(sys.argv)

