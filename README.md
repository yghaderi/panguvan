# metafid
## panguvan
<div dir="rtl">
پنگوئن برای ایجادِ  پایگاه-داده و به-روز-رسانی داده‌ها مبتنی بر
<a href="https://pypi.org/project/oxtapus/">
اُختاپوس
</a>
توسعه داده ‌می‌شود.
</div>

<div dir="rtl">
مرحله‌یِ اول کانفیگ و ساحتِ جدول‌ها است. قبل از این کا باید بر روی سیستم خود پایگاه-داده‌ای نصب و ایجاد کنید- پیشنهاد میشه از postgresql استفاده کنید.
</div>

```python
from panguvan import config
from panguvan.models import ise
config(engin="postgresql", name="panguvan", user="postgres", password="postgres", host="localhost", port=5432)
ise.create_tables()
```

<div dir="rtl">
جدل‌هایِ مربوط به صنعت بر مبنایِ The Refinitiv Business Classification توسعه یافته و هنوز امکانِ شخصی-سازی وجود نداره. دلیل عدمِ-بهره-گیری از دسته-بندیِ tsetmc  دقتِ پایین و به تبع انحرافِ در تحلیل است. برای داده‌های مربوط به تابعِ write_trbc_tables به فایل TRBC.h5 نیاز خواهید داشت که می‌توانید
<a href="https://github.com/yghaderi/panguvan">
اینجا
</a>
دانلود کنید.  
</div>

```python
from panguvan.data import ISE
ise_data = ISE()
ise_data.write_date_table()
ise_data.write_market_table()
ise_data.write_trbc_tables("./TRBC.h5")
```

<div dir="rtl">
اکنون باید جدولِ ise_instrument داده-دهی شود. زحمت این بخش رو فعلن باید خودتون بکشید!
مراحلِ بعدی هم راحته(!) و تنها کافیه چند تابع ساده نوشته بشه. البته تا دو-سه هفته‌یِ دیگه این بخش‌ها هم توسعه داده می‌شوند.
</div>

