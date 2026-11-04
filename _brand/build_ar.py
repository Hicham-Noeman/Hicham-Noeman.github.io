"""Build ar/index.html (Arabic, right-to-left) from index.html.

Re-run after changing the English page:  python _brand/build_ar.py
Every replacement must match, so the script stops if the English page has
changed in a way the translation table doesn't cover.
"""
import json
import re

s = open('index.html', encoding='utf-8').read()


def rep(old, new, count=None):
    global s
    n = s.count(old)
    if count is None:
        assert n >= 1, ('missing', old[:80])
    else:
        assert n == count, (n, old[:80])
    s = s.replace(old, new)


WA_EN = 'https://wa.me/96171684504?text=Hi%20Hicham%2C%20I%20found%20your%20website%20and%20would%20like%20to%20talk%20about%20a%20project.'
WA_AR = 'https://wa.me/96171684504?text=' + '%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%20%D9%87%D8%B4%D8%A7%D9%85%D8%8C%20%D9%88%D8%AC%D8%AF%D8%AA%20%D9%85%D9%88%D9%82%D8%B9%D9%83%20%D9%88%D8%A3%D9%88%D8%AF%20%D8%A7%D9%84%D8%AA%D8%AD%D8%AF%D8%AB%20%D9%85%D8%B9%D9%83%20%D8%B9%D9%86%20%D9%85%D8%B4%D8%B1%D9%88%D8%B9.'

FAQ_AR = [
    ("هل يمكنك تخصيص Business Central دون التأثير على التحديثات المستقبلية؟",
     "نعم. أبني التخصيصات كإضافات بلغة AL تعمل فوق النظام الأساسي بدلاً من تعديله، فلا تمحو تحديثات Microsoft تعديلاتك، وتبقى الترقيات سهلة الإدارة."),
    ("هل يمكن ربط Business Central بالأدوات الأخرى التي نستخدمها؟",
     "غالباً نعم. يربط Power Automate وPower Apps نظام Business Central بـ Microsoft 365 وTeams وOutlook — مثل الموافقات عبر Teams أو الإشعارات التلقائية بالبريد الإلكتروني. ويمكن ربط الأنظمة الأخرى عبر واجهات Business Central البرمجية (APIs)."),
    ("هل تعمل عن بُعد؟",
     "نعم. أقيم في طرابلس، لبنان، وأعمل حالياً عن بُعد مع ProService 365، وهي شركة مقرّها كندا. ورش العمل والعروض والدعم كلها تتم بسلاسة عبر الإنترنت."),
    ("هل تقدّم الدعم بعد التشغيل؟",
     "نعم. الدعم لا يتوقف عند الإطلاق: معالجة الأخطاء، مشاكل الأداء، التحسينات الصغيرة، وتدريب المستخدمين ليكون فريقك مرتاحاً في استخدام النظام."),
    ("لسنا متأكدين مما نحتاجه. من أين نبدأ؟",
     "بمحادثة قصيرة حول طريقة عمل مؤسستك اليوم وما الذي يبطئها. ومن هناك نحدد إن كان الحل الأنسب تعديلاً في الإعدادات، أو إضافة برمجية، أو أتمتة. راسلني عبر واتساب أو البريد الإلكتروني."),
]
FAQ_EN = [
    "Can you customize Business Central without breaking future updates?",
    "Can Business Central connect to the other tools we use?",
    "Do you work remotely?",
    "Do you help after go-live?",
    "We're not sure what we need. Where do we start?",
]

