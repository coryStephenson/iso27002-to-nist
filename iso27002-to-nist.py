import pandas as pd

data = {
    "ISO 27002": [
        "5.1.1",
        "15.1.1",
        "11.1.4",
        "12.6.1",
        "16.1.1",
        "N/A",
        "N/A",
        "12.1.1",
        "17.1.2",
        "14.1.1",
        "14.2.8",
        "N/A",
    ],
    "NIST 800-53 r4": [
        "PM-1",
        "PS-7\nSA-4",
        "PM-9\nRA-1\nRA-3",
        "SI-2\nSI-3(2)",
        "IR-1",
        "Privacy Section\nSA-3",
        "PL-2",
        "PL-7",
        "CP-1\nCP-2\nIR-4(3)\nPM-8",
        "CM-2\nCM-6\nSA-8",
        "CA-1\nPM-10",
        "N/A",
    ],
}

df = pd.DataFrame(data)

print(df)
