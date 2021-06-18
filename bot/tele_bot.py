import telebot
import time
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton,InlineQueryResultVideo,ReplyKeyboardMarkup,KeyboardButton
import json

# import logging
bale_token = "260752710:465bea46b20c3775bf21df37a983a2909f99f393"

telegram_token = "1766529248:AAFxVGIMyE30puIWTSrIHBZzD75PQwOczFw"
bot=telebot.TeleBot(token=telegram_token)
usernamearr={'safari78':'12345','manman':'4420886048'}
newwws=[
    {
        "title": "برنده نوبل: بیت کوین می‌تواند بارها و بارها از مرگ فرار کند!",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/340990_98fd.jpg",
        "body": "پاول کراگمن، برنده جایزه نوبل که پیش‌تر مرگ قریب‌الوقوع بیت کوین را پیش‌بینی کرده بود، ضمن کوتاه‌آمدن از این موضع خود، اعلام کرد که بیت کوین «آیینی» است که می‌تواند بارها و بارها از مشکلات مختلف جان سالم به در ببرد. او در توییت خود، بیت کوین را به آیینی تشبیه کرد که همواره پیروان جدیدی دارد و همین مسئله باعث می‌شود بارها و بارها از از زیر بار مشکلات فرار کند و به بقا ادامه دهد.",
        "src_name": "Bitcoin.com",
        "src_link": "https://news.bitcoin.com/nobel-laureate-paul-krugman-quits-predicting-bitcoins-demise-btc-survive-indefinitely/",
        "date": "2021-05-24"
    },
    {
        "title": "ماینرهای بیت کوین در بازار جهانی کمیاب شدند",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/Mining-978x675-1.jpg",
        "body": "در شرایطی که قیمت بیت کوین دچار افت شدید شده و سختی شبکه این ارز دیجیتال بیشتر شده است، به نظر می‌رسد ماینرها همچنان به دنبال خرید دستگاه‌های استخراج و کسب درآمد بیشتر هستند. داده‌های اخیر نشان می‌دهد که موجودی دستگاه‌های استخراج در بازار به اتمام رسیده و همه آنها به فروش رفته‌اند. به نظر می‌رسد عمده این دستگاه توسط نهادها خریداری شده باشند. گفتنی است ۶ سازنده برتر دستگاه‌های استخراج بیت کوین، در کشور چین فعال هستند.",
        "src_name": "Bitcoin.com",
        "src_link": "https://news.bitcoin.com/btc-mining-devices-out-of-stock-worldwide-6-chinese-mining-rig-makers-dominate-the-asic-industry-in-2021/",
        "date": "2021-05-24"
    },
    {
        "title": "آقای گل مسابقات جام ملت‌های اروپا NFT جایزه می‌گیرد",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/ruto-1024x574.jpg",
        "body": "شرکت گازپروم روسیه، حامی مالی مسابقات یورو ۲۰۲۰، می‌خواهد به برترین گلزن این دوره از بازی‌ها یک توکن غیر مثلی هدیه دهد. این جایزه منحصر بفرد بخشی از توافق اخیر میان این شرکت روسی و اتحادیه فوتبال اروپا (یوفا) است. برای این منظور اثر هنری یک هنرمند روس قرار است در قالب یک ویدئوی سه‌بعدی اسکن شود تا از آن برای ایجاد این توکن غیر مثلی استفاده شود. گفتنی است آقای گل این مسابقات هدیه خود را بعد از پایان این دوره از بازی‌ها و در مقر یوفا دریافت خواهد کرد.",
        "src_name": "Bitcoin.com",
        "src_link": "https://news.bitcoin.com/best-goal-scorer-at-euro-soccer-championship-to-get-nft-trophy-from-gazprom/",
        "date": "2021-05-24"
    },
    {
        "title": "کندل هفتگی بیت کوین و اتریوم باز هم به رنگ قرمز بسته شد",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/chart-9.jpg",
        "body": "روند ریزشی بازار برای دومین هفته متوالی ادامه پبدا کرد و کندل هفتگی بیت کوین و اتریوم در کنار سایر ارزهای دیجیتال باز هم رنگ قرمز به خود گرفت. بهای بیت کوین نسبت به هفته قبل ۲۹.۷ درصد کاهش یافت و به محدوده ۳۳,۳۲۰ دلار رسید. اتریوم هم در مقایسه با هفته گذشته ۴۴.۲ درصد افت کرد و تا قیمت ۱,۷۲۸ پایین رفت. تغییرات اخیر در احساسات بازار این گمانه‌زنی را به همراه داشته که روند صعودی بازار به اتمام رسیده و دوران نزولی آن شروع شده است. توییت‌های ضد بیت کوینی ایلان ماسک و اعمال محدودیت بر فعالیت‌های استخراج در چین را می‌توان از عوامل مهم روند اخیر بازار برشمرد.",
        "src_name": "CRYPTOBRIEFING",
        "src_link": "https://cryptobriefing.com/crypto-market-continues-slide-after-week-chaos/",
        "date": "2021-05-24"
    },
    {
        "title": "دولت مانع اراده سرمایه‌گذاران در مورد ارزهای دیجیتال نخواهد شد",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/340897_1c54.jpg",
        "body": "دیوید روبنشتاین، میلیاردر معروف و هم‌بنیانگذار کارلیل گروپ (Carlyle Group) می‌گوید این ایده که دولت مانع ارزهای دیجیتال خواهد شد و در برابر اراده سرمایه‌گذاران آن خواهد ایستاد، بسیار غیر واقع بینانه است. او معتقد است که ارزهای دیجیتال آمده‌اند تا بمانند. او می‌گوید ارزهای دیجیتال آمده‌اند تا جایگزین طلا باشند و درست همانند طلا، از بین نخواهند رفت. روبنشتاین همچنین می‌گوید که ارزهای دیجیتال مانند هر چیز جدیدی، فراز و نشیب‌هایی دارند و این بدان معنا نیست که قرار است محو شوند.",
        "src_name": "Bitcoin.com",
        "src_link": "https://news.bitcoin.com/billionaire-david-rubenstein-unrealistic-government-stop-cryptocurrency/",
        "date": "2021-05-23"
    },
    {
        "title": "کمک بایننس برای نجات جان ۱۲,۰۰۰ نفر در هند",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/Binance-2-1024x671.jpg",
        "body": "بخش خیریه صرافی بایننس در قالب پویش کریپتو علیه کووید، از ارسال محموله بزرگ اکسیژن به کشور هند برای مقابله با این همه‌گیری خبر داد. چانگ پنگ ژائو، مدیرعامل این صرافی، در توییتر نوشت: «دو مخزن فرستادیم تا در نجات جان ۱۲,۰۰۰ نفر کمک کرده باشیم.»",
        "src_name": "Ambcrypto",
        "src_link": "https://ambcrypto.com/binance-charity-funds-latest-efforts-should-help-save-about-12000-lives-in-india",
        "date": "2021-05-23"
    },
    {
        "title": "تیم فوتبال اوکراینی وارد عرصه NFT شد",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/kiv-1024x557.jpg",
        "body": "تیم فوتبال دینامو کی‌یف، قهرمان لیگ برتر اوکراین، می‌خواهد برای فصل ۲۰۲۱ بلیت‌های NFT صادر کند. این تیم بزرگ اوکراینی همچنین قصد دارد اقلام کلکسیونی منحصر بفردی را با همکاری شرکت بلاک چینی مون‌واک در اختیار طرفداران خود قرار دهد. بلیت‌های NFT دینامو کی‌یف در اواخر ژوئن در بازار توکن‌های غیر مثلی بایننس لیست خواهد شد.",
        "src_name": "Decrypt",
        "src_link": "https://decrypt.co/71751/dynamo-kiev-to-sell-nft-soccer-tickets-on-upcoming-binance-marketplace",
        "date": "2021-05-23"
    },
    {
        "title": "مدیر ارشد کوین شیرز: در پشت فاد مصرف انرژی بیت کوین، شرکت ریپل قرار دارد",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/Cryptocurrency-metal-coins-1.jpg",
        "body": "به‌عقیده ملتم دمیرورز، مدیر ارشد استراتژی شرکت کوین شیرز (Coinshares)، شرکت ریپل پشت روایت ضد بیت کوینی فراگیر شده اخیر، مبنی بر استفاده بیش از حد بیت کوین از برق قرار دارد. ملتم دمیرورز این ادعای خود را در پاسخ به توییت شبهه برانگیز بری سیلبرت، مدیرعامل شرکت دیجیتال کارنسی گروپ، مبنی بر اینکه شاید فاد (FUD) یا ترس مصرف انرژی بیت کوین توسط یک شرکت سازماندهی می‌شود، منتشر کرده است.",
        "src_name": "U.TODAY",
        "src_link": "https://u.today/ripple-is-behind-bitcoin-energy-usage-fud-says-coinshares-cso",
        "date": "2021-05-23"
    },
    {
        "title": "سقوط ارزش بازار کل ارزهای دیجیتال به زیر ۱.۵ تریلیون دلار",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/340717_cbcd.jpg",
        "body": "بر اساس داده‌های سایت Nomics، هم‌زمان با سقوط قیمت ارزهای دیجیتال، ارزش بازار کل ارزهای دیجیتال نیز به زیر ۱.۵ تریلیون دلار کشیده شده است. ارزش بازار کل ارزهای دیجیتال در ۲۴ ساعت اخیر، حدود ۹ درصد و در طول هفته اخیر، ۳۵ درصد کاهش یافته و نسبت به اوج تاریخی ۲.۵ تریلیون دلاری خود که در حوالی آغاز ماه می رخ داده بود، ریزش شدیدی را تجربه کرده است.",
        "src_name": "Decrypt",
        "src_link": "https://decrypt.co/71741/crypto-market-cap-sinks-below-1-5t-as-btc-and-eth-continue-to-crash",
        "date": "2021-05-23"
    },
    {
        "title": "لری سامرز: ارزهای دیجیتال آمده‌اند که بمانند",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/Larry-summers-Bitcoin-BTC-1024x680.jpg",
        "body": "لری سامرز، وزیر خزانه داری سابق ایالات متحده و اقتصاددان ارشد اسبق بانک جهانی در گفتگو با خبرگزاری بلومبرگ درباره ارزهای دیجیتال صحبت کرد. او که سابقه ریاست شورای ملی اقتصاد در دولت اوباما و ریاست دانشگاه هاروارد را نیز در کارنامه دارد، معتقد است که ارزهای دیجیتال آمده‌اند تا بمانند و نوعی طلای دیجیتال باشند.",
        "src_name": "Bitcoin.com",
        "src_link": "https://news.bitcoin.com/former-us-treasury-secretary-larry-summers-cryptocurrency-here-to-stay-digital-gold/",
        "date": "2021-05-23"
    },
    {
        "title": "نویسنده «پدر پولدار، پدر بی‌پول»: سقوط فعلی بیت کوین، یک فرصت خرید است",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/340789_f33f.jpg",
        "body": "رابرت کیوساکی، نویسنده کتاب مشهور «پدر پولدار، پدر بی‌پول» در توییتر خود گفت که سقوط کنونی بیت کوین، یک فرصت خرید است، مخصوصاً برای کسانی که قبلاً می‌گفتند توان خرید بیت کوین را ندارند.",
        "src_name": "Bitcoin.com",
        "src_link": "https://news.bitcoin.com/rich-dad-poor-dad-robert-kiyosaki-crypto-investors-buy-the-dip/",
        "date": "2021-05-23"
    },
    {
        "title": "تعداد کیف پول‌های کاردانو به بیش از ۱ میلیون رسید",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/340727_2c7a-1024x709.jpeg",
        "body": "بر اساس گزارش بنیاد کاردانو،  تعداد کیف پول‌های ADA بلاک چین اثبات سهم کاردانو، از مرز ۱ میلیون کیف پول عبور کرده است. جامعه و طرفداران ارز دیجیتال کاردانو در سال ۲۰۲۱ رشد قابل‌توجهی داشته است. در تاریخ ۱ ژانویه (۱۲ دی ۹۹) تعداد کیف پول‌های کاردانو تنها ۲۰۳,۵۱۹ عدد بود و این یعنی از ابتدای سال، تعداد کیف پول‌های این ارز دیجیتال تقریباً ۵ برابر شده است.",
        "src_name": "U.TODAY",
        "src_link": "https://u.today/cardano-achieves-major-milestone-with-1-million-ada-wallets",
        "date": "2021-05-23"
    },
    {
        "title": "محدودیت جدید استخراج بیت کوین در چین",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/340669_a635-1024x683.jpeg",
        "body": "طبق گزارش کالین وو، روزنامه‌نگار حوزه ارزهای دیجیتال استخر هوبئی که از زیرمجموعه‌های گروه هوبئی (Huobi Group) است، از این پس به ماینرهای بیت کوین در چین خدمات خود را ارائه نخواهد داد. طبق این گزارش، محدودیت ارائه خدمات شامل استخراج کنندگان فایل کوین نخواهد شد.",
        "src_name": "U.TODAY",
        "src_link": "https://u.today/huobi-pool-blocks-chinese-bitcoin-miners-amid-crackdown",
        "date": "2021-05-23"
    },
    {
        "title": "رشد چشمگیر جستجو عبارت «آیا باید ارز دیجیتال خود را بفروشم» در گوگل",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/google-now-lists-altcoin-prices-x486_1px.jpeg",
        "body": "داده‌های گوگل ترندز نشان می‌دهد که با عقب نشینی بازار ارزهای دیجیتال، یک عبارت جدید به جمع محبوب ترین موارد جستجو گوگل در رابطه با بازار کریپتو اضافه شده است. حساب گوگل ترندز در توییتر می‌گوید که میزان جستجوهای گوگل برای ارزهای دیجیتال به اوج تاریخی خود رسیده است.",
        "src_name": "CryptoSlate",
        "src_link": "https://cryptoslate.com/search-query-should-i-sell-my-bitcoin-skyrockets-on-google-trends/",
        "date": "2021-05-23"
    },
    {
        "title": "ایلان ماسک: پول فیات دشمن واقعی ماست",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/340734_6c7a-1024x640.jpg",
        "body": "همزمان با حملات بی شمار دوج کوینرها و بیت کوینرها به مدیرعامل تسلا در توییتر، ایلان ماسک از همه آن‌ها خواست تا بر روی پول فیات که به زعم وی دشمن اصلی همه آنهاست، تمرکز کنند. مدیرعامل تسلا پس از اینکه از وی پرسیده شد که نظرش درباره کسانی که از توییت‌هایش درباره ارزهای دیجیتال خشمگین هستند، چیست؛ پاسخ داد که نبرد واقعی بین کریپتو و پول فیات است. او می‌گوید خودش در این نبرد طرفدار کریپتو است.",
        "src_name": "U.TODAY",
        "src_link": "https://u.today/elon-musk-believes-fiat-is-your-real-enemy",
        "date": "2021-05-23"
    },
    {
        "title": "اتریوم به زیر ۲,۰۰۰ دلار کاهش یافت",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/340760_7105.jpg",
        "body": "بهای اتریوم برای نخستین بار از روز ۷ آوریل سال جاری تاکنون به زیر ۲,۰۰۰ دلار کاهش یافت. حالا ارزش هر اتریوم به کمتر از نصف ارزش آن در اوج قیمتی ۴,۱۶۵ دلاری روز ۱۲ ماه مه رسیده است.  ارزش بازار آن نیز اوج نیم تریلیون دلاری خود حالا به حدود ۲۳۰ میلیارد دلار سقوط کرده است. اتریوم در روز گذشته حدود ۱۸ درصد و در یک هفته اخیر ۴۵ درصد کاهش بها داشته است. هر اتریوم در ساعت ۱۸:۳۰ دقیقه به وقت تهران با حدود ۱۹ درصد کاهش به قیمت ۱,۹۶۵ دلار رسیده است.",
        "src_name": "Decrypt",
        "src_link": "https://decrypt.co/71744/ethereum-sinks-below-2000-amid-latest-crypto-crash",
        "date": "2021-05-23"
    },
    {
        "title": "تریدر برجسته: دوج کوین ارز مناسبی برای ورود مبتدیان به بازار است",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/3HOUWE7WFJK3NCF3R6HASOHHCY-1.jpg",
        "body": "اسکات ملکر، تریدر برجسته حوزه ارزهای دیجیتال، می‌گوید دوج کوین نقطه ورود مناسبی برای سرمایه‌گذاران مبتدی است. او دلیل خود را بهای زیر یک دلار دوج کوین و حمایت‌های مستمر افراد شناخته‌شده همچون ایلان ماسک عنوان کرده است. ملکر افزود دوج کوین ارزش بنیادی ندارد و سرمایه‌گذاران تازه‌کار خودشان باید درباره ارزهای دیجیتال تحقیق کنند و همواره از اشتباهات خود درس بگیرند. ملکر ۷۰ درصد از سبد سرمایه خود را به سرمایه‌گذاری بلند مدت اختصاص داده و استراتژی بلند مدت را بهترین روش برای کسب درآمد می‌داند.",
        "src_name": "Bitcoin.com",
        "src_link": "https://news.bitcoin.com/wolf-of-all-streets-trader-dogecoin-cryptocurrency-advice-doge-investors/",
        "date": "2021-05-23"
    },
    {
        "title": "آمریکا و اروپا به زودی در استخراج بیت کوین از چین سبقت می‌گیرند",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/medium_image_912727778-1.jpg",
        "body": "ژیانگ ژوئر، اپراتور استخر استخراج لبیت چین، می‌گوید سخت‌گیری‌های اخیر دولت این کشور در قبال استخراج ارزهای دیجیتال، احتمالاً باعث می‌شود ماینرها به آمریکا و اروپا نقل‌مکان کنند. ژیانگ گفت بسیاری از ماینرهای محلی بر این باور بودند که راه‌اندازی واحد استخراج در دیگر کشورها پرهزینه خواهد بود ولی اطلاعیه جدید دولت نظر بسیاری از آنها را تغییر داده است. چین در هفته گذشته چندین بیانیه درباره ارزهای دیجیتال منتشر کرد که آثاری منفی را برای بازار به همراه داشت. ممنوعیت انجام معامله در بازار مشتقات و اعمال محدودیت بر فعالیت‌های استخراج دو مورد مهم آن است.",
        "src_name": "CryptoSlate",
        "src_link": "https://cryptoslate.com/europe-and-u-s-may-soon-take-the-lead-in-bitcoin-mining-says-major-chinese-pool/",
        "date": "2021-05-23"
    },
    {
        "title": "جی‌پی مورگان: ارزش واقعی بیت کوین ۳۵,۰۰۰ دلار است",
        "image": "https://cdn.arzdigital.com/uploads/2021/05/bit-18-2.jpg",
        "body": "در شرایطی که سقوط سنگین بیت کوین، قیمت این ارز دیجیتال را تا محدوده ۳۰,۰۰۰ دلار هم به پایین کشید، تحلیل‌گران بانک جی‌پی مورگان می‌گویند سرمایه‌گذاران نهادی برای نخستین بار در ۶ ماه گذشته مشغول تبدیل بیت کوین‌های خود به طلا هستند. این در حالی است که در بازارهای آتی بیت کوین قراردادهای بسیاری لیکویید شده‌اند ولی صندوق‌های قابل معامله طلا در حال جذب سرمایه بوده‌اند. در نتیجه این رویدادها، جی‌پی مورگان اعلام کرد ارزش واقعی بیت کوین بر اساس نسبت نوسان بین بیت کوین و طلا ۳۵,۰۰۰ دلار است.",
        "src_name": "CryptoSlate",
        "src_link": "https://cryptoslate.com/jpmorgan-says-bitcoins-true-value-is-35000-amid-price-crash/",
        "date": "2021-05-23"
    },
    {
        "title": "مخالفت کارآفرینان در السالوادور با پذیرش اجباری بیت کوین",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/354422_b113-1024x670.jpeg",
        "body": "نتایج نظرسنجی اتاق بازرگانی السالوادور نشان می‌دهد فقط ۴ درصد از کارآفرینان در این کشور حامی پذیرش اجباری بیت کوین هستند. این در حالی است که ۳۹ درصد کارآفرینان معتقدند پذیرش اجباری این ارز دیجیتال به بی‌اعتمادی منجر می‌شود و نیمی از آنان بر این باورند که بیت کوین تأثیری بر اقتصاد کشورشان ندارد. به موجب ماده ۷ قانون بیت کوین در السالوادور، بنگاه‌های اقتصادی باید پذیرش بیت کوین را در دستور کار خود قرار دهند.",
        "src_name": "U.TODAY",
        "src_link": "https://u.today/overwhelming-majority-of-salvadoran-entrepreneurs-oppose-mandatory-bitcoin-acceptance",
        "date": "2021-06-18"
    },
    {
        "title": "رشد ۳۰ درصدی توکن پروتکل میرور به‌رغم روند ریزشی بازار",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/mirror.png",
        "body": "توکن پروتکل دیفای میرور (MIR) عملکرد قابل‌توجهی را از خود در روز پنج‌شنبه ثبت کرد. بهای میرور با ۳۰ درصد افزایش نسبت به روز گذشته از ۳.۹۷ دلار به حدود ۵ دلار رسید. راه‌اندازی شبکه آزمایشی این پروتکل با هدف ارتقا دادن این پروژه و لیست شدن این توکن در صرافی جمینای را می‌توان با این رشد قیمت مرتبط دانست.",
        "src_name": "CoinTelegraph",
        "src_link": "https://cointelegraph.com/news/mirror-protocol-silently-rallies-30-overnight-despite-crypto-market-slump",
        "date": "2021-06-17"
    },
    {
        "title": "همکاری تیم بسکتبال فیلادلفیا سونتی‌سیکسرز با پلتفرم توکن‌های هواداری",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/EFuVSNdWkAY7Yfp-1024x576.jpg",
        "body": "پلتفرم توکن‌های هواداری Socios که پیش‌تر با یک تیم لیگ ملی فوتبال آمریکا و یو اف سی قراردادهای شراکت تجاری امضا کرده بود، حالا سراف یکی از تیم‌های اتحادیه ملی بستکبال آمریکا (NBA) آمده است. تیم فیلادلفیا سونتی‌سیکسرز از اعضای لیگ ان‌بی‌ای برای نخستین بار در تاریخ این رقابت‌ها حاضر شده است تا شریکی برای برند تجاری خود بپذیرد. مدیرعامل Socios گفته است که این قرارداد و عرضه توکن‌های هوادارای برای فیلادلفیا می‌تواند بخشی از هدف این پلتفرم، یعنی تبدیل طرفداران منفعل به طرفداران فعال باشد.",
        "src_name": "CoinTelegraph",
        "src_link": "https://cointelegraph.com/news/nba-76ers-joins-fan-token-platform-socios",
        "date": "2021-06-17"
    },
    {
        "title": "بیت‌دائو در دور جدید تامین سرمایه خود ۲۳۰ میلیون دلار جمع آوری کرد",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/notes-and-coins-1000x628-1.jpg",
        "body": "بیت‌دائو (BitDAO)، یکی از بزرگترین سازمان‌های غیرمتمرکز و خودمختار جهان که در حوزه دیفای فعال است، توانست در دور جدید تامین سرمایه خود ۲۳۰ میلیون دلار جمع آوری کند. این سازمان که یکی از بزرگترین سازمان‌های غیرمتمرکز جهان محسوب می‌شود، در این دور از تامین سرمایه خود مشارکت بیش از ۲۰ نهاد را جلب کرد. از معروف ترین سرمایه‌گذاران در این رویداد می‌توان به آلن هاوارد، (مدیر معروف صندوق پوشش ریسک)، پیتر تیل (کارآفرین مشهور)، شرکت دراگون‌فلای کپیتال، پنترا کپیتال، فنبوشی، فاوندرز فاند، جامپ کپیتال و اسپارتان گروپ اشاره کرد.",
        "src_name": "Bitcoin.com",
        "src_link": "https://news.bitcoin.com/bitdao-collects-230-million-in-private-capital-from-investors/",
        "date": "2021-06-17"
    },
    {
        "title": "تعویق مجدد اعلام نظر SEC درباره ETF بیت کوین ون‌اک",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/354159_6ce2.png",
        "body": "کمیسیون بورس و اوراق بهادار آمریکا یک بار دیگر تصمیم گیری درباره صندوق قابل معامله بورسی ون‌اک بیت کوین تراست (VanEck Bitcoin Trust) را به تعویق انداخت. این نهاد در هفته اخیر تصمیم گیری درباره ETF بیت کوین کریپتوین را به آینده موکول کرده بود. حالا SEC از مردم خواسته است تا به چند سوال درباره این ETFها پاسخ دهند که شامل بحث آسیب پذیری آن‌ها در برابر دستکاری و عدم شفافیت بیت کوین است. عموم مردم فرصت دارند تا در ۲۰ روز آینده به این سوالات پاسخ دهند.",
        "src_name": "Decrypt",
        "src_link": "https://decrypt.co/73817/sec-delays-vaneck-bitcoin-etf-application-again",
        "date": "2021-06-17"
    },
    {
        "title": "مارک کوبان به دنبال سقوط توکن تیتان خواهان نظارت بیشتر بر استیبل کوین‌ها شد",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/354382_a860-1024x683.jpg",
        "body": "مارک کوبان، مالک تیم بسکتبال دالاس ماوریکس و میلیاردر ارزهای دیجیتال که زمانی از توکن تیتان (TTN) حمایت می‌کرد؛ حالا می‌گوید درسی که می‌توان از نابودی این استیبل کوین گرفت، این است که نظارت بیشتری در این بخش مورد نیاز است.",
        "src_name": "U.TODAY",
        "src_link": "https://u.today/billionaire-mark-cuban-wants-to-regulate-stablecoins-after-collapse-of-titanium-token",
        "date": "2021-06-17"
    },
    {
        "title": "بیش از یک سوم دارندگان ارز دیجیتال در بریتانیا آن را نوعی قمار می‌دانند",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/354317_8ed7.png",
        "body": "جدیدترین نظرسنجی اداره رفتار مالی بریتانیا (FCA) نشان می‌دهد که تعداد کاربران ارزهای دیجیتال در بریتانیا در حال افزایش است. این نظرسنجی که در ژانویه ۲۰۲۱ انجام شده می‌گوید که ۷۸ درصد از بزرگسالان در بریتانیا درباره ارزهای دیجیتال شنیده‌اند که ۵ درصد رشد نسبت به سال گذشته و ۴۳ درصد رشد نسبت به سال ۲۰۱۹ را نشان می‌دهد. همچنین تعداد کاربران ارزهای دیجیتال نیز با ۰.۳ درصد افزایش به ۵.۷ درصد رسیده است. محققان بر اساس این داده‌ها تخمین می‌زنند اکنون در بریتانیا ۲.۳ میلیون نفر ارز دیجیتال داشته باشند.",
        "src_name": "Decrypt",
        "src_link": "https://decrypt.co/73840/more-uk-citizens-confident-investing-crypto-fca-survey",
        "date": "2021-06-17"
    },
    {
        "title": "سفارش بزرگ شرکت جنسیس برای خرید ماینر بیت کوین",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/miner-4.jpg",
        "body": "شرکت جنسیس دیجیتال برای افزایش توان استخراجی خود ۱۰ هزار دستگاه ماینر بیت کوین را خریداری کرده است. ماینرهای خریداری‌شده جدیدترین محصول شرکت کانان است که قیمت هر دستگاه حدوداً پنج هزار دلار است. جنسیس که حدود دو ماه پیش هم از کانان ماینر خریده بود، ۱.۲ درصد از کل توان پردازش شبکه بیت کوین را در اختیار دارد.",
        "src_name": "CRYPTOBRIEFING",
        "src_link": "https://cryptobriefing.com/genesis-orders-more-bitcoin-mining-rigs-canaan/",
        "date": "2021-06-17"
    },
    {
        "title": "شکار ۹۰ هزار بیت کوینی نهنگ‌های میلیونر در ۲۵ روز اخیر",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/bit-5-1024x640.jpg",
        "body": "به گزارش وب‌سایت تحلیلی سنتیمنت، نهنگ‌های میلیونر طی ۲۵ روز گذشته مشغول خرید بیت کوین بوده‌اند و حدود ۹۰,۰۰۰ واحد از این ارز دیجیتال را به ذخایر خود اضافه کرده‌اند. سنتیمنت افزود این خرید را آدرس‌های حاوی ۱۰۰ تا ۱۰,۰۰۰ بیت کوین انجام داده‌اند و این نهنگ‌ها در حال حاضر ۴۸.۷ درصد کل بیت کوین جهان را در اختیار دارند. این آدرس‌ها در مجموع حدود ۹.۱۱ میلیون واحد بیت کوین دارند که ارزش آن تقریباً ۳۶۷ میلیارد دلار است. در همین حال، گلسنود اعلام کرد ماینرها هم مشغول ذخیره بیت کوین‌های خود هستند و فروش آن‌ها به پایین‌تر مقدار در ۵ ماه اخیر رسیده است.",
        "src_name": "CoinTelegraph",
        "src_link": "https://cointelegraph.com/news/millionaire-whales-gobble-up-90-000-bitcoin-over-past-25-days",
        "date": "2021-06-17"
    },
    {
        "title": "نگرانی‌های بنیانگذار کوین بیس درباره تنظیم مقررات ارزهای دیجیتال در آمریکا",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/354283_cbd4.jpg",
        "body": "فرد ارسام، هم‌بنیان‌گذار صرافی کوین بیس روز سه شنبه به بلومبرگ درباره نگرانی‌هایش نسبت به مساله نظارت بر ارزهای دیجیتال گفت که هنگام بررسی ارزهای دیجیتال، این خطر وجود دارد که تنظیم کنندگان، فرصت‌های موجود در این فضا را دست کم بگیرند و ریسک‌های موجود در آن را بیش از حد ارزیابی کنند.",
        "src_name": "Decrypt",
        "src_link": "https://decrypt.co/73838/danger-that-u-s-regulators-get-crypto-wrong-coinbase-co-founder",
        "date": "2021-06-17"
    },
    {
        "title": "سرمایه‌گذاری پی‌پل در پلتفرم اطلاعاتی بلاک چین تی‌آرام لبز",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/2e479f412a44e700a31a703dbd4121f3.jpg",
        "body": "پلتفرم اطلاعات بلاک چین تی‌آرام لبز (TRM Labs) در دور اول تامین سرمایه خود، از سوی شرکت‌های حوزه فناوری و ارزهای دیجیتال، ۱۴ میلیون دلار بودجه جمع‌آوری کرده است. این مرحله از تامین سرمایه تی‌آرام لبز توسط بسمر ونچر پارتنرز رهبری شد و صندوق‌های سرمایه‌گذاری خطرپذیر پی‌پل و سیلزفورس (Salesforce) نیز در آن مشارکت داشتند. گفتنی است که تی‌آرام به شرکت‌های بلاک چین، موسسات مالی و حتی نهادهای قانونی کمک می‌کند جرائم مالی مرتبط با ارزهای دیجیتال را شناسایی و از وقوع آن‌ها پیشگیری کنند.",
        "src_name": "CoinTelegraph",
        "src_link": "https://cointelegraph.com/news/paypal-salesforce-contribute-to-trm-labs-14m-investment-round",
        "date": "2021-06-17"
    },
    {
        "title": "یک راننده ناسکار حقوق خود را با بیت کوین و لایت کوین دریافت کرد",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/354347_3733-1024x683.jpeg",
        "body": "لاندون کاسیل، راننده مسابقات ماشین‌رانی ناسکار برای نخستین بار در تاریخ این مسابقات دستمزد خود را به طور کامل از طریق ارزهای دیجیتال دریافت کرد. این راننده قرار است حقوق خود را از طریق بیت کوین و لایت کوین دریافت کند. او با اشاره به اینکه از دریافت حقوقش با ارزهای دیجیتال احساس راحتی می‌کند، در این باره گفت: «تعداد انگشت شماری از رانندگان هستند که در حوزه ارزهای دیجیتال فعالیت می‌کنند. اما من یکی از آن‌ها هستم که احتمالا به اندازه کافی در این بخش فعال بوده و به همین خاطر با نحوه عملکرد آن‌ها آشنا هستم.»",
        "src_name": "U.TODAY",
        "src_link": "https://u.today/nascar-driver-landon-cassill-to-receive-his-salary-in-bitcoin-and-litecoin",
        "date": "2021-06-17"
    },
    {
        "title": "ابتکار ماینرهای بیت کوین برای ادامه فعالیت در چین",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/miner-6.jpg",
        "body": "به گزارش رسانه‌های محلی، برخی از ماینرهای بیت کوین در چین می‌خواهند برای تأمین برق مصرفی و ادامه فعالیت خود به استفاده از انرژی‌های تجدید پذیر روی آورند. مدیرعامل شرکت استخراج اس‌ای‌آی می‌گوید: «ما در حال همکاری با شرکت‌های تولید برق هستیم تا از وضعیت برق مازاد آنها مطلع شویم تا آنها بتوانند با تأمین برق برای استخراج بیت کوین از هدر رفت انرژی جلوگیری کنند.» استخراج بیت کوین به دلیل مصرف شدید برق و آلایندگی‌های زیست محیطی از ماه گذشته با محدودیت‌های شدیدی در این کشور مواجه شده است.",
        "src_name": "CryptoSlate",
        "src_link": "https://cryptoslate.com/bitcoin-btc-miners-in-china-plot-plans-to-go-green/",
        "date": "2021-06-17"
    },
    {
        "title": "بانک جهانی درخواست کمک السالوادور را رد کرد",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/thumbs_b_c_84c557c918a4e95069bc1510deda5a95.jpg",
        "body": "السالوادور از بانک جهانی درخواست کرده تا به این کشور در جریان روند پذیرش بیت کوین به عنوان پول قانونی کمک کند، اما بانک جهانی این درخواست را رد کرده است. سخنگوی بانک جهانی در این باره گفته است: «دولت السالوادور برای دریافت کمک در راستای پذیرش بیت کوین به ما مراجعه کرد، اما این چیزی نیست که بانک جهانی با توجه به مسائل مرتبط با محیط زیست و شفافیت بتواند از آن پشتیبانی کند.»",
        "src_name": "CoinTelegraph",
        "src_link": "https://cointelegraph.com/news/world-bank-refuses-el-salvador-s-request-for-help-on-btc-transition",
        "date": "2021-06-17"
    },
    {
        "title": "ای‌اس راک: ممنوعیت استخراج ارزهای دیجیتال در چین تقاضا برای کارت گرافیک را کاهش داده است",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/354300_a543.jpg",
        "body": "شرکت تولید سخت‌افزار ای‌اس راک (ASRock) اخیرا عنوان کرده است که سخت‌گیری دولت چین بر ماینینگ ارزهای دیجیتال و ریزش بازار در ماه مه، تقاضا برای کارت‌های گرافیک در این کشور را کاهش داده است. گفتنی است که اعمال محدودیت بر استخراج ارزهای دیجیتال یکی از عوامل ریزش بیت کوین تا ۳۲,۰۰۰ دلار بود و تاکنون ماینرها در چند استان چین از جمله یون‌نان و سین‌کیانگ فعالیت خود را متوقف کرده‌اند.",
        "src_name": "Decrypt",
        "src_link": "https://decrypt.co/73830/gpu-demand-down-in-wake-of-mays-crypto-crash-and-china-ban-asrock",
        "date": "2021-06-17"
    },
    {
        "title": "پیشنهاد وزیر ارتباطات برای تبدیل کیش به مرکز صرافی‌های ارز دیجیتال در منطقه",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/354277_2193.jpg",
        "body": "محمدجواد آذری جهرمی، وزیر ارتباطات و فناوری اطلاعات، در جریان سفری به جزیره کیش پیشنهاد تبدیل شدن این منطقه آزاد را به یک قطب بین‌المللی برای صرافی‌های ارزهای دیجیتال در منطقه مطرح کرده است. وی گفت: «کیش زیرساخت‌های لازم برای تبدیل شدن به مرکز صرافی‌های بین‌المللی ارز دیجیتال کشورهای منطقه را دارد و باید از این فرصت به بهترین نحو ممکن استفاده کرد.» این اظهارات در حالی عنوان شد که پیش از این فایننشال تریبیون گزارش داده بود ۱۲ واحد استخراج ارز دیجیتال در این جزیره مشغول به کار هستند.",
        "src_name": "Bitcoin.com",
        "src_link": "https://news.bitcoin.com/persian-gulf-island-to-become-crypto-exchange-hub-iran-minister-proposes/",
        "date": "2021-06-17"
    },
    {
        "title": "شرکت سرمایه‌گذاری ودبوش برای تسویه سهام خود از بلاک چین پکسوس استفاده می‌کند",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/Wedbush-hero.jpg",
        "body": "شرکت سرمایه‌گذاری آمریکایی ودبوش (Wedbush) که ۲.۴ میلیارد دلار سرمایه را تحت مدیریت دارد، می‌خواهد از فناوری بلاک چین برای تسویه سهام خود استفاده کند. این شرکت برای به کار گیری زیرساخت بلاک چین پکسوس نتورک (Paxos Network)، با این پروژه وارد همکاری شده است. گفتنی است که پیش‌تر نیز بنک آو امریکا، کردیت سوئیس، اینستینت و سوسیته ژنرال از زیرساخت بلاک چین پکسوس استفاده کرده‌اند.",
        "src_name": "CRYPTOBRIEFING",
        "src_link": "https://cryptobriefing.com/wedbush-will-use-paxos-network-to-settle-stocks/",
        "date": "2021-06-17"
    },
    {
        "title": "همکاری تزوس و تیم فرمول ۱ مک‌لارن برای راه‌اندازی پلتفرم توکن غیر مثلی",
        "image": "https://cdn.arzdigital.com/uploads/breaking-news/354281_9eff-1024x683.jpg",
        "body": "مک‌لارن، دومین تیم پرافتخار مسابقات فرمول ۱ قصد دارد با همکاری تزوس (Tezos) یک پلتفرم برای توکن‌های غیر مثلی راه‌اندازی کند. در بیانیه مطبوعاتی که درباره این همکاری منتشر شده، مک‌لارن اعلام کرده است که قصد دارد یک پلتفرم توکن غیر مثلی ایجاد کند که تجربه‌ای جذاب برای طرفدارانش به ارمغان بیاورد.",
        "src_name": "U.TODAY",
        "src_link": "https://u.today/2nd-most-successful-formula-1-team-mclaren-picks-tezos-to-build-nft-platform-on-it",
        "date": "2021-06-17"
    },
    {
        "title": "صرافی کراکن قصد دارد سهامش را در سال ۲۰۲۲ عرضه عمومی کند",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/Kraken-1-1024x576.jpg",
        "body": "جسی پاول، مدیرعامل صرافی آمریکایی کراکن در مصاحبه با بلومبرگ تی‌وی اعلام کرد که سهام این صرافی تا پایان سال ۲۰۲۲ عرضه عمومی خواهد شد. وی این اقدام را پیشرفت طبیعی کراکن در راستای ماموریت خود برای معرفی ارزهای دیجیتال به سراسر جهان خواند. سخنگوی کراکن در ماه مارس عنوان کرده بود که این شرکت بزرگ‌تر از آن است که از طریق ادغام با شرکت دیگر سهام خود را در بورس عرضه کند؛ در نتیجه احتمالا سهام کراکن از طریق عرضه اولیه عمومی به بازار سهام راه می‌یابد.",
        "src_name": "CoinTelegraph",
        "src_link": "https://cointelegraph.com/news/us-crypto-exchange-kraken-eyeing-public-listing-in-2022",
        "date": "2021-06-17"
    },
    {
        "title": "ریک ادلمن: بیت کوین اولین کلاس دارایی واقعا جدید در ۱۵۰ سال اخیر است",
        "image": "https://cdn.arzdigital.com/uploads/2021/06/ric-edelman-0417-1024x685.jpg",
        "body": "ریک ادلمن، بنیان‌گذار شرکت مشاوره مالی ادلمن فایننشال انجینز، دیروز در مصاحبه با یاهو فایننس بیت کوین و ارزهای دیجیتال را «اولین کلاس دارایی واقعا جدید در ۱۵۰ سال اخیر» خواند. به عقیده وی، از زمان پیدایش بازار طلا، کلاس دارایی نوآورانه‌ای همچون ارزهای دیجیتال وجود نداشته است و این نوع دارایی با سایر دارایی‌ها همچون سهام، اوراق قرضه، املاک و مستغلات، نفت و کالاها هیچ نقطه مشترکی ندارد.",
        "src_name": "CoinTelegraph",
        "src_link": "https://cointelegraph.com/news/bitcoin-first-genuinely-new-asset-class-in-150-years-says-ric-edelman",
        "date": "2021-06-17"
    }
]
recom=[
    [
        {
            "message": "گوش کن، دور ترین مرغ #جهان می‌خواند \nشب سلیس است، و یکدست، و باز",
            "postId": 11,
            "date": "2021-05-10T22:49:48.254696Z",
            "UserName": "iliya",
            "image": './poem-love-molana.jpg',
            "like": 2
        }
    ],
    [
        {
            "message": "ترا می‌خواهم و دانم که هرگز\nبه کام #دل در آغوشت نگیرم",
            "postId": 18,
            "date": "2021-05-11T11:14:42.204039Z",
            "UserName": "safari",
            "image": './lovely-poet-laureate.jpg',
            "like": 1
        }
    ],
    [
        {
            "message": "iran man payandeeeeeeee):::::",
            "postId": 15,
            "date": "2021-05-11T11:13:56.444250Z",
            "UserName": "mahziar",
            "image": None,
            "like": 1
        }
    ],
    [
        {
            "message": "سلام به  #یورو2020 ",
            "postId": 12,
            "date": "2021-05-11T00:18:01.722222Z",
            "UserName": "iliya",
            "image": './ruto-1024x574.jpg',
            "like": 1
        }
    ],
    [
        {
            "message": " من سلامی به گرمی #ایران اسلامی",
            "postId": 1,
            "date": "2021-05-09T22:15:26.118576Z",
            "UserName": "AnonymousUser",
            "image": "/media/Screenshot_66.png",
            "like": 1
        }
    ],
    [
        {
            "message": "miooooo",
            "postId": 37,
            "date": "2021-06-13T09:02:54.447862Z",
            "UserName": "iliya",
            "image": None,
            "like": 0
        }
    ],
    [
        {
            "message": "hi toooo",
            "postId": 36,
            "date": "2021-06-13T06:52:35.480787Z",
            "UserName": "iliya",
            "image": None,
            "like": 0
        }
    ],
    [
        {
            "message": "salam",
            "postId": 35,
            "date": "2021-06-12T17:24:54.456110Z",
            "UserName": "iliya",
            "image": None,
            "like": 0
        }
    ],
    [
        {
            "message": "are are",
            "postId": 34,
            "date": "2021-06-12T16:30:50.258648Z",
            "UserName": "iliya",
            "image": None,
            "like": 0
        }
    ]
]
rec=json.dumps(recom)
print(json.loads(rec)[0][0]['date'])
# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.
# postnum=0
id_yaro=0
username_input=''
# password_eror=0

