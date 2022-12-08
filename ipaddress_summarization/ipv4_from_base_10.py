import pandas as pd
from dataprep.clean import clean_ip

def ipv4_from_base_10(data:list):
    return clean_ip(pd.DataFrame({"ip": data}), "ip", output_format="binary", report=False)