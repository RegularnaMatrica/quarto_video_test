import subprocess

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
        command += ["-P", f"output_dir:{output_dir}"]
        command += ["--output-dir", output_dir]
       
    # execute command
    result = subprocess.run(command)

    # check if command was executed successfully
    if result.returncode != 0:
        raise ValueError(f"Failed to render: {' '.join(command)} :(")
    else:
        print("successful rendering :)")