def markup_twitte(like=0):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("بعدی", callback_data="next_twitt"),
                               InlineKeyboardButton("قبلی", callback_data="back_twitt"),InlineKeyboardButton(f"{like}❤️", callback_data="like"))

    return markup

def markup_email_notif():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("قعال کردن", callback_data="email_on"),
                               InlineKeyboardButton("غیر فعال کردن", callback_data="email_off"))

    return markup

def markup_news(link='www.pazapp.ir'):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("بعدی", callback_data="next_news"),
                               InlineKeyboardButton("قبلی", callback_data="back_news"),InlineKeyboardButton("مشاهده خبر", url=link))
    return markup


def markup_forget_pass():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("فراموشی رمز عبور",url='www.bitycle.com/forgetpassword' ,callback_data="forgetpassword"))
    return markup

def markup_signup_bott():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = InlineKeyboardButton("ثبت نام",url='www.pazapp.ir/register')
    itembtn2 = KeyboardButton('ورود')
    markup.add(itembtn1, itembtn2)

    return markup

def markup_menu():

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width=2
    itembtn1 = KeyboardButton('توییت ها📑')
    itembtn2 = KeyboardButton('اخبار📨')
    itembtn4 = KeyboardButton('ارسال توییت✏️')
    itembtn3 = KeyboardButton('تنظیمات⚙️')
    itembtn5 = KeyboardButton('راهنما🔖')
    markup.add(itembtn1, itembtn2,itembtn3,itembtn4,itembtn5)

    return markup
