from collections import Counter

def detect_anomalies(logs):
    counts = Counter(logs)
    return [log for log, freq in counts.items() if freq ==1 ]