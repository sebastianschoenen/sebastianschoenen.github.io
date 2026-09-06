#!/usr/bin/env python3
"""Generates index.html (EN) and de/index.html (DE) plus sitemap.xml/robots.txt
from a single content source. Run: python3 build.py
"""
import json, html as H, datetime
from pathlib import Path

SITE = "https://sebastianschoenen.github.io/"
PHOTO = "SebastianSchoenen.jpg"
LINKEDIN = "https://www.linkedin.com/in/dr-sebastian-schoenen-b24898153/"
RESEARCHGATE = "https://www.researchgate.net/profile/Sebastian-Schoenen"
LASTMOD = datetime.date.today().isoformat()
YEAR = str(datetime.date.today().year)

exec(open(Path(__file__).parent / "content.py", encoding="utf-8").read())

ICONS = {
 "phd":'<path d="M12 3L1 9l11 6 9-4.91V17h2V9L12 3zM5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82z"/>',
 "msc":'<path d="M4 6h16v2H4zm0 5h16v2H4zm0 5h10v2H4z"/>',
 "work":'<path d="M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z"/>',
 "net":'<path d="M12 2a5 5 0 015 5c0 1.6-.8 3-2 3.9V13h3a3 3 0 013 3v1h2v5h-6v-5h2v-1a1 1 0 00-1-1h-3v2h2v5H8v-5h2v-2H7a1 1 0 00-1 1v1h2v5H2v-5h2v-1a3 3 0 013-3h3v-2.1A5 5 0 017 7a5 5 0 015-5zm0 2a3 3 0 100 6 3 3 0 000-6z"/>',
 "pin":'<path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/>',
 "lang":'<path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm6.93 6h-2.95c-.32-1.25-.78-2.45-1.38-3.56 1.84.63 3.37 1.91 4.33 3.56zM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96zM4.26 14C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2s.06 1.34.14 2H4.26zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56-1.84-.63-3.37-1.9-4.33-3.56zm2.95-8H5.08c.96-1.66 2.49-2.93 4.33-3.56C8.81 5.55 8.35 6.75 8.03 8zM12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96zM14.34 14H9.66c-.09-.66-.16-1.32-.16-2s.07-1.35.16-2h4.68c.09.65.16 1.32.16 2s-.07 1.34-.16 2zm.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95c-.96 1.65-2.49 2.93-4.33 3.56zM16.36 14c.08-.66.14-1.32.14-2s-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2h-3.38z"/>',
 "li":'<path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>',
}
LI_SVG = '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'+ICONS["li"]+'</svg>'

def jsonld(t):
    person = {
      "@context":"https://schema.org","@type":"Person","@id":SITE+"#person",
      "name":"Sebastian Schoenen","honorificPrefix":"Dr.","givenName":"Sebastian","familyName":"Schoenen",
      "alternateName":"Dr. Sebastian Schoenen","url":SITE,"image":SITE+PHOTO,
      "jobTitle":["Director of Innovation & Technology","Head of Data & AI Center of Excellence"],
      "worksFor":[
        {"@type":"Organization","name":"ControlExpert GmbH","url":"https://www.controlexpert.com/","address":{"@type":"PostalAddress","addressLocality":"Langenfeld (Rheinland)","addressCountry":"DE"}},
        {"@type":"Organization","name":"Solvd Group","url":"https://solvd.group/"}],
      "alumniOf":{"@type":"CollegeOrUniversity","name":"RWTH Aachen University","url":"https://www.rwth-aachen.de/"},
      "hasCredential":{"@type":"EducationalOccupationalCredential","credentialCategory":"degree","name":"Ph.D. in Physics","recognizedBy":{"@type":"CollegeOrUniversity","name":"RWTH Aachen University"}},
      "address":{"@type":"PostalAddress","addressRegion":"North Rhine-Westphalia","addressCountry":"DE"},
      "nationality":{"@type":"Country","name":"Germany"},
      "knowsLanguage":["de","en"],
      "knowsAbout":["Agentic AI","Generative AI","Computer Vision","Deep Learning","Machine Learning","Insurance Claims Management","Motor Insurance","Fraud Detection","Astroparticle Physics","AI Governance"],
      "award":["AI Communication Award 2026 – AI Strategy, Analytics & Agents in Communication (ClaimsPilot)","KI Innovation Award 2024 – F.A.Z. Institut & KI Bundesverband","Springorum Denkmünze – RWTH Aachen (2013)","DFG Research Training Group scholarship – RWTH Aachen (2013)","3rd place Talanx Insurance Hackathon (2018)"],
      "sameAs":[LINKEDIN,RESEARCHGATE],
    }
    site = {"@context":"https://schema.org","@type":"WebSite","@id":SITE+"#website","url":SITE,"name":"Dr. Sebastian Schoenen","inLanguage":["en","de"],"about":{"@id":SITE+"#person"},"publisher":{"@id":SITE+"#person"}}
    page = {"@context":"https://schema.org","@type":"ProfilePage","url":t["url"],"inLanguage":t["lang"],"name":t["og_title"],"description":t["description"],"mainEntity":{"@id":SITE+"#person"},"dateModified":LASTMOD,"isPartOf":{"@id":SITE+"#website"}}
    return "\n".join(f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in (person, site, page))