def strategy_menu():

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width=2
    itembtn1 = KeyboardButton('مشاهده استراتژی ها📊')
    itembtn2 = KeyboardButton('ویرایش استراتژی ها ✏️')
    itembtn3 = KeyboardButton('برگشت ↪️')

    markup.add(itembtn1, itembtn2,itembtn3)

    return markup
def nabz_menu():

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width=2
    itembtn1 = KeyboardButton('مشاهده قیمت💰')
    itembtn2 = KeyboardButton('مشاهده تابلو و چارت 📊')
    itembtn3 = KeyboardButton('فیلتر صعودی و نزولی 📈')
    itembtn4 = KeyboardButton('برگشت ↪️')

    markup.add(itembtn1, itembtn2,itembtn4,itembtn3)

    return markup
def assis_menu():

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width=2
    itembtn1 = KeyboardButton('دستیار تکنیکال📈')
    itembtn2 = KeyboardButton('دستیار فاندامنتال📡')
    itembtn3 = KeyboardButton('دستیار بایننس💵')
    itembtn4 = KeyboardButton('برگشت ↪️')

    markup.add(itembtn1, itembtn2,itembtn4,itembtn3)

    return markup
def notif_menu():

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row_width=2
    itembtn1 = KeyboardButton('تنظیم اعلان ها🔔')
    itembtn2 = KeyboardButton('برگشت ↪️')

    markup.add(itembtn2,itembtn1)

    return markup

