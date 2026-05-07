# pipeline.py
# Satge 3 - Count and summarize events by severity and source

filename = "data/sample.csv"

def check_severity(line):
    if "ERROR" in line:
        return "ERROR"
    elif "WARNING" in line:
        return "WARNING"
    else:
        return "INFO"
    
def parse_line(line):
    parts = line.strip().split(",")
    return {
        "timestamp": parts[0],
        "source": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

def summarize_data(filename):
    severity_counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    source_errors = {}
    
    with open(filename) as f:
        next(f)  # Skip header
        for line in f:
            row =parse_line(line)
            level = row["level"]
            
            # count by severity
            if level in severity_counts:
                severity_counts[level] += 1
                
            
            # count errors per source
            if level == "ERROR":
                source = row["source"]
                if source not in source_errors:
                    source_errors[source] = 0
                source_errors[source] += 1
                
    return severity_counts, source_errors
        
severity_counts, source_errors = summarize_data(filename)

print("=== Severity Counts ===")
for level, count in severity_counts.items():
    print(f"{level}: {count}")

print("\n=== Errors by Source ===")
for source, count in source_errors.items():
    print(f"{source}: {count}")