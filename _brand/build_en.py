"""One-off: add FAQ, CV buttons, language switch and hreflang to index.html."""
import json

p = 'index.html'
s = open(p, encoding='utf-8').read()


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (n, old[:70])
    s = s.replace(old, new)


FAQ = [
    ("Can you customize Business Central without breaking future updates?",
     "Yes. I build customizations as AL extensions, which sit on top of the standard system instead of changing it. Microsoft's updates don't overwrite your changes, and upgrades stay manageable."),
    ("Can Business Central connect to the other tools we use?",
     "Usually, yes. Power Automate and Power Apps connect Business Central to Microsoft 365, Teams and Outlook — for example approvals in Teams or automatic email notifications. Other systems can be integrated through Business Central's APIs."),
    ("Do you work remotely?",
     "Yes. I'm based in Tripoli, Lebanon, and I already work remotely with ProService 365, a team based in Canada. Workshops, demos and support all run smoothly online."),
    ("Do you help after go-live?",
     "Yes. Support doesn't stop at deployment: debugging, performance issues, small improvements and training your users so the team is comfortable with the system."),
    ("We're not sure what we need. Where do we start?",
     "With a short conversation about how your business works today and what's slowing you down. From there we can see whether a configuration change, an extension or an automation is the right fit. Message me on WhatsApp or by email."),
]

rep('  <link rel="canonical" href="https://hicham-noeman.dev/">',
    '  <link rel="canonical" href="https://hicham-noeman.dev/">\n'
    '  <link rel="alternate" hreflang="en" href="https://hicham-noeman.dev/">\n'
    '  <link rel="alternate" hreflang="ar" href="https://hicham-noeman.dev/ar/">\n'
    '  <link rel="alternate" hreflang="x-default" href="https://hicham-noeman.dev/">')
rep('  <meta property="og:locale" content="en_US">',
    '  <meta property="og:locale" content="en_US">\n  <meta property="og:locale:alternate" content="ar_AR">')
rep('    "name": "Hicham Noeman",\n', '    "name": "Hicham Noeman",\n    "alternateName": "هشام نعمان",\n')
faqld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]}
rep('  <link rel="preconnect" href="https://fonts.googleapis.com">',
    '  <script type="application/ld+json">\n  ' + json.dumps(faqld, ensure_ascii=False) +
    '\n  </script>\n  <link rel="preconnect" href="https://fonts.googleapis.com">')

rep('    .social { display: inline-flex;',
    '''    .btn.alt { background: rgba(255, 255, 255, .06); color: var(--text); border: 1px solid var(--glass-border); }
    .btn.alt:hover { background: rgba(255, 255, 255, .12); box-shadow: none; }
    .btn.alt:hover svg { transform: translateY(2px); }
    .btn-row { display: flex; flex-wrap: wrap; gap: 10px; }
    .cta .btn-row { justify-content: center; }
    .social { display: inline-flex;''')
rep('    .menu-btn { display: none;',
    '''    .nav-end { display: flex; align-items: center; gap: 10px; }
    .lang { display: inline-grid; place-items: center; min-width: 44px; height: 40px; padding: 0 14px; border-radius: 100px; font-size: .85rem; font-weight: 600; color: var(--ice); background: rgba(255,255,255,.05); border: 1px solid var(--glass-border); transition: background .3s; }
    .lang:hover { background: rgba(255,255,255,.12); }
    .menu-btn { display: none;''')
rep('      .menu-btn { display: grid; }', '      .menu-btn { display: grid; }\n      .lang { height: 44px; }')
rep('      .hero-left { max-width: 560px; align-self: center; text-align: center; }',
    '      .hero-left { max-width: 560px; align-self: center; text-align: center; }\n      .hero-left .btn-row { justify-content: center; }')
rep('    /* ---------- CTA ---------- */',
    '''    /* ---------- FAQ ---------- */
    .faq { padding: 0 0 var(--pad-y); }
    .faq .xp-btn { grid-template-columns: 1fr 40px; }
    .faq .xp-btn .co { font-size: clamp(1.05rem, 1.8vw, 1.25rem); }
    .faq .xp-body { grid-template-columns: 1fr; }
    .faq .xp-body p { max-width: 760px; }
    @media (max-width: 760px) { .faq .xp-btn { grid-template-columns: 1fr 36px; } .faq .xp-btn .pm { grid-row: 1; } }

    /* ---------- CTA ---------- */''')

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M7 17 17 7M8 7h9v9"/></svg>'
rep(f'''    <a class="btn nav-cta" href="#contact">Let's Talk
      {ARROW}</a>
    <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><span></span></button>''',
    f'''    <div class="nav-end">
      <a class="lang" href="/ar/" hreflang="ar" lang="ar" title="النسخة العربية">عربي</a>
      <a class="btn nav-cta" href="#contact">Let's Talk
        {ARROW}</a>
      <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><span></span></button>
    </div>''')
rep('      <li><a href="#skills">Skills</a></li>', '      <li><a href="#skills">Skills</a></li>\n      <li><a href="#faq">FAQ</a></li>')

DL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 4v12M6 11l6 6 6-6M5 20h14"/></svg>'
CV = f'<a class="btn alt" href="/cv/Hicham-Noeman-CV.pdf" download>Download CV\n              {DL}</a>'
rep(f'''          <a class="btn" href="#contact">Get in touch
            {ARROW}</a>''',
    f'''          <div class="btn-row">
            <a class="btn" href="#contact">Get in touch
              {ARROW}</a>
            {CV}
          </div>''')
rep(f'''        <a class="btn" href="mailto:hnoeman@proservice365.com">Email me
          {ARROW}</a>''',
    f'''        <div class="btn-row">
          <a class="btn" href="mailto:hnoeman@proservice365.com">Email me
            {ARROW}</a>
          {CV}
        </div>''')

items = ''.join(f'''
          <div class="xp-item reveal">
            <button class="xp-btn" aria-expanded="false" aria-controls="faq{i}">
              <span class="co">{q}</span>
              <span class="pm" aria-hidden="true"></span>
            </button>
            <div class="xp-panel" id="faq{i}"><div>
              <div class="xp-body"><p>{a}</p></div>
            </div></div>
          </div>''' for i, (q, a) in enumerate(FAQ, 1))
rep('    <!-- CTA -->', f'''    <!-- FAQ -->
    <section class="faq" id="faq">
      <div class="wrap">
        <div class="sec-head">
          <span class="ghost" aria-hidden="true">FAQ</span>
          <h2><span>/FAQ</span></h2>
          <span class="aside">Questions clients ask</span>
        </div>
        <div class="xp">{items}
        </div>
      </div>
    </section>

    <!-- CTA -->''')

open(p, 'w', encoding='utf-8', newline='').write(s)
print('ok')