def give_username(message):
    if (message.text) in usernamearr.keys():
        username_input=message.text

        # print(username_input)
        start_msg='لطفا رمز عبور خودرا  وارد نمایید'
        sent=bot.send_message(message.chat.id, start_msg)
        bot.register_next_step_handler(sent,give_password, username_input)
    elif 'ثبت نام' in message.text:
        start_msg=f' سلام {message.from_user.username} عزیز❤    \n\n از طریق لینک زیر اقدام به ثبت نام در سایت نمایید'
        bot.send_message(message.chat.id, start_msg , reply_markup=markup_signup())
    else :
        start_msg='لطفا  نام کاربری صحیح را وارد نمایید'
        sent=bot.send_message(message.chat.id, start_msg)
        bot.register_next_step_handler(sent,give_username)

def give_password(message,username_input):
    print(usernamearr[f'{username_input}'],message.text,username_input)
    if   message.text== usernamearr[f'{username_input}']:
        pass_input=message.text
        # print(pass_input)
        start_msg='خوش آمدید🌹\n  از منوی زیر بخش مورد نظر خودرا انتخاب کنید.'
        bot.send_message(message.chat.id, start_msg,reply_markup=markup_menu())
    elif 'ثبت نام' in message.text:
        start_msg=f' سلام {message.from_user.username} عزیز❤    \n\n از طریق لینک زیر اقدام به ثبت نام در سایت نمایید'
        bot.send_message(message.chat.id, start_msg , reply_markup=markup_signup())

    else:
        start_msg='لطفا رمز عبور صحیح را وارد نمایید'
        sent=bot.send_message(message.chat.id, start_msg)
        bot.register_next_step_handler(sent,give_password, username_input)

