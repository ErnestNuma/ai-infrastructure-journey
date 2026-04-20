import subprocess	#Tool used for system commands
import os		#Tool used for operating system logic
import datetime		#Tool used to get timestamps
 
def generate_report():
	# Setup Data

	user = os.environ.get('USER' , 'unknown')
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	# Grab System Info

	ram = subprocess.check_output(['free' , '-m']).decode('utf-8')
	storage = subprocess.check_output(['df' , '-h']).decode('utf-8')
	cpu = subprocess.check_output(['uptime']).decode('utf-8')


	print(f"{'=' * 40}")
	print(f"--- SYSTEM REPORT FOR {user} ---")
	print(f" Generated at: {now}")
	print(f"{'=' * 40}")


	print(f"\nRAM INFO:\n{ram}")
	print(f"\nSTORAGE INFO:\n{storage}")
	print(f"\nCPU INFO:\n{cpu}")

	print(f"{'=' * 40}")
	print(f" Report complete.")
	print(f"{'=' * 40}")

	report_content = f"""

================================================

SYSTEM REPORT FOR: {user}
Generated at: {now}

================================================


RAM INFO:
{ram}

STORAGE INFO:
{storage}

CPU INFO:
{cpu}

================================================
Report Complete.
================================================

"""

# 2. Write it to the disk
# 'ww stands for 'write' (it creates the file or overwrites it)

	with open("report.txt" , "w") as f:
		f.write(report_content)

	print("\n[SUCESS] report.txt has been generated on your Desktop.")

# THis tells Phyton to run the function as soon as the script starts
if __name__ == "__main__":
	generate_report()
