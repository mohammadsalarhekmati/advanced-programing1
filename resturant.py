from datetime import datetime

class Dish:
    #کلاس اغذا
      
    def __init__(self, title, group, cook_days):
        self.title = title           # نام غذا
        self.group = group           # ایرانی یا فرنگی
        self.cook_days = cook_days   # روز هایی که غذا موجود است
        self.quantity = 0            # مجودی غذا در رسنوران

    def set_quantity(self, count):
        
        self.quantity = count

    def is_available_today(self):
        
        day = datetime.now().strftime('%A')  # نام روز امروز به انگلیسی (مثل Saturday)
        return day in self.cook_days


class Worker:
    #کلاس کار کنان
    def __init__(self, full_name, section):
        self.full_name = full_name  # نام کامل کارمند
        self.section = section      # بخشی که کارمند در آن فعالیت می‌کند (مثلاً بسته‌بندی)
        self.leave = False          # وضعیت مرخصی (True = در مرخصی)

    def apply_leave(self):
        
        self.leave = True

    def leave_status(self):
        
        status = 'در مرخصی' if self.leave else 'مشغول'
        return f"{self.full_name} ({self.section}) - {status}"


class System:
    
    def __init__(self):
        self.dish_list = {}   # دیکشنری غذاها با کلید نام غذا
        self.worker_list = [] # لیست کارمندان

    def insert_dish(self, dish, stock):
        
        dish.set_quantity(stock)
        self.dish_list[dish.title] = dish

    def insert_worker(self, worker):
        """
        افزودن یک کارمند جدید به سیستم
        """
        self.worker_list.append(worker)

    def list_workers(self):
        """
        نمایش وضعیت تمام کارمندان
        """
        for w in self.worker_list:
            print(w.leave_status())

    def list_menu(self):
        """
        نمایش منوی کامل غذاها به همراه گروه و روزهای پخت هر غذا
        """
        for d in self.dish_list.values():
            days = ', '.join(d.cook_days)
            print(f"{d.title} ({d.group}) - پخت: {days}")

    def today_dishes(self):
        """
        نمایش غذاهایی که امروز قابل پخت هستند.
        """
        current = datetime.now().strftime('%A')
        available = [d.title for d in self.dish_list.values() if d.is_available_today()]
        if available:
            print(f"امروز ({current}) قابل تهیه: {', '.join(available)}")
        else:
            print(f"امروز ({current}) هیچ غذایی پخته نمی‌شود.")
        return available

    def make_order(self, dish_name, count):
        """
        انجام سفارش برای یک غذا با تعداد مشخص
        """
        dish = self.dish_list.get(dish_name)
        if not dish:
            print("چنین غذایی نداریم.")
            return
        if not dish.is_available_today():
            print(f"{dish.title} امروز پخته نمی‌شود. روزهای پخت: {', '.join(dish.cook_days)}")
            return
        if dish.quantity < count:
            print(f"موجودی کافی نیست. موجودی فعلی: {dish.quantity}")
            return
        dish.quantity -= count
        print(f"سفارش {dish.title} با تعداد {count} ثبت شد. باقی‌مانده: {dish.quantity}")


# --- اجرای تست نمونه ---

if __name__ == "__main__":
    # ساخت نمونه سیستم
    system = System()

    # تعریف لیست غذاهای ایرانی و جهانی به همراه روزهای هفته (به انگلیسی)
    iran = ['عدس‌پلو', 'باقالی‌پلو', 'مرغ', 'خوراک لوبیا', 'آبگوشت', 'کوفته', 'ته‌چین']
    world = ['چیزبرگر', 'راتاتویی', 'لازانیا', 'چیکن کاری', 'نودل', 'چوروس', 'سوشی']
    week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # افزودن غذاها به سیستم با موجودی 8 عدد برای هر غذا
    for i in range(7):
        system.insert_dish(Dish(iran[i], 'ملی', [week[i]]), 8)
        system.insert_dish(Dish(world[i], 'جهانی', [week[i]]), 8)

    # افزودن کارمندان
    system.insert_worker(Worker("احمدرضا", "بسته‌بندی"))
    system.insert_worker(Worker("نگار", "پخت"))
    system.insert_worker(Worker("یوسف", "تحویل"))

    # احمدرضا مرخصی می‌گیرد
    system.worker_list[0].apply_leave()

    print("کارمندان:")
    system.list_workers()

    print("\nمنو کامل:")
    system.list_menu()

    print("\nغذاهای امروز:")
    today = system.today_dishes()

    if today:
        # سفارش یک عدد از اولین غذای موجود امروز
        system.make_order(today[0], 1)

    # تلاش برای سفارش از غذایی که امروز پخته نمی‌شود (اولین غذا خارج از لیست امروز)
    for item in system.dish_list:
        if item not in today:
            system.make_order(item, 1)
            break