def setting(message):
    if 'تنظیم اعلان ها🔔' in message.text :
        start_msg='ارسال توییت ها به ایمیل'
        sent=bot.send_message(message.chat.id, start_msg,reply_markup=markup_email_notif())
    if  'برگشت' in message.text:
        start_msg='لطفا از منو زیر انتخاب نمایید'
        sent=bot.send_message(message.chat.id, start_msg,reply_markup=markup_menu())
def twittes(id1=id_yaro,num=0):
    global postnum,id_yaro
    postnum=num
    twitt=json.loads(rec)[num][0]

    if twitt['image']!=None:
        pic=twitt['image']
        photo = open(pic, 'rb')
        # body=f"\nS   {twitt['UserName']}   \n\n   {twitt['message']}    \n\n    {twitt['date']}        "
        body=f"\n👤 کاربر    {twitt['UserName']}    نوشت:\n\n📝 {twitt['message']}    \n\n📆 {twitt['date']} "
        bot.send_photo(id1,photo,caption=body,reply_markup=markup_twitte(twitt['like']))


    else:
        body=f"\n👤 کاربر   {twitt['UserName']}  نوشت:\n\n📝 {twitt['message']}   \n\n\n📆 {twitt['date']} "
        sent=bot.send_message(id1, body,reply_markup=markup_twitte(twitt['like']))




