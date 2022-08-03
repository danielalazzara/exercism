def transpose(lines):
    if not lines:
        return ""
        
    lines = lines.split("\n")
    max_len = len(max(lines, key=len))
    result = ""

    for i in range(0, max_len):
        for j in range(0, len(lines)):
            result += (lines[j][i] if i < len(lines[j]) else "_")
        result = result.rstrip("_").replace("_", " ", -1) + "\n"

    return result[:-1]  
  
