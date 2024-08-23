import datetime

class MyGreeter:
    def greeting(self):
        current_time = datetime.datetime.now().time()
        hour = current_time.hour

        # 根据当前小时数判断时间段
        if 6 <= hour < 12:
            return "Good morning"
        elif 12 <= hour < 18:
            return "Good afternoon"
        else:
            return "Good evening"