def write_twitte(message):
    start_msg='توییت شما با موفقیت ثبت شد'
    sent=bot.send_message(message.chat.id, start_msg,reply_markup=markup_menu())
    # print(message.__dict__)
    text=message.caption
    print(text)
    pic=message.json
    a=pic['photo'][0]['file_id']
    # print(pic)
    # pic=pic['photo'][0][0]
    # print(pic)
    # uniq='AQADN_GhL10AAyFOAAI'
    # pipi='AgACAgQAAxkBAAIBgGDMHHLc2hC6fCdRcsfNGVbiQmjdAAIztDEb8X9hUjZkPlc-AAHeJTfxoS9dAAMBAAMCAAN5AAMfTgACHwQ'
    # # pipi='AgACAgQAAxkBAAIBoGDMIcVYKa6DAAF8CamOlFh3-DgZ8gACM7QxG_F_YVI2ZD5XPgAB3iU38aEvXQADAQADAgADcwADIE4AAh8E'
    # pipi='AgACAgQAAxkBAAIBgGDMHHLc2hC6fCdRcsfNGVbiQmjdAAIztDEb8X9hUjZkPlc-AAHeJTfxoS9dAAMBAAMCAAN4AAMiTgACHwQ'
    bot.send_photo(message.chat.id,a, caption=text,reply_markup=markup_menu())

