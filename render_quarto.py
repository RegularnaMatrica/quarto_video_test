import subprocess
import os
import shutil

def move_folder(src_folder, dst_folder):

    if os.path.isdir(src_folder):
        # Move the folder
        shutil.move(src_folder, dst_folder)
        # print message
        print(f"Folder moved from {src_folder} to {dst_folder}")
    else:
        raise ValueError(f"{src_folder} does not exist!")


def render_quarto(
    input_file, 
    output_dir = None, 
    **kwargs
):
    
    # base command
    command = ["quarto", "render", input_file]

    # add additional parameters
    for parameter, value in kwargs.items():
        command += ["-P", f"{parameter}:{value}"]

    # check if provided output file is html
    if output_dir:
        output_dir_basename = os.path.basename(output_dir)
        command += ["-P", f"output_dir:{output_dir_basename}"]
        command += ["--output-dir", output_dir_basename]
       
    # execute command
    result = subprocess.run(command)

    # check if command was executed successfully
    if result.returncode != 0:
        raise ValueError(f"Failed to render: {' '.join(command)} :(")
    else:
        print("successful rendering :)")
        # move folder if output folder is provided
        """ if output_dir:
            src_folder = os.path.join("quarto_reports", output_dir_basename)
            move_folder(src_folder, output_dir) """




