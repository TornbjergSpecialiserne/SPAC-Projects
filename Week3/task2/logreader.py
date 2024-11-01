if __name__ == "__main__":
    errors = []
    warnings = []
    info = []
    success = []
    misc = []
    with open('app_log.txt', encoding="utf-8") as f:
        read_data = f.read()
        lines = read_data.split("\n")
        for line in lines:
            if "error" in line.lower():
                errors.append(line)
            elif "warning" in line.lower():
                warnings.append(line)
            elif "info" in line.lower():
                info.append(line)
            elif "success" in line.lower():
                success.append(line)
            else:
                misc.append(line)
        f.close()
    with open("error_log.txt","w", encoding="utf-8") as f:
        for line in errors:
            f.write(line + "\n")
        f.close()
    with open("warning_log.txt","w", encoding="utf-8") as f:
        for line in warnings:
            f.write(line + "\n")
        f.close()
    with open("info_log.txt","w", encoding="utf-8") as f:
        for line in info:
            f.write(line + "\n")
        f.close()
    with open("success_log.txt","w", encoding="utf-8") as f:
        for line in success:
            f.write(line + "\n")
        f.close()
    with open("misc_log.txt","w", encoding="utf-8") as f:
        for line in misc:
            f.write(line + "\n")
        f.close()