def news(id1=id_yaro,num=0):
    global newsnum,id_yaro
    newsnum=num
    new=newwws[num]

    pic=new['image']
    body=f"\n📣عنوان خبر:    {new['title']}\n\n\n📝شرح کوتاه:\n {new['body']}    \n\n📆 {new['date']}\n\n\n منبع خبر: {new['src_name']} "
    bot.send_photo(id1,pic,caption=body,reply_markup=markup_news(new['src_link']))



def nabz(message):
    if  'برگشت' in message.text:
        start_msg='لطفا از منو زیر انتخاب نمایید'
        sent=bot.send_message(message.chat.id, start_msg,reply_markup=markup_menu())

@bot.message_handler(func=lambda message: True)
def send_welcomes(message):
    global state,username_input,postnum,id_yaro,newsnum

    if 'start' in message.text:
        start_msg=f' سلام {message.from_user.username} عزیز❤    \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی\n اگه هنوز توی سایت ما\n🌐 www.pazapp.ir \n\n ثبت نام نکردی اول از طریق دکمه زیر ثبتنام کن'
        bot.send_message(message.chat.id, start_msg,reply_markup=markup_signup_bott())
    if 'help' in message.text:
        msg2='توییت ها📑\n -مشاهده جدیدترین توییت های دوستان شما\n-قابلیت لایک کردن \n\n'
        msg3='اخبار📨\n -مشاهده اخرین اخبار \n -همراه با مرجع و منبع خبر \n\n '
        msg4='ارسال توییت✏️\n -نوشتن توییت  \n\n'
        msg5='⚙️ تنظیمات\n -تنظیمات اعلان ها'
        start_msg=f' سلام {message.from_user.username} عزیز❤    \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی' +'\n\n'
        start_msg1=msg2+msg3+msg4+msg5
        bot.send_message(message.chat.id, start_msg,)
        bot.send_message(message.chat.id, start_msg1,)
    if 'راهنما' in message.text:
        msg2='توییت ها📑\n -مشاهده جدیدترین توییت های دوستان شما\n-قابلیت لایک کردن \n\n'
        msg3='اخبار📨\n -مشاهده اخرین اخبار \n -همراه با مرجع و منبع خبر \n\n '
        msg4='ارسال توییت✏️\n -نوشتن توییت  \n\n'
        msg5='⚙️ تنظیمات\n -تنظیمات اعلان ها'
        start_msg=f' سلام {message.from_user.username} عزیز❤    \n\n به ربات  🎖️پاز اپ🎖️ خوش اومدی' +'\n\n'
        start_msg1=msg2+msg3+msg4+msg5
        bot.send_message(message.chat.id, start_msg,)
        bot.send_message(message.chat.id, start_msg1,)
    if 'ثبت نام' in message.text:
        start_msg=f' سلام {message.from_user.username} عزیز❤    \n\n از طریق لینک زیر اقدام به ثبت نام در سایت نمایید'
        bot.send_message(message.chat.id, start_msg , reply_markup=markup_signup())
    if 'ورود' in message.text:
        start_msg='لطفا نام کاربری خودرا  وارد نمایید'
        sent=bot.send_message(message.chat.id, start_msg)
        bot.register_next_step_handler(sent,give_username)
    if 'توییت ها📑' in message.text:
        # start_msg='اماده ای1؟'
        id_yaro=message.chat.id
        # pic=twitt['image']
        # image='https://cdn.arzdigital.com/uploads/2021/05/ruto-1024x574.jpg'

        # # photo = open(image, 'rb')
        # # body=f"\nS   {twitt['UserName']}   \n\n   {twitt['message']}    \n\n    {twitt['date']}        "
        # bot.send_photo(id_yaro,image,caption='body',reply_markup=markup_twitte(5))



        # sent=bot.send_message(id_yaro, start_msg,reply_markup=markup_menu())
        # bot.send_photo(id_yaro,photo,caption='salam',reply_markup=markup_twitte())

        twittes(id_yaro,0)
    if 'اخبار📨' in message.text:
        id_yaro=message.chat.id
        news(id_yaro,0)

        # # start_msg='لطفا از منو زیر انتخاب نمایید'
        # sent=bot.send_message(message.chat.id, start_msg,reply_markup=strategy_menu())
        # bot.register_next_step_handler(sent,strategy)
    if 'ارسال توییت✏️' in message.text:
        start_msg='لطفا توییت مد نظر خودرا ارسال کنید'
        sent=bot.send_message(message.chat.id, start_msg,reply_markup=markup_menu())
        bot.register_next_step_handler(sent,write_twitte)
    if 'تنظیمات' in message.text:
        start_msg='لطفا از منو زیر انتخاب نمایید'
        sent=bot.send_message(message.chat.id, start_msg,reply_markup=notif_menu())
        bot.register_next_step_handler(sent,setting)
    if  'برگشت' in message.text:
        start_msg='لطفا از منو زیر انتخاب نمایید'
        sent=bot.send_message(message.chat.id, start_msg,reply_markup=markup_menu())
