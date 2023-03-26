import psutil

def get_cpu():
    return 100

def get_current_cpu_usage():
    return psutil.cpu_count()

def get_current_cpu_usage_percent():
    return psutil.cpu_percent()/100

def get_memory():
    return psutil.virtual_memory()[0]/2**30

def get_current_memory_usage_percent():
    return psutil.virtual_memory()[2]/100

def get_current_memory_usage():
    return psutil.virtual_memory()[3]/2**30

def get_disk():
    return psutil.disk_usage("/")[0]/2**30

def get_current_disk_usage():
    return psutil.disk_usage("/")[1]/2**30

def get_current_disk_usage_percent():
    return psutil.disk_usage("/")[3]/100


def get_type(type):
    if type == "memory":
        return get_memory(), get_current_memory_usage(), get_current_memory_usage_percent()
    if type == "disk":
        return get_disk(), get_current_disk_usage(), get_current_disk_usage_percent()
    if type == "cpu":
        return get_cpu(), get_current_cpu_usage(), get_current_cpu_usage_percent()