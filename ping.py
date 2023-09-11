import subprocess
import concurrent.futures

# Ping Function
def ping(ip):
    param = '-n'
    command = ['ping', param, '3', ip]
    try:
        result = subprocess.check_output(command, universal_newlines=True)
        if "Destination host unreachable" in result:
            return f"{ip} is down\n"
        else:
            return f"{ip} is up\n"
    except subprocess.CalledProcessError:
        return f"{ip} is down\n"

# Opening the file containing the list of IP Addresses
with open("IPs.txt") as f:
    ips = f.read().splitlines()

# Ping each IP using multiprocessing for faster execution
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(ping, ips))

# Write the results to the output file
with open("output.txt", "w") as output_file:
    output_file.writelines(results)

# Print the output to the screen
with open("output.txt") as f:
    output = f.read()
    print(output)