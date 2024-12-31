import os 
import subprocess


# result = os.system('ls -la')
# print(f'{type(result) =} {result = }')

# total 12
# drwxrwxrwx+  2 codespace codespace 4096 Dec 31 00:09 .
# drwxrwxrwx+ 10 codespace codespace 4096 Dec 31 00:09 ..
# -rw-rw-rw-   1 codespace codespace   99 Dec 31 00:09 a_subprocess_ex.py
# type(result) =<class 'int'> result = 0



def execute_command(cmd):
    result = os.system(cmd)  
    print(f"result:{result}")


# execute_command("ping google.com") 
# execute_command("ifconfig")  
# execute_command("ifconfigjhg")  



def get_execution_result(cmd):
    # cmd = "ifconfig"
    p = subprocess.Popen(
            cmd, 
            shell=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    output, err = p.communicate()

    output = output.decode("utf-8")
    err = err.decode("utf-8")

    print(f"\noutput:{output}")
    print(f"err   :{err}")


get_execution_result("ping google.com")
get_execution_result("ifconfig")
get_execution_result("ifconfigjhg")