# bot.polling(none_stop=True)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global state,username_input,postnum,id_yaro,newsnum

    if call.data == "next_twitt":
        bot.answer_callback_query(call.id, "رفتیم بعدی")

        twittes(id_yaro,postnum+1)
    elif call.data == "back_twitt":
        bot.answer_callback_query(call.id, "رفتیم قبلی")

        twittes(id_yaro,postnum-1)
    elif call.data == "next_news":
        bot.answer_callback_query(call.id, "رفتیم بعدی")

        news(id_yaro,newsnum+1)
    elif call.data == "back_news":
        bot.answer_callback_query(call.id, "رفتیم قبلی")

        news(id_yaro,newsnum-1)
    elif call.data == "email_off":
        bot.answer_callback_query(call.id, "اعلان های ایمیل خاموش شد ")

    elif call.data == "email_on":
        bot.answer_callback_query(call.id, "اعلان های ایمیل روشن شد ")

    elif call.data == "like":
        bot.answer_callback_query(call.id, " لایک شد❤️")
        twitt=json.loads(rec)[postnum][0]
        twitt['like']=twitt['like']+1

# @bot.callback_query_handler(func=lambda call: True)
# def  test_callback(call):
#     print(call.contact)
#     # logger.info(call.contact)
#         # usernameget()
#     #     @bot.message_handler(func=lambda message: True)
#     #     def username(message):
#     # # print(message.from_user.username)
#     #         msg=message.text
#     #         print(msg)
#     #         bot.send_message(message.chat.id, 'password?')

#         # bot.answer_callback_query(call.id, "voroddd")

















# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if message.text=='/start':
#         # bot.reply_to(message, 'به ربات هوشمند bitycle خوش امدید')
# @bot.inline_handler(lambda query: query.query == 'video')
# def query_video(inline_query):
#     try:
#         r = InlineQueryResultVideo('1',
#                                          'https://github.com/eternnoir/pyTelegramBotAPI/blob/master/tests/test_data/test_video.mp4?raw=true',
#                                          'video/mp4', 'Video',
#                                          'https://raw.githubusercontent.com/eternnoir/pyTelegramBotAPI/master/examples/detailed_example/rooster.jpg',
#                                          'Title'
#                                          )
#         bot.answer_inline_query(inline_query.id, [r])
#     except Exception as e:
#         print(e)



# def gen_markup():
#     markup = InlineKeyboardMarkup()
#     markup.row_width = 2
#     markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
#                                InlineKeyboardButton("No", callback_data="cb_no"))
#     return markup

# def usernameget(message):
#     bot.send_message(message.chat.id, "username?")


# @bot.message_handler(func=lambda message: True)
# def message_handler(message):
#     bot.send_message(message.chat.id, "Yes/no?", reply_markup=gen_markup())



while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
















# {'content_type': 'photo', 'id': 384, 'message_id': 384, 'from_user': <telebot.types.User object at 0x7f9ca9434f40>, 'date': 1623989362, 'chat': <telebot.types.Chat object at 0x7f9ca9434c70>, 'forward_from': No
# ne, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None
# , 'author_signature': None, 'text': None, 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': [<telebot.types.PhotoSize object at 0x7f9ca9434b50>, <telebot.types.PhotoSize obj
# ect at 0x7f9ca94348e0>, <telebot.types.PhotoSize object at 0x7f9ca9434f70>, <telebot.types.PhotoSize object at 0x7f9ca9434250>], 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': 'ع
# حجی', 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': N
# one, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None, 'json': {'message_id': 384, 'from': {'id': 614286939, 'is_bot': False, 'first_name': 'safari_ir', 'username': 'safari_ir', 'language_code': 'fa'}, 'chat': {'id': 614286939, 'first_name': 'safari_ir', 'username': 'safari_ir', 'type': 'private'}, 'date': 1623989362, 'photo': [{'file_id': 'AgACAgQAAxkBAAIBgGDMHHLc2hC6fCdRcsfNGVbi
# QmjdAAIztDEb8X9hUjZkPlc-AAHeJTfxoS9dAAMBAAMCAANzAAMgTgACHwQ', 'file_unique_id': 'AQADN_GhL10AAyBOAAI', 'file_size': 1779, 'width': 90, 'height': 90}, {'file_id': 'AgACAgQAAxkBAAIBgGDMHHLc2hC6fCdRcsfNGVbiQmjdAA
# IztDEb8X9hUjZkPlc-AAHeJTfxoS9dAAMBAAMCAANtAAMhTgACHwQ', 'file_unique_id': 'AQADN_GhL10AAyFOAAI', 'file_size': 25896, 'width': 320, 'height': 320}, {'file_id': 'AgACAgQAAxkBAAIBgGDMHHLc2hC6fCdRcsfNGVbiQmjdAAIzt
# DEb8X9hUjZkPlc-AAHeJTfxoS9dAAMBAAMCAAN5AAMfTgACHwQ', 'file_unique_id': 'AQADN_GhL10AAx9OAAI', 'file_size': 90870, 'width': 1024, 'height': 1024}, {'file_id': 'AgACAgQAAxkBAAIBgGDMHHLc2hC6fCdRcsfNGVbiQmjdAAIztD
# Eb8X9hUjZkPlc-AAHeJTfxoS9dAAMBAAMCAAN4AAMiTgACHwQ', 'file_unique_id': 'AQADN_GhL10AAyJOAAI', 'file_size': 93987, 'width': 800, 'height': 800}], 'caption': 'عحجی'}}


# {'message_id': 416, 'from': {'id': 614286939, 'is_bot': False, 'first_name': 'safari_ir', 'username': 'safari_ir', 'language_code': 'fa'}, 'chat': {'id': 614286939, 'first_name': 'safari_ir', 'username': 'safari_ir', 'type': 'private'}, 'date': 1623990725, 'photo': [{'file_id': 'AgACAgQAAxkBAAIBoGDMIcVYKa6DAAF8CamOlFh3-DgZ8gACM7QxG_F_YVI2ZD5XPgAB3iU38aEvXQADAQADAgADcwADIE4AAh8E', 'file_unique_id': 'AQADN_GhL10AAyBOAAI', 'file_size': 1779, 'width': 90, 'height': 90}, {'file_id': 'AgACAgQAAxkBAAIBoGDMIcVYKa6DAAF8CamOlFh3-DgZ8gACM7QxG_F_YVI2ZD5XPgAB3iU38aEvXQADAQADAgADbQADIU4AAh8E', 'file_unique_id': 'AQADN_GhL10AAyFOAAI','file_size': 25896, 'width': 320, 'height': 320}, {'file_id': 'AgACAgQAAxkBAAIBoGDMIcVYKa6DAAF8CamOlFh3-DgZ8gACM7QxG_F_YVI2ZD5XPgAB3iU38aEvXQADAQADAgADeQADH04AAh8E', 'file_unique_id': 'AQADN_GhL10AAx9OAAI', 'file_size': 90870, 'width': 1024, 'height': 1024}, {'file_id': 'AgACAgQAAxkBAAIBoGDMIcVYKa6DAAF8CamOlFh3-DgZ8gACM7QxG_F_YVI2ZD5XPgAB3iU38aEvXQADAQADAgADeAADIk4AAh8E', 'file_unique_id': 'AQADN_GhL10AAyJOAAI', 'file_size': 93987, 'width': 800, 'height': 800}], 'caption': 'غغعب'}