def status_pill(t, s):
    return {"ongoing":f'<span class="pill pill-ongoing">{t["ongoing"]}</span>',
            "done":f'<span class="pill pill-done">{t["completed"]}</span>',
            "upcoming":f'<span class="pill pill-upcoming">{t["upcoming"]}</span>'}.get(s,"")

def li(cls, items): return "".join(f'<li class="{cls}">{x}</li>' for x in items)

def render(t):
    p = t["prefix"]
    nav_links = "".join(f'<li><a href="{h}" data-section="{h[1:]}">{l}</a></li>' for h,l in t["nav"])
    mob_links = "".join(f'<a href="{h}">{l}</a>' for h,l in t["nav"])
    cur = ' aria-current="page"'
    en_href, de_href = ("./", "de/") if t["lang"]=="en" else ("../", "./")
    lang_sw = (f'<a href="{en_href}" hreflang="en" lang="en"{cur if t["lang"]=="en" else ""}>EN</a>'
               f'<a href="{de_href}" hreflang="de" lang="de"{cur if t["lang"]=="de" else ""}>DE</a>')
    badges = li("badge", t["hero_badges"])
    stats = "".join(f'<li class="hero-stat"><div class="stat-num">{n}</div><div class="stat-lbl">{l}</div></li>' for n,l in t["hero_stats"])
    about_p = "".join(f"<p>{x}</p>" for x in t["about_p"])
    about_cards = "".join(f'<div class="info-card reveal"><div class="info-icon"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[i]}</svg></div><div><h3>{h}</h3><p>{d}</p></div></div>' for i,h,d in t["about_cards"])
    exp = "".join(f'<li class="t-item reveal"><div class="t-dot" aria-hidden="true"></div><div class="t-period">{per}</div><h3 class="t-role">{H.escape(role)}</h3><div class="t-company">{H.escape(co)}</div><p class="t-desc">{desc}</p><ul class="t-tags">{li("t-tag",tags)}</ul></li>' for per,role,co,desc,tags in t["exp"])
    skills = "".join(f'<div class="skill-cat reveal"><h3>{h}</h3><ul class="skill-pills">{li("skill-pill",xs)}</ul></div>' for h,xs in t["skills"])
    impact = "".join(f'<li class="impact-stat"><div class="impact-stat-num">{n}</div><div class="impact-stat-lbl">{l}</div></li>' for n,l in t["impact"])
    tabs = "".join(f'<button class="tab-btn{" active" if i==0 else ""}" role="tab" id="tabbtn-{k}" aria-controls="tab-{k}" aria-selected="{"true" if i==0 else "false"}" data-tab="{k}">{l} <span class="tab-count">{c}</span></button>' for i,(k,l,c) in enumerate(t["tabs"]))
    products = "".join(f'<li class="card-base reveal prod-card"><span class="pill {"pill-flagship" if fl else "pill-ai"}">{t["flagship"] if fl else t["ai_product"]}</span><h3>{h}</h3><p>{d}</p><div class="card-meta"><strong>{m}</strong></div></li>' for h,d,m,fl in t["products"])
    patents = "".join(f'<li class="card-base reveal patent-card"><span class="pill pill-patent">{j}</span><h3>{h}</h3><p>{d}</p><div class="patent-num">{n}</div></li>' for j,h,d,n in t["patents"])
    research = "".join(f'<li class="card-base reveal research-card"><div class="pill-row"><span class="pill pill-research">{f}</span>{status_pill(t,s)}</div><h3>{h}</h3><p>{d}</p><div class="card-meta"><strong>{m}</strong>{(" · "+per) if per else ""}</div></li>' for f,h,d,m,per,s in t["research"])
    pubs = ""
    for gh, items in t["pub_groups"]:
        cards = "".join(f'<li class="card-base reveal pub-card"><span class="pill pill-pub">{j}</span><h4>{h}</h4><p>{d}</p><div class="card-meta"><strong>{m}</strong></div></li>' for j,h,d,m in items)
        pubs += f'<div class="pub-group"><h3 class="group-title">{gh}</h3><ul class="proj-grid">{cards}</ul></div>'
    awards = "".join(f'<li class="award-card reveal"><div class="award-rank">{r}</div><h3>{h}</h3><p>{d}</p><div class="award-meta"><strong>{m}</strong></div></li>' for r,h,d,m in t["awards"])
    talks = ""
    for date,place,title,event,desc,link,s in t["talks"]:
        ttl = f'<a href="{link}" target="_blank" rel="noopener">{title}</a>' if link else title
        talks += f'<li class="talk reveal"><div class="talk-date">{date}<small>{place}</small></div><div class="talk-body"><h3>{ttl}</h3><div class="talk-event">{event}</div><p>{desc}</p>{status_pill(t,s)}</div></li>'
    talks_more = "".join(f'<li class="talk-row"><span class="talk-row-date">{d}</span><span class="talk-row-body"><span class="talk-row-title">{h}</span><span class="talk-row-event">{e}</span><span class="talk-row-note">{n}</span></span></li>' for d,h,e,n in t["talks_more"])
    vol = "".join(f'<li class="vol-card reveal"><h3>{h}</h3><div class="role">{r}</div><p>{d}</p><div class="vol-period">{per}</div></li>' for h,r,d,per in t["vol"])
    groups = [("products",products,"proj-grid"),("patents",patents,"proj-grid"),("research",research,"proj-grid"),("publications",pubs,None),("awards",awards,"awards-grid")]
    panels = ""
    for i,(k,body,cls) in enumerate(groups):
        extra = f'<p class="more-note">{t["pub_note"]}</p>' if k=="publications" else ""
        inner = body if cls is None else f'<ul class="{cls}">{body}</ul>'
        panels += f'<div class="proj-group{" visible" if i==0 else ""}" id="tab-{k}" role="tabpanel" aria-labelledby="tabbtn-{k}"{"" if i==0 else " hidden"}>{inner}{extra}</div>'
    loc, loc_alt = ("en_US","de_DE") if t["lang"]=="en" else ("de_DE","en_US")

    return f'''<!DOCTYPE html>
<html lang="{t["lang"]}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{H.escape(t["description"])}">
<meta name="author" content="Dr. Sebastian Schoenen">
<meta name="google-site-verification" content="PhaROYmn4Sk4O86H737ElXS9R5Nn_UCqVJHR-7QiGtM">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0a0a0f">
<link rel="canonical" href="{t["url"]}">
<link rel="alternate" hreflang="en" href="{SITE}">
<link rel="alternate" hreflang="de" href="{SITE}de/">
<link rel="alternate" hreflang="x-default" href="{SITE}">
<link rel="icon" href="{p}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
<link rel="sitemap" type="application/xml" href="{p}sitemap.xml">
<meta property="og:type" content="profile">
<meta property="og:site_name" content="Dr. Sebastian Schoenen">
<meta property="og:locale" content="{loc}">
<meta property="og:locale:alternate" content="{loc_alt}">
<meta property="og:url" content="{t["url"]}">
<meta property="og:title" content="{H.escape(t["og_title"])}">
<meta property="og:description" content="{H.escape(t["og_desc"])}">
<meta property="og:image" content="{SITE}og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Dr. Sebastian Schoenen">
<meta property="profile:first_name" content="Sebastian">
<meta property="profile:last_name" content="Schoenen">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{H.escape(t["og_title"])}">
<meta name="twitter:description" content="{H.escape(t["og_desc"])}">
<meta name="twitter:image" content="{SITE}og-image.png">
<link rel="preload" as="image" href="{p}{PHOTO}">
<link rel="stylesheet" href="{p}style.css">
{jsonld(t)}
</head>
<body>

<header>
<nav aria-label="Main">
  <div class="nav-inner">
    <a class="nav-logo" href="#hero">Dr. Sebastian Schoenen</a>
    <div class="nav-right">
      <ul class="nav-links">{nav_links}</ul>
      <div class="lang-switch" aria-label="Language">{lang_sw}</div>
      <button class="nav-hamburger" id="hamburger" aria-label="{t["menu_label"]}" aria-expanded="false" aria-controls="mobileMenu"><span></span><span></span><span></span></button>
    </div>
  </div>
</nav>
<div class="mobile-menu" id="mobileMenu">{mob_links}</div>
</header>

<main>
<section id="hero">
  <div class="hero-bg" aria-hidden="true"></div>
  <div class="grid-lines" aria-hidden="true"></div>
  <div class="hero-inner">
    <img class="hero-photo" src="{p}{PHOTO}" alt="{t["photo_alt"]}" width="220" height="220" fetchpriority="high">
    <div class="hero-text">
      <div class="hero-tag">{t["hero_tag"]}</div>
      <h1 class="hero-name">Dr. Sebastian <br>Schoenen</h1>
      <p class="hero-title">{t["hero_title"]}</p>
      <blockquote class="hero-quote">“{t["hero_quote"]}”</blockquote>
      <ul class="hero-badges">{badges}</ul>
      <div class="hero-btns"><a href="#projects" class="btn-pri">{t["btn_pri"]}</a><a href="#contact" class="btn-sec">{t["btn_sec"]}</a></div>
      <ul class="hero-stats">{stats}</ul>
    </div>
  </div>
</section>

<section id="about">
  <div class="container">
    <div class="sec-label">{t["about_label"]}</div>
    <h2 class="sec-title">{t["about_title"]}</h2>
    <div class="sec-line" aria-hidden="true"></div>
    <div class="about-grid">
      <div class="about-text">{about_p}</div>
      <div class="about-cards">{about_cards}</div>
    </div>
  </div>
</section>

<section id="experience">
  <div class="container">
    <div class="sec-label">{t["exp_label"]}</div>
    <h2 class="sec-title">{t["exp_title"]}</h2>
    <div class="sec-line" aria-hidden="true"></div>
    <ol class="timeline">{exp}</ol>
  </div>
</section>

<section id="skills">
  <div class="container">
    <div class="sec-label">{t["skills_label"]}</div>
    <h2 class="sec-title">{t["skills_title"]}</h2>
    <div class="sec-line" aria-hidden="true"></div>
    <div class="skills-grid">{skills}</div>
  </div>
</section>

<section id="projects">
  <div class="container">
    <div class="sec-label">{t["proj_label"]}</div>
    <h2 class="sec-title">{t["proj_title"]}</h2>
    <div class="sec-line" aria-hidden="true"></div>
    <div class="tab-bar" role="tablist">{tabs}</div>
    {panels}
  </div>
</section>

<section id="talks">
  <div class="container">
    <div class="sec-label">{t["talks_label"]}</div>
    <h2 class="sec-title">{t["talks_title"]}</h2>
    <div class="sec-line" aria-hidden="true"></div>
    <p class="sec-intro">{t["talks_intro"]}</p>
    <ol class="talk-list">{talks}</ol>
    <h3 class="group-title talks-more-title">{t["talks_more_title"]}</h3>
    <ol class="talk-rows">{talks_more}</ol>
  </div>
</section>

<section id="volunteer">
  <div class="container">
    <div class="sec-label">{t["vol_label"]}</div>
    <h2 class="sec-title">{t["vol_title"]}</h2>
    <div class="sec-line" aria-hidden="true"></div>
    <ul class="vol-grid">{vol}</ul>
  </div>
</section>

<section id="contact">
  <div class="container">
    <div class="contact-wrap">
      <div class="sec-label">{t["contact_label"]}</div>
      <h2 class="sec-title">{t["contact_title"]}</h2>
      <div class="sec-line" style="margin:0 auto 2rem" aria-hidden="true"></div>
      <p>{t["contact_p"]}</p>
      <div class="contact-links">
        <a href="{LINKEDIN}" target="_blank" rel="noopener" class="contact-link">{LI_SVG} {t["contact_li"]}</a>
        <a href="{RESEARCHGATE}" target="_blank" rel="noopener" class="contact-link alt">{t["contact_rg"]}</a>
      </div>
    </div>
  </div>
</section>
</main>

<footer>
  <div>{t["footer"].replace("© 2026", "© " + YEAR)}</div>
</footer>

<script src="{p}main.js" defer></script>
</body>
</html>
'''

out = Path(__file__).parent
(out/"index.html").write_text(render(T["en"]), encoding="utf-8")
(out/"de").mkdir(exist_ok=True)
(out/"de"/"index.html").write_text(render(T["de"]), encoding="utf-8")

def alt_links():
    return (f'    <xhtml:link rel="alternate" hreflang="en" href="{SITE}"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="de" href="{SITE}de/"/>\n'
            f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}"/>\n')
sitemap = ('<?xml version="1.0" encoding="UTF-8"?>\n'
 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
 f'  <url>\n    <loc>{SITE}</loc>\n    <lastmod>{LASTMOD}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>1.0</priority>\n{alt_links()}  </url>\n'
 f'  <url>\n    <loc>{SITE}de/</loc>\n    <lastmod>{LASTMOD}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.9</priority>\n{alt_links()}  </url>\n'
 '</urlset>\n')
(out/"sitemap.xml").write_text(sitemap, encoding="utf-8")
(out/"robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8")
print("built")
