import os
import json
import datetime


def read_logs():


    # ----Config-------------------------------
    log_path = "/var/log/dpkg.log"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[INFO] Reading log file: {log_path}")
    print(f"[INFO] Started at: {now}")

    #-----Read the log file -------------------

    try:
        with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except PermissionError:
        print("[ERROR] Permission denied. Run with: sudo python3 log_intel.py")
        return
    except FileNotFoundError:
        print(f"[ERROR] Log file not found: {log_path}")
        return

    print(f"[INFO] Total Lines read: {len(lines)}")

    #----- Parse each line --------------------
    error_lines = []
    warning_lines = []
    total_errors = 0
    total_warnings = 0

    for line in lines:
        line_lower = line.lower()

        if "error" in line_lower:
            total_errors += 1
            error_lines.append(line.strip())

        elif "warning" in line_lower:
            total_warnings += 1
            warning_lines.append(line.strip())


    # ---- Build the report Dictionary ---------

    report = {
        "report_metadata": {
            "generated_At": now,
            "log_file_parsed": log_path,
            "total_lines_read": len(lines)
        },
        "summary": {
            "total_errors": total_errors,
            "total_warnings": total_warnings,
            "error_rate_percent": round((total_errors / len(lines)) * 100, 2)
        },
        "recent_errors": error_lines[-5:],
        "recent_warnings": warning_lines[-5:]
    }

    # ---- Print sumarry to terminal -----------
    print(f"\n{'=' * 40}")
    print(f"  LOG INTELLIGENCE REPORT")
    print(f"{'=' * 40}")
    print(f"  Total lines:    {len(lines)}")
    print(f"  Errors found:   {total_errors}")
    print(f"  Warnings found: {total_warnings}")
    print(f"  Error rate:     {report['summary']['error_rate_percent']}%")
    print(f"{'=' * 40}\n")


    # ----- Save to JSON file ------------------
    output_path = os.path.join(os.path.dirname(__file__), "log_report.json")

    with open(output_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"[SUCCESS] Report saved to: {output_path}")

if __name__ == "__main__":
    read_logs()