# ---------- head ----------
s = re.sub(r'  <script type="application/ld\+json">.*?</script>\n', '', s, flags=re.S)  # drop EN schemas
faqld = {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": "ar", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ_AR]}
rep('<html lang="en">', '<html lang="ar" dir="rtl">', 1)
rep('  <title>Hicham Noeman — Technical Consultant</title>', '  <title>هشام نعمان — مستشار تقني</title>', 1)
rep('<meta name="description" content="Hicham Noeman — Technical Consultant & Software Developer specializing in Microsoft Dynamics 365 Business Central, AL, Power Apps and Power Automate.">',
    '<meta name="description" content="هشام نعمان — مستشار تقني ومطوّر برمجيات متخصص في Microsoft Dynamics 365 Business Central وAL وPower Apps وPower Automate.">', 1)
rep('  <link rel="canonical" href="https://hicham-noeman.dev/">', '  <link rel="canonical" href="https://hicham-noeman.dev/ar/">', 1)
rep('  <meta property="og:locale" content="en_US">\n  <meta property="og:locale:alternate" content="ar_AR">',
    '  <meta property="og:locale" content="ar_AR">\n  <meta property="og:locale:alternate" content="en_US">', 1)
rep('  <meta property="og:url" content="https://hicham-noeman.dev/">', '  <meta property="og:url" content="https://hicham-noeman.dev/ar/">', 1)
rep('  <meta property="og:site_name" content="Hicham Noeman">', '  <meta property="og:site_name" content="هشام نعمان">', 1)
rep('content="Hicham Noeman — Technical Consultant">', 'content="هشام نعمان — مستشار تقني">', 2)
rep('content="Microsoft Dynamics 365 Business Central solutions with AL, Power Apps and Power Automate.">',
    'content="حلول Microsoft Dynamics 365 Business Central باستخدام AL وPower Apps وPower Automate.">', 2)
rep('content="Hicham Noeman — Technical Consultant, Business Central developer">', 'content="هشام نعمان — مستشار تقني ومطوّر Business Central">', 1)
rep('  <link rel="preconnect" href="https://fonts.googleapis.com">',
    '  <script type="application/ld+json">\n  ' + json.dumps(faqld, ensure_ascii=False) +
    '\n  </script>\n  <link rel="preconnect" href="https://fonts.googleapis.com">', 1)
rep('family=JetBrains+Mono:wght@400&display=swap', 'family=JetBrains+Mono:wght@400&family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&display=swap', 1)
rep('--font: "Manrope", system-ui,', '--font: "Manrope", "IBM Plex Sans Arabic", system-ui,', 1)

RTL_CSS = '''
    /* ---------- Arabic / right-to-left adjustments ---------- */
    [dir="rtl"] .hero h1, [dir="rtl"] .sec-head h2, [dir="rtl"] .ghost, [dir="rtl"] .row h3, [dir="rtl"] .cta h2,
    [dir="rtl"] .statement, [dir="rtl"] .stats strong, [dir="rtl"] .xp-sub, [dir="rtl"] .hero-left h2,
    [dir="rtl"] .hero-right .label, [dir="rtl"] .sk-num, [dir="rtl"] .skill-card h3 { letter-spacing: 0; }
    [dir="rtl"] .hero h1 { font-weight: 700; line-height: 1.2; }
    [dir="rtl"] .hero h1 .word { padding: .05em .04em .18em; }
    [dir="rtl"] .sec-head h2 { line-height: 1.35; padding-bottom: .05em; }
    [dir="rtl"] .cta h2 { line-height: 1.3; }
    [dir="rtl"] .statement { line-height: 1.6; }
    [dir="rtl"] .skip { left: auto; right: 16px; }
    [dir="rtl"] .btn svg, [dir="rtl"] .row .arr svg { transform: scaleX(-1); }
    [dir="rtl"] .btn:hover svg { transform: scaleX(-1) translate(2px, -2px); }
    [dir="rtl"] .btn.alt svg, [dir="rtl"] .btn.alt:hover svg { transform: none; }
    [dir="rtl"] .row::before { background: linear-gradient(270deg, rgba(47,123,246,.14), transparent 80%); }
    [dir="rtl"] .row:hover h3 { transform: translateX(-12px); }
    [dir="rtl"] .row:hover .arr { transform: rotate(-45deg); }
    [dir="rtl"] .stats div { border-left: 0; border-right: 1px solid var(--line); }
    [dir="rtl"] .stats div:first-child { border-right: 0; padding-right: 0; padding-left: 20px; }
    [dir="rtl"] .xp-btn { text-align: right; }
    [dir="rtl"] .stats strong { direction: ltr; unicode-bidi: isolate; text-align: right; }
    [dir="rtl"] .list li { padding-left: 0; padding-right: 20px; }
    [dir="rtl"] .list li::before { left: auto; right: 0; }
    [dir="rtl"] .preview .bar, [dir="rtl"] .preview pre { direction: ltr; text-align: left; }
    [dir="rtl"] .wa-float { right: auto; left: max(18px, env(safe-area-inset-left)); }
    @media (max-width: 760px) {
      [dir="rtl"] .stats div { padding: 20px 18px 20px 0; }
      [dir="rtl"] .stats div:nth-child(odd) { border-right: 0; padding-right: 0; }
    }
'''
rep('    @media (prefers-reduced-motion: reduce) {', RTL_CSS + '    @media (prefers-reduced-motion: reduce) {', 1)

# relative asset paths -> absolute (page lives in /ar/)
rep('src="images/hicham-cutout.webp"', 'src="/images/hicham-cutout.webp"', 1)

# ---------- nav ----------
rep('<a href="#about" class="skip">Skip to content</a>', '<a href="#about" class="skip">انتقل إلى المحتوى</a>', 1)
rep('<span class="dot"></span>Technical Consultant<span class="long">', '<span class="dot"></span>مستشار تقني<span class="long">', 1)
rep('<span class="long">&nbsp;@ ProService 365</span>', '<span class="long">&nbsp;في ProService 365</span>', 1)
rep('<nav id="nav" class="nav" aria-label="Main">', '<nav id="nav" class="nav" aria-label="القائمة الرئيسية">', 1)
for en, ar in [('About', 'نبذة'), ('Expertise', 'الاختصاص'), ('Experience', 'الخبرات'), ('Skills', 'المهارات'), ('FAQ', 'أسئلة شائعة'), ('Contact', 'تواصل')]:
    rep(f'">{en}</a></li>', f'">{ar}</a></li>', 1)
rep('<a class="lang" href="/ar/" hreflang="ar" lang="ar" title="النسخة العربية">عربي</a>',
    '<a class="lang" href="/" hreflang="en" lang="en" title="English version">EN</a>', 1)
rep("Let's Talk\n", 'لنتحدث\n', 1)
rep('aria-label="Open menu"', 'aria-label="فتح القائمة"', 1)
rep('open ? "Close menu" : "Open menu"', 'open ? "إغلاق القائمة" : "فتح القائمة"', 1)

# ---------- hero ----------
rep('<h1 id="title" aria-label="Hicham Noeman">', '<h1 id="title" aria-label="هشام نعمان">', 1)
rep('<span class="word outline" aria-hidden="true">Hicham</span>', '<span class="word outline" aria-hidden="true">هشام</span>', 1)
rep('<span class="word solid" aria-hidden="true">Noeman</span>', '<span class="word solid" aria-hidden="true">نعمان</span>', 1)
# Arabic letters must stay joined: animate whole words instead of single letters
rep('      [...text].forEach(ch => {', '      [text].forEach(ch => {', 1)
rep('<h2>Technical Consultant</h2>', '<h2>مستشار تقني</h2>', 1)
rep('<p>Business Central developer building AL extensions and Power Platform solutions.</p>',
    '<p>مطوّر Business Central، أبني إضافات بلغة AL وحلولاً على Power Platform.</p>', 1)
rep('Get in touch\n', 'تواصل معي\n', 1)
# The CV is English-only and linked from the English page: no CV button on the Arabic page
s, n = re.subn(r'\n *<a class="btn alt" href="/cv/Hicham-Noeman-CV\.pdf"[^>]*>View CV\n.*?</a>', '', s, flags=re.S)
assert n == 2, n
rep('alt="Portrait of Hicham Noeman"', 'alt="صورة هشام نعمان"', 1)
rep('Photo coming soon', 'الصورة قريباً', 1)
rep('<span class="label">Connect</span>', '<span class="label">تواصل</span>', 1)
rep('</svg>Email</a>', '</svg>البريد</a>', 1)
rep('</svg>WhatsApp</a>', '</svg>واتساب</a>', 1)
rep('<i></i>Scroll</div>', '<i></i>مرّر</div>', 1)
rep(WA_EN, WA_AR, 3)

# ---------- about ----------
rep('<span class="ghost" aria-hidden="true">ABOUT</span>', '<span class="ghost" aria-hidden="true">نبذة</span>', 1)
rep('<h2><span>/ABOUT</span></h2>', '<h2><span>/نبذة</span></h2>', 1)
rep('<span class="aside">Understand first. Code second.</span>', '<span class="aside">افهم أولاً، ثم اكتب الكود.</span>', 1)
rep('For me, development goes far beyond writing code. It starts with understanding how a business <em class="accent">actually works</em>, finding the challenge behind the process, and building the <em class="accent">right solution</em> around it.',
    'بالنسبة لي، التطوير أبعد بكثير من كتابة الكود. يبدأ بفهم كيف تعمل المؤسسة <em class="accent">فعلياً</em>، وإيجاد التحدي الكامن وراء كل عملية، ثم بناء <em class="accent">الحل المناسب</em> حوله.', 1)
rep('Curious by nature, always learning — and powered by tea.', 'فضولي بطبعي، دائم التعلّم — وطاقتي من الشاي.', 1)
rep('<span>Years of experience</span>', '<span>سنوات من الخبرة</span>', 1)
rep('<span>Roles & positions</span>', '<span>أدوار ومناصب</span>', 1)
rep('<span>Business Central extensions</span>', '<span>إضافات Business Central</span>', 1)
rep('<div><strong>B.Sc.</strong><span>Computer Science</span></div>', '<div><strong>B.Sc.</strong><span>إجازة في علوم الكمبيوتر</span></div>', 1)

# ---------- expertise ----------
rep('<span class="ghost" aria-hidden="true">EXPERTISE</span>', '<span class="ghost" aria-hidden="true">الاختصاص</span>', 1)
rep('<h2><span>/EXPERTISE</span></h2>', '<h2><span>/الاختصاص</span></h2>', 1)
rep('<span class="aside">What I work on</span>', '<span class="aside">ما أعمل عليه</span>', 1)
rep('<h3>Business Central Development</h3><p>Custom AL extensions — tables, pages, reports and logic.</p>',
    '<h3>تطوير Business Central</h3><p>إضافات AL مخصّصة — جداول، صفحات، تقارير ومنطق عمل.</p>', 1)
rep('<h3>ERP Implementation</h3><p>From requirements to go-live.</p>', '<h3>تطبيق أنظمة ERP</h3><p>من تحليل المتطلبات حتى الإطلاق.</p>', 1)
rep('<h3>Power Platform Automation</h3><p>Power Apps and Power Automate connected to Business Central.</p>',
    '<h3>الأتمتة عبر Power Platform</h3><p>Power Apps وPower Automate مرتبطة بـ Business Central.</p>', 1)
rep('<h3>Optimization & Support</h3><p>Debugging, performance and user training.</p>',
    '<h3>التحسين والدعم</h3><p>معالجة الأخطاء، تحسين الأداء وتدريب المستخدمين.</p>', 1)
rep('<div class="ttl">Implementation lifecycle</div><div class="tags"><span>Requirements</span><span>Fit-gap</span><span>Solution design</span><span>Development</span><span>UAT</span><span>Go-live</span><span>Support</span></div>',
    '<div class="ttl">مراحل التطبيق</div><div class="tags"><span>المتطلبات</span><span>تحليل الفجوات</span><span>تصميم الحل</span><span>التطوير</span><span>اختبار المستخدمين</span><span>الإطلاق</span><span>الدعم</span></div>', 1)
rep('<div class="ttl">Reliability first</div><div class="tags"><span>Debugging</span><span>Performance</span><span>Testing</span><span>User training</span><span>Documentation</span></div>',
    '<div class="ttl">الموثوقية أولاً</div><div class="tags"><span>معالجة الأخطاء</span><span>الأداء</span><span>الاختبار</span><span>تدريب المستخدمين</span><span>التوثيق</span></div>', 1)

# ---------- experience ----------
rep('<span class="ghost" aria-hidden="true">EXPERIENCE</span>', '<span class="ghost" aria-hidden="true">الخبرات</span>', 1)
rep('<h2><span>/EXPERIENCE</span></h2>', '<h2><span>/الخبرات</span></h2>', 1)
rep('<span class="aside">2022 — Now</span>', '<span class="aside">2022 — الآن</span>', 1)
rep('<span class="ro">Software Developer · Technical Consultant</span>', '<span class="ro">مطوّر برمجيات · مستشار تقني</span>', 1)
rep('<span class="dt">Apr 2023 — <span class="now">Now</span></span>', '<span class="dt">نيسان 2023 — <span class="now">الآن</span></span>', 1)
rep('<div class="meta">Canada · Remote</div>', '<div class="meta">كندا · عن بُعد</div>', 1)
rep('<li>Business Central extensions in AL — tables, pages, reports and logic</li>', '<li>إضافات Business Central بلغة AL — جداول، صفحات، تقارير ومنطق عمل</li>', 1)
rep('<li>ERP implementations, from requirements to deployment</li>', '<li>تطبيق أنظمة ERP، من المتطلبات حتى التشغيل</li>', 1)
rep('<li>Power Apps and Power Automate integrated with Business Central</li>', '<li>Power Apps وPower Automate مدمجة مع Business Central</li>', 1)
rep('<li>Debugging, optimization and end-user support</li>', '<li>معالجة الأخطاء، التحسين ودعم المستخدمين</li>', 1)
rep('<span class="ro">Python Trainer</span>', '<span class="ro">مدرّب Python</span>', 1)
rep('<span class="dt">Jul 2025 — Aug 2025</span>', '<span class="dt">تموز 2025 — آب 2025</span>', 1)
rep('<div class="meta">Tripoli, Lebanon</div>', '<div class="meta">طرابلس، لبنان</div>', 1)
rep('<li>Taught Python and programming logic to Grades 10–11</li>', '<li>تعليم Python والتفكير البرمجي لطلاب الصفّين العاشر والحادي عشر</li>', 1)
rep('<li>Hands-on, project-based coding sessions</li>', '<li>جلسات برمجة تطبيقية قائمة على المشاريع</li>', 1)
rep('<span class="ro">Campus Ambassador · Jinan University</span>', '<span class="ro">سفير الحرم الجامعي · جامعة الجنان</span>', 1)
rep('<span class="dt">Mar 2024 — Mar 2025</span>', '<span class="dt">آذار 2024 — آذار 2025</span>', 1)
rep('<div class="meta">Volunteer</div>', '<div class="meta">تطوّع</div>', 1)
rep('<li>Organized AI events and workshops on campus</li>', '<li>تنظيم فعاليات وورش عمل في الذكاء الاصطناعي داخل الجامعة</li>', 1)
rep('<li>Built and delivered introductory AI courses</li>', '<li>إعداد وتقديم دورات تمهيدية في الذكاء الاصطناعي</li>', 1)
rep('<span>AI</span><span>Workshops</span><span>Course design</span>', '<span>الذكاء الاصطناعي</span><span>ورش عمل</span><span>تصميم الدورات</span>', 1)
rep('<h3 class="xp-sub reveal">Other experience</h3>', '<h3 class="xp-sub reveal">خبرات أخرى</h3>', 1)
rep('<span class="ro">Social Media Manager & Graphic Designer</span></span><span class="dt">Aug 2025 — Aug 2026</span>',
    '<span class="ro">مدير وسائل التواصل الاجتماعي ومصمّم غرافيك</span></span><span class="dt">آب 2025 — آب 2026</span>', 1)
rep('<span class="ro">Administrative & Student Affairs Officer</span></span><span class="dt">Oct 2025 — Jun 2026</span>',
    '<span class="ro">مسؤول إداري وشؤون الطلاب</span></span><span class="dt">تشرين الأول 2025 — حزيران 2026</span>', 1)
rep('<span class="ro">Project Officer</span></span><span class="dt">Dec 2022 — Aug 2025</span>',
    '<span class="ro">مسؤول مشاريع</span></span><span class="dt">كانون الأول 2022 — آب 2025</span>', 1)
rep('<span class="ro">Initiatives Manager · Volunteer</span></span><span class="dt">Jan 2024 — Apr 2025</span>',
    '<span class="ro">مدير مبادرات · تطوّع</span></span><span class="dt">كانون الثاني 2024 — نيسان 2025</span>', 1)

# ---------- skills ----------
rep('<span class="ghost" aria-hidden="true">SKILLS</span>', '<span class="ghost" aria-hidden="true">المهارات</span>', 1)
rep('<h2><span>/SKILLS</span></h2>', '<h2><span>/المهارات</span></h2>', 1)
rep('<span class="aside">Tools of the trade</span>', '<span class="aside">أدوات العمل</span>', 1)
for en, ar in [('01 · CORE', '01 · الأساس'), ('02 · LIFECYCLE', '02 · دورة العمل'), ('03 · FOUNDATION', '03 · القاعدة'), ('04 · PROFESSIONAL', '04 · مهني')]:
    rep(f'<span class="sk-num">{en}</span>', f'<span class="sk-num">{ar}</span>', 1)
for en, ar in [('Microsoft Ecosystem', 'منظومة Microsoft'), ('Delivery', 'التنفيذ'), ('Programming & Data', 'البرمجة والبيانات'), ('Leadership & Design', 'القيادة والتصميم')]:
    rep(f'<h3>{en}</h3>', f'<h3>{ar}</h3>', 1)
for en, ar in [('AL Programming', 'برمجة AL'), ('ERP Implementation', 'تطبيق أنظمة ERP'), ('Requirements Analysis', 'تحليل المتطلبات'),
               ('Solution Design', 'تصميم الحلول'), ('Integrations', 'ربط الأنظمة'), ('Testing & Debugging', 'الاختبار ومعالجة الأخطاء'),
               ('Performance', 'الأداء'), ('Deployment', 'النشر'), ('Documentation', 'التوثيق'),
               ('Object-Oriented Programming', 'البرمجة كائنية التوجّه'), ('Data Structures', 'هياكل البيانات'), ('Databases', 'قواعد البيانات'),
               ('Web Development', 'تطوير الويب'), ('AI Fundamentals', 'أساسيات الذكاء الاصطناعي'), ('Project Management', 'إدارة المشاريع'),
               ('Team Leadership', 'قيادة الفرق'), ('UI / UX Design', 'تصميم UI / UX'), ('Graphic Design', 'التصميم الغرافيكي')]:
    rep(f'<li>{en}</li>', f'<li>{ar}</li>', 1)

# ---------- education ----------
rep('<span class="ghost" aria-hidden="true">EDUCATION</span>', '<span class="ghost" aria-hidden="true">التعليم</span>', 1)
rep('<h2><span>/EDUCATION</span></h2>', '<h2><span>/التعليم</span></h2>', 1)
rep('<span class="co">Jinan University — Lebanon</span><span class="ro">Bachelor\'s degree, Computer Science</span>',
    '<span class="co">جامعة الجنان — لبنان</span><span class="ro">إجازة في علوم الكمبيوتر</span>', 1)
rep('<span class="dt">Feb 2022 — Jan 2025</span>', '<span class="dt">شباط 2022 — كانون الثاني 2025</span>', 1)
rep('<div class="meta">Lebanon</div>', '<div class="meta">لبنان</div>', 1)
rep('<li>OOP, data structures, databases and web development</li>', '<li>البرمجة كائنية التوجّه، هياكل البيانات، قواعد البيانات وتطوير الويب</li>', 1)
rep('<li>Projects in Python and MySQL</li>', '<li>مشاريع باستخدام Python وMySQL</li>', 1)
rep('<div class="ttl">B.Sc. Computer Science</div>', '<div class="ttl">إجازة في علوم الكمبيوتر</div>', 1)

# ---------- FAQ ----------
rep('<span class="ghost" aria-hidden="true">FAQ</span>', '<span class="ghost" aria-hidden="true">أسئلة</span>', 1)
rep('<h2><span>/FAQ</span></h2>', '<h2><span>/أسئلة شائعة</span></h2>', 1)
rep('<span class="aside">Questions clients ask</span>', '<span class="aside">أسئلة يطرحها العملاء</span>', 1)
en_answers = re.findall(r'<div class="xp-body"><p>(.*?)</p></div>', s)
assert len(en_answers) == 5, len(en_answers)
for q_en, (q_ar, a_ar), a_en in zip(FAQ_EN, FAQ_AR, en_answers):
    rep(f'<span class="co">{q_en}</span>', f'<span class="co">{q_ar}</span>', 1)
    rep(f'<div class="xp-body"><p>{a_en}</p></div>', f'<div class="xp-body"><p>{a_ar}</p></div>', 1)

# ---------- contact + footer ----------
rep('<span class="dot"></span>Get in touch</span>', '<span class="dot"></span>تواصل معي</span>', 1)
rep('<h2>Let\'s <span class="outline">connect.</span></h2>', '<h2>لنبقَ <span class="outline">على تواصل.</span></h2>', 1)
rep('Email me\n', 'راسلني\n', 1)
rep('<a class="social" href="mailto:hnoeman@proservice365.com">Email</a>', '<a class="social" href="mailto:hnoeman@proservice365.com">البريد</a>', 1)
rep('rel="noopener">WhatsApp</a>', 'rel="noopener">واتساب</a>', 1)
rep('aria-label="Chat on WhatsApp"', 'aria-label="تواصل عبر واتساب"', 1)
rep('<span>© <span id="yr"></span> Hicham Noeman</span>', '<span>© <span id="yr"></span> هشام نعمان</span>', 1)
rep('<span>Understand the operation first. Code second.</span>', '<span>افهم العمل أولاً، ثم اكتب الكود.</span>', 1)

# guard: no leftover English UI text that should have been translated
for leftover in ['>About<', '>Skills<', 'Get in touch', 'View CV', 'Hicham-Noeman-CV.pdf', 'Other experience', 'Questions clients ask', 'Scroll<']:
    assert leftover not in s, leftover

open('ar/index.html', 'w', encoding='utf-8', newline='').write(s)
print('ar/index.html written')
