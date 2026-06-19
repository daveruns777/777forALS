# -*- coding: utf-8 -*-
"""Page bodies for 777 for ALS."""

DONATE_WMC = "https://daves-wmc.cheddarup.com"
DONATE_BBF = "https://givestar.io/gs/run-the-world-for-als"
EMAIL = "dave@777forALS.com"
BBF_SITE = "https://www.brigancebrigade.org/"
BOOK = "https://www.amazon.com/Strength-Champion-Finding-Fortitude-Adversity/dp/0451467620/"

def img(name):
    return "assets/images/" + name

# ============================================================ HOME
def home():
    return '''
<section class="hero">
  <div class="hero__bg"><img src="''' + img("img_home_dae7e0f420.jpg") + '''" alt="Dave Lang and O.J. Brigance"></div>
  <div class="hero__inner">
    <div class="wrap">
      <span class="hero__badge"><span class="dot"></span>Dave's World Marathon Challenge</span>
      <h1 class="h-display">
        <span class="ln">7 Marathons</span>
        <span class="ln">7 Continents</span>
        <span class="ln">7 Days</span>
      </h1>
      <p class="hero__sub">Running the globe to raise $100K for people living with ALS.</p>
      <div class="hero__cta">
        <a href="donate.html" class="btn btn--primary btn--lg">Donate Now <span class="arrow">&rarr;</span></a>
        <a href="story.html" class="btn btn--ghost btn--lg">The Story</a>
      </div>
    </div>
  </div>
</section>

<section class="section--tight" style="background:var(--bg-2);border-bottom:1px solid var(--border)">
  <div class="wrap">
    <div class="stats reveal">
      <div class="stat"><div class="stat__num">183.4</div><div class="stat__label">Miles To Run</div></div>
      <div class="stat"><div class="stat__num">168</div><div class="stat__label">Hour Race Clock</div></div>
      <div class="stat"><div class="stat__num">23,600</div><div class="stat__label">Miles Of Travel</div></div>
      <div class="stat"><div class="stat__num">$100,000</div><div class="stat__label">Fundraising Goal</div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap center">
    <h2 class="section-title reveal" style="margin-bottom:14px">Countdown to the<br>2027 World Marathon Challenge</h2>
    <p class="lead mx-auto reveal" style="margin-bottom:40px">In January 2027, Dave Lang will attempt one of the most extreme endurance feats on the planet &mdash; seven marathons, across all seven continents, in just seven days.</p>
    <div class="countdown reveal" id="countdown" data-target="2027-01-30T00:00:00"></div>
  </div>
</section>

<section class="section" style="background:var(--bg-2);border-top:1px solid var(--border)">
  <div class="wrap">
    <div class="center" style="margin-bottom:46px">
      <span class="eyebrow reveal">Watch</span>
      <h2 class="section-title reveal">The Announcement</h2>
    </div>
    <div class="video-single reveal">
      <div class="video-embed video-lite" data-src="https://drive.google.com/file/d/1oRH_076-twOmOjm2XPMDZgHEou08HlJE/preview" data-title="WMC Announcement" role="button" tabindex="0" aria-label="Play the announcement video">
        <img src="''' + img("video_thumb_announcement.jpg") + '''" alt="Watch the World Marathon Challenge announcement" style="object-fit:contain;background:#000">
        <button class="video-lite__play" aria-label="Play video"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></button>
      </div>
    </div>
  </div>
</section>

<section class="cta-band section--tight">
  <div class="amber-rule" style="position:absolute;top:0;left:0;right:0"></div>
  <div class="wrap reveal">
    <h2 class="h-display">Every Mile Matters</h2>
    <p class="lead mx-auto" style="margin-bottom:28px">Your support helps Dave reach the start line &mdash; and helps the Brigance Brigade Foundation change lives for people living with ALS.</p>
    <a href="donate.html" class="btn btn--primary btn--lg">Support Dave's Run <span class="arrow">&rarr;</span></a>
  </div>
</section>
'''

# ============================================================ MISSION
LEGS = [
  ("01","ANTARCTICA","Ultima Base, Antarctica","Jan. 30, 2027","78.4&deg;S 90.0&deg;W","The journey begins in the most extreme place on Earth &mdash; sub-zero temperatures and complete isolation.","cont_antarctica.jpg"),
  ("02","AFRICA","Cape Town, South Africa","Jan. 31, 2027","33.9&deg;S 18.4&deg;E","From ice to the cradle of humanity, with Table Mountain as witness to mile two.","cont_africa.jpg"),
  ("03","AUSTRALIA","Perth, Australia","Feb. 1, 2027","31.9&deg;S 115.8&deg;E","The red continent stretches endlessly &mdash; each mile a meditation on endurance.","cont_australia.jpg"),
  ("04","ASIA","Dubai, U.A.E.","Feb. 2, 2027","25.2&deg;N 55.3&deg;E","Halfway around the world, running through a skyline rising from the desert.","cont_asia.jpg"),
  ("05","EUROPE","Madrid, Spain","Feb. 3, 2027","40.4&deg;N 3.7&deg;W","Through the heart of Spain, legs heavy, spirit driven by purpose.","cont_europe.jpg"),
  ("06","SOUTH AMERICA","Fortaleza, Brazil","Feb. 4, 2027","3.7&deg;S 38.5&deg;W","Along the Brazilian coast, the finish line of the world tour drawing near.","cont_southamerica.jpg"),
  ("07","NORTH AMERICA","Miami, Florida, USA","Feb. 5, 2027","25.8&deg;N 80.2&deg;W","The final 26.2 miles, home soil, completing 183.4 miles around the globe.","cont_northamerica.jpg"),
]

def mission():
    legs = ""
    for num, cont, loc, date, coords, desc, im in LEGS:
        legs += '''
      <article class="leg-card reveal">
        <div class="leg-card__img"><img src="''' + img(im) + '''" alt="''' + cont + '''"></div>
        <div class="leg-card__num">''' + num + '''</div>
        <div class="leg-card__coords">''' + coords + '''</div>
        <div class="leg-card__body">
          <div class="leg-card__continent">''' + cont + '''</div>
          <div class="leg-card__meta">''' + loc + ''' &middot; ''' + date + '''</div>
          <p class="leg-card__desc">''' + desc + '''</p>
        </div>
      </article>'''
    impact = [
      ("&#127968;","In-Home Healthcare","BBF is one of the few organizations that funds the vital need of in-home care for PALS. Quality in-home healthcare supports the physical and emotional well-being of PALS and their Caregivers (CALS)."),
      ("&#9855;","Equipment","BBF supports grant requests for equipment purchases or rental fees not covered by insurance &mdash; aiding mobility, communication and breathing &mdash; including installation, supplies and maintenance plans."),
      ("&#127962;","Home Accessibility","To support independence and safety, BBF considers funding for home modifications such as bathroom accessibility, door widening, ramp installation, sidewalk repair and compact generators."),
    ]
    cards = ""
    for ic, h, p in impact:
        cards += '<div class="card reveal"><div class="card__icon">' + ic + '</div><h3>' + h + '</h3><p>' + p + '</p></div>'

    return '''
<section class="page-hero">
  <div class="page-hero__bg"><img src="''' + img("cont_antarctica.jpg") + '''" alt="Mission"></div>
  <div class="page-hero__inner"><div class="wrap">
    <span class="eyebrow">The Mission</span>
    <h1 class="h-display">Run The World<br>Marathon Challenge</h1>
    <p class="lead">Held annually in January, the World Marathon Challenge is the most unique running adventure on the planet. In 168 hours, participants run 183.4 miles while traveling 23,600 miles around the globe.</p>
  </div></div>
</section>

<section class="section">
  <div class="wrap">
    <div class="center" style="margin-bottom:44px">
      <span class="eyebrow reveal">2027 Schedule</span>
      <h2 class="section-title reveal">Seven Days. Seven Continents.</h2>
    </div>
    <div class="schedule-grid">''' + legs + '''</div>
    <div class="center reveal" style="margin-top:46px">
      <p class="lead mx-auto"><strong>Only 292 people</strong> &mdash; and just <strong>119 Americans</strong> &mdash; have ever completed the World Marathon Challenge.</p>
    </div>
  </div>
</section>

<section class="section--tight" style="background:var(--bg-2);border-top:1px solid var(--border);border-bottom:1px solid var(--border)">
  <div class="wrap media-strip reveal">
    <span class="eyebrow eyebrow--muted">As Featured On</span>
    <div class="media-strip__imgs">
      <img src="''' + img("media-strip-1.jpg") + '''" alt="Featured media outlets">
      <img src="''' + img("media-strip-2.jpg") + '''" alt="Featured media outlets">
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="feature" style="margin-bottom:60px">
      <div class="feature__media reveal"><img src="''' + img("img_home_e08b38940c.jpg") + '''" alt="Brigance Brigade Foundation" style="object-fit:contain;background:#fff;padding:40px"></div>
      <div class="reveal">
        <span class="eyebrow">The Goal</span>
        <h2 class="section-title" style="margin-bottom:20px">Raise $100K+ for PALS</h2>
        <div class="text-block">
          <p>While 2014's viral Ice Bucket Challenge raised awareness and funds for ALS (Lou Gehrig's Disease), it remains an "orphan disease" &mdash; a rare disease with limited and high-cost treatment options. As such, ALS does not receive the levels of attention or funding as other more common disorders.</p>
          <p>Dave is running the World Marathon Challenge to raise proceeds for the <strong>Brigance Brigade Foundation</strong> so that it may provide increased access to equipment, support services and resources that will drastically improve the quality of life for more people living with ALS (PALS) and their families.</p>
        </div>
        <a href="''' + DONATE_BBF + '''" target="_blank" rel="noopener" class="btn btn--primary" style="margin-top:24px">Donate to the Brigance Brigade <span class="arrow">&rarr;</span></a>
      </div>
    </div>
    <div class="center" style="margin:20px 0 36px"><span class="eyebrow reveal">Your support will provide</span></div>
    <div class="card-grid">''' + cards + '''</div>
  </div>
</section>

<section class="cta-band section--tight">
  <div class="amber-rule" style="position:absolute;top:0;left:0;right:0"></div>
  <div class="wrap reveal">
    <h2 class="h-display">Fuel The Mission</h2>
    <a href="donate.html" class="btn btn--primary btn--lg" style="margin-top:12px">Donate to Support Dave's Run <span class="arrow">&rarr;</span></a>
  </div>
</section>
'''

# ============================================================ MOTIVATION
OJ_VIDS = ["jCGtQLgX4LY","xiMHddeorEI","IuNL_hmhmuQ","b7kX2OW_mFo","VyPlnz0qztM","kU5I9K8RO9g"]

def motivation():
    vids = ""
    for v in OJ_VIDS:
        vids += '<div class="video-embed"><iframe src="https://www.youtube.com/embed/' + v + '" allowfullscreen title="O.J. Brigance story"></iframe></div>'
    return '''
<section class="page-hero">
  <div class="page-hero__bg"><img src="''' + img("img_motivation_78cf78f4cb.jpg") + '''" alt="O.J. Brigance"></div>
  <div class="page-hero__inner"><div class="wrap">
    <span class="eyebrow">The Story</span>
    <h1 class="h-display">Why I Run</h1>
    <p class="lead">Running seven marathons across the globe in a week seems crazy, right?! It also requires an immense commitment to training. So why am I doing this?</p>
  </div></div>
</section>

<section class="section">
  <div class="wrap">
    <div class="feature feature--reverse" style="margin-bottom:30px">
      <div class="feature__media reveal"><img src="''' + img("img_motivation_3c3c835c98.jpg") + '''" alt="O.J. Brigance, Baltimore Ravens"><span class="feature__caption">O.J. Brigance &middot; #57</span></div>
      <div class="reveal">
        <span class="eyebrow">The Inspiration</span>
        <h2 class="section-title" style="margin-bottom:20px">O.J.'s Story</h2>
        <div class="text-block">
          <p>O.J. Brigance is the utmost example of the phrase "All things are possible." His remarkable story started on the football field. After going undrafted in 1991, he contacted every NFL team seeking a tryout before beginning his pro career in the Canadian Football League, where he became a CFL All-Star and Grey Cup Champion. In 1996 he signed with the Miami Dolphins, where he was voted team captain and named the Ed Block Courage Award recipient. In 2000, he helped the Baltimore Ravens win Super Bowl XXXV &mdash; making the game's first tackle.</p>
          <p>Following his seven-year NFL playing career, Brigance became the Ravens' director of player development. In May 2007, at the age of 37, he was diagnosed with amyotrophic lateral sclerosis (Lou Gehrig's disease), a neurodegenerative disease that slowly takes away a person's ability to walk, talk, eat and eventually breathe. Mental capacity, however, remains intact. There is no cure for ALS, and the average life expectancy is 2&ndash;5 years after diagnosis. (Just 10% of patients live 10+ years.)</p>
        </div>
      </div>
    </div>
    <div class="feature" style="margin-bottom:10px">
      <div class="feature__media reveal"><img src="''' + img("img_motivation_8067b2b37d.jpg") + '''" alt="O.J. Brigance and his wife Chanda"></div>
      <div class="reveal">
        <div class="text-block">
          <p>Shortly after his diagnosis, Brigance and his wife, Chanda, created the <strong>Brigance Brigade Foundation</strong> to equip, encourage, and empower people living with ALS (PALS). Across nearly two decades, the BBF has helped improve the quality of life for hundreds of PALS and their families, and provided access to needed equipment and support services.</p>
          <p>As he enters his 20th year battling ALS, O.J. continues his transcendent work. He still comes into work at the Ravens facility, offering counsel to players, coaches and staff, while remaining actively involved in the philanthropic mission of the Brigance Brigade Foundation.</p>
        </div>
        <blockquote class="quote">
          <p>"Extraordinary accomplishments are only achieved when we are able to overcome extraordinary challenges."</p>
          <cite>&mdash; O.J. Brigance</cite>
        </blockquote>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--bg-2);border-top:1px solid var(--border)">
  <div class="wrap">
    <div class="feature feature--reverse">
      <div class="feature__media reveal"><img src="''' + img("img_motivation_fda88c3cd7.jpg") + '''" alt="Dave Lang and O.J. Brigance"></div>
      <div class="reveal">
        <span class="eyebrow">From The Runner</span>
        <h2 class="section-title" style="margin-bottom:20px">Dave's Motivation</h2>
        <div class="text-block">
          <p>For nearly 20 years, I've witnessed a strength and resiliency that few can ever imagine. I met O.J. Brigance during my first week working for the Ravens &mdash; less than a month after he had been diagnosed with ALS. Besides his quick wit and sense of humor, the thing that stood out most to me about O.J. was his smile, which was the biggest in the building, and his genuine care for other people.</p>
          <p>Gradually, the effects of ALS began to show. Just a few years earlier, O.J. was one of the top athletes in the world. But soon the disease inhibited his ability to walk, confining him to a wheelchair. Then I watched as ALS deprived O.J. of his ability to speak. Eventually, the disease suppressed his breathing, requiring a breathing tube and ventilator to survive.</p>
          <p>Despite these challenging circumstances, O.J.'s determination is unwavering. Coach John Harbaugh often referred to O.J. as the strongest man in the building and the spiritual foundation of the Ravens. Before I ran the Baltimore Marathon in 2012, he shared meaningful words of encouragement &mdash; a message that required significant effort to communicate by typing words with his eyes on a screen, and a message I heard in my head when the race got tough.</p>
          <p>When I first heard about the World Marathon Challenge in 2018, I questioned if it was humanly possible. In perspective though, running 183 miles around the globe in a week seems easier than what someone with ALS goes through daily just to live their life. I recognize that I've been blessed with a gift &mdash; not of endurance, but simply with two healthy legs and the ability to run and walk &mdash; and I feel called to use that gift for a greater purpose.</p>
          <p>To honor the inspiration O.J. has instilled in me, and to celebrate his incredible 20th year living with ALS, I'm taking on the World Marathon Challenge to support him and the Brigance Brigade Foundation by raising $100,000 to provide necessary assistance to ALS patients in need. I hope you'll support O.J. and me on this journey!</p>
        </div>
        <div class="hero__cta" style="margin-top:26px">
          <a href="''' + DONATE_WMC + '''" target="_blank" rel="noopener" class="btn btn--primary">Donate to Support Dave's Run</a>
          <a href="''' + DONATE_BBF + '''" target="_blank" rel="noopener" class="btn btn--ghost">Donate to the Brigance Brigade</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="center" style="margin-bottom:42px">
      <span class="eyebrow reveal">Watch</span>
      <h2 class="section-title reveal">More About O.J.'s Story</h2>
    </div>
    <div class="video-grid video-grid--three reveal">''' + vids + '''</div>
  </div>
</section>
'''

# ============================================================ ABOUT
def about():
    return '''
<section class="page-hero">
  <div class="page-hero__bg"><img src="''' + img("img_about_76a3542e6b.jpg") + '''" alt="About Dave Lang"></div>
  <div class="page-hero__inner"><div class="wrap">
    <span class="eyebrow">About</span>
    <h1 class="h-display">The People<br>Behind The Run</h1>
  </div></div>
</section>

<section class="section">
  <div class="wrap">
    <div class="feature" style="margin-bottom:70px">
      <div class="feature__media reveal"><img src="''' + img("img_about_59d3705465.jpg") + '''" alt="Dave Lang with his daughters"></div>
      <div class="reveal">
        <span class="eyebrow">The Runner</span>
        <h2 class="section-title" style="margin-bottom:20px">About Dave Lang</h2>
        <div class="text-block">
          <p>Dave Lang is a husband and girl dad (of three). He grew up in Dumont, NJ and, soon after graduating from Loyola University, moved back to Maryland to begin an internship with the Baltimore Ravens. During his first season with the Ravens in 2007, Dave befriended then-Director of Player Development O.J. Brigance, who had been diagnosed with ALS just one month earlier.</p>
          <p>Now the Ravens' Sr. Director of Digital Strategy &amp; Innovation, Dave is proudly in his 20th season with the team. He has also served on the board for the Ravens Foundation since 2019.</p>
          <p>Much more a "regular" guy than a world-class endurance athlete, Dave has completed all six races in the Baltimore Running Festival, including his first marathon in 2012 and a 4th-place overall finish in the 2025 Baltimoron-a-Thon. Dave also ran the 2022 Marine Corps Marathon 50K to raise $3,500+ for a friend battling breast cancer. In 2026, he took 1st place in the Brigance Brigade 5.7K. He and his family live in Eldersburg, MD, where he spends lots of time driving his daughters to activities when he isn't running.</p>
        </div>
      </div>
    </div>

    <div class="feature feature--reverse">
      <div class="feature__media reveal"><img src="''' + img("img_about_092109feb3.jpg") + '''" alt="O.J. and Chanda Brigance"></div>
      <div class="reveal">
        <span class="eyebrow">The Foundation</span>
        <h2 class="section-title" style="margin-bottom:20px">About the Brigance Brigade</h2>
        <div class="text-block">
          <p>Following his diagnosis of amyotrophic lateral sclerosis in 2007, seven-year NFL veteran and Super Bowl XXXV champion O.J. Brigance and his wife, Chanda, created the Brigance Brigade Foundation to equip, encourage, and empower people living with ALS. The foundation's mission is to improve the quality of life for people living with ALS (PALS) and their families by providing access to support services, needed equipment and resource guidance.</p>
          <p>Throughout 20 years, the BBF has helped hundreds of families across the mid-Atlantic region and beyond, increasing access to caregiving services, equipment, and in-home accessibility for PALS. In addition to providing financial help to offset some of the staggering costs associated with ALS, the BBF is also committed to programming that supports the mental, physical, and emotional health of ALS caregivers (CALS).</p>
        </div>
        <a href="''' + BBF_SITE + '''" target="_blank" rel="noopener" class="btn btn--primary" style="margin-top:24px">Learn More <span class="arrow">&rarr;</span></a>
      </div>
    </div>
  </div>
</section>

<section class="cta-band section--tight">
  <div class="amber-rule" style="position:absolute;top:0;left:0;right:0"></div>
  <div class="wrap reveal">
    <h2 class="h-display">Join The Journey</h2>
    <a href="donate.html" class="btn btn--primary btn--lg" style="margin-top:12px">Donate Now <span class="arrow">&rarr;</span></a>
  </div>
</section>
'''

# ============================================================ SPONSORS
def slogo(img_name, alt, url, text=False):
    inner = ('<span class="text-logo">%s</span>' % alt) if text else ('<img src="%s" alt="%s">' % (img(img_name), alt))
    tgt = '' if url == '#' else ' target="_blank" rel="noopener"'
    return '<a class="sponsor-logo" href="%s"%s title="%s">%s</a>' % (url, tgt, alt, inner)

PKGS = [
  ("&#127758;","World Sponsorship","$50,000","pkg--feature",[
    "Logo on Dave's gear during all 7 marathons",
    "Prominent presenting sponsorship logo &amp; wording on website &amp; all promotional materials",
    "Company mention / logo / call out in pre- and post-race media interviews",
    "Finish line photo for each marathon on social media; company @mention",
    "Post-race photo of Dave holding a sign thanking your company at each finish line",
    "Post-race social media video shoutout following each continent's marathon",
    "(3) social media shoutouts leading up to WMC; includes company @mention",
    "Post-WMC meet &amp; greet / company visit / private Zoom / blog or case study / group run with Dave",
    "Logo on Sponsors page of website",
    'Copy of <a href="%s" target="_blank" rel="noopener" style="color:var(--accent)">Strength of a Champion</a> by O.J. Brigance' % BOOK,
    "Logo featured on World Marathon Challenge and Runbuk Instagram, Facebook and/or YouTube accounts",
  ]),
  ("&#128506;","Continent Sponsorship","$10,000","",[
    "Logo on Dave's gear during marathon on one continent",
    "Post-WMC meet &amp; greet / company visit / private Zoom / blog / group run with Dave",
    "Finish line photo for continent marathon on social media; company @mention",
    "Post-marathon photo of Dave holding a sign thanking your company",
    "Pre/post-race social media video shoutout for the continent's marathon",
    "(2) social media shoutouts leading up to WMC; includes company @mention",
  ]),
  ("&#127987;","Country Sponsorship","$5,000","",[
    "Finish line photo for country marathon on social media; company @mention",
    "Social media video shoutout while in country during WMC; company @mention",
    "Social media shoutout leading up to WMC; includes company @mention",
  ]),
  ("&#128205;","City Sponsorship","$2,500","",[
    "Social media video shoutout while in city during WMC; company @mention",
    "Social media video shoutout leading up to WMC; company @mention",
  ]),
  ("&#128153;","Community Sponsorship","$1,000","",[
    "Recognition as a Community supporter of Dave's Run the World for ALS",
    "Social media shoutout amplified by World Marathon Challenge &amp; Brigance Brigade accounts",
  ]),
]

def sponsors():
    lead = "".join(slogo(*s) for s in [
        ("yinzcam.png", "YinzCam", "https://www.yinzcam.com/", False),
        ("ravens.png", "Baltimore Ravens", "https://www.baltimoreravens.com", False),
        ("image-engineering.png", "Image Engineering", "https://www.imageengineering.com/", False),
        ("architectural-window.png", "Architectural Window", "https://www.architecturalwindow.com/", False),
    ])
    supporting = "".join(slogo(*s) for s in [
        ("balti-virtual.png", "Balti Virtual", "https://www.baltivirtual.com/", False),
        ("momento.png", "Momento", "https://www.mymomento.com/", False),
        ("medstar.png", "MedStar Health", "https://www.medstarhealth.org/", False),
        ("freedom-digital.png", "Freedom Digital Media", "https://www.freedomdigital.net/", False),
    ])
    pk = ""
    for ic, name, price, cls, items in PKGS:
        lis = "".join("<li>" + i + "</li>" for i in items)
        tag = '<div class="pkg__tag">Presenting Tier</div>' if cls else '<div class="pkg__tag">Sponsorship</div>'
        pk += '''<div class="pkg ''' + cls + ''' reveal">
          ''' + tag + '''
          <div class="pkg__name">''' + ic + ''' ''' + name + '''</div>
          <div class="pkg__price">''' + price + '''<small>Includes:</small></div>
          <ul>''' + lis + '''</ul>
        </div>'''
    return '''
<section class="page-hero">
  <div class="page-hero__bg"><img src="''' + img("img_sponsors_d1de96009a.jpg") + '''" alt="Corporate Sponsors"></div>
  <div class="page-hero__inner"><div class="wrap">
    <span class="eyebrow">Partners</span>
    <h1 class="h-display">Corporate Sponsors</h1>
    <p class="lead">Thank you to my sponsors whose generosity and belief in me will help me reach the World Marathon Challenge starting line.</p>
  </div></div>
</section>

<section class="section">
  <div class="wrap">
    <div class="sponsor-tier">
      <div class="sponsor-tier__title">Leading Sponsors</div>
      <div class="sponsor-tier__rule"></div>
      <div class="sponsor-logos sponsor-logos--lead reveal">''' + lead + '''</div>
    </div>
    <div class="sponsor-tier">
      <div class="sponsor-tier__title">Supporting Sponsors</div>
      <div class="sponsor-tier__rule"></div>
      <div class="sponsor-logos reveal">''' + supporting + '''</div>
    </div>
  </div>
</section>

<section class="section--tight" style="background:var(--bg-2);border-top:1px solid var(--border);border-bottom:1px solid var(--border)">
  <div class="wrap" style="max-width:840px">
    <div class="text-block center reveal">
      <p>Participation in the World Marathon Challenge &mdash; which will provide an extraordinary opportunity for Dave to raise funds for those battling ALS &mdash; is a costly endeavor. It also offers a unique opportunity for your brand to gain global media exposure while aligning itself with an inspiring story of perseverance and a meaningful purpose.</p>
      <p>Dave is still actively seeking corporate partners to help fund the remaining part of his race entry fee that will enable him to stimulate worldwide support for the life-changing mission of the Brigance Brigade Foundation. All additional sponsorship proceeds above the race entry fee will go directly to the Brigance Brigade Foundation.</p>
      <p style="font-size:.92rem;color:var(--muted-2)">(Individuals looking to support Dave's WMC race entry can <a href="''' + DONATE_WMC + '''" target="_blank" rel="noopener" style="color:var(--accent)">donate here</a>.)</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="center" style="margin-bottom:44px">
      <span class="eyebrow reveal">Get Involved</span>
      <h2 class="section-title reveal">Sponsor Packages</h2>
      <p class="lead mx-auto reveal">View sponsorship opportunities below and contact <a href="mailto:''' + EMAIL + '''" style="color:var(--accent)">''' + EMAIL + '''</a>.</p>
    </div>
    <div class="pkg-grid">''' + pk + '''</div>
    <p class="pkg__note center mx-auto reveal" style="max-width:760px;margin-top:26px">*The World Marathon Challenge highlights and amplifies fundraising efforts by its participants across its own Instagram, Facebook and YouTube accounts. Social posts are also amplified by the Brigance Brigade Foundation's social accounts.</p>
  </div>
</section>

<section class="cta-band section--tight">
  <div class="amber-rule" style="position:absolute;top:0;left:0;right:0"></div>
  <div class="wrap reveal">
    <h2 class="h-display">Become A Sponsor</h2>
    <p class="lead mx-auto" style="margin-bottom:26px">Align your brand with an inspiring story of perseverance and purpose.</p>
    <a href="mailto:''' + EMAIL + '''" class="btn btn--primary btn--lg">Contact Dave <span class="arrow">&rarr;</span></a>
  </div>
</section>
'''

# ============================================================ DONATE
GIFTS = [
  ("$777","in honor of the 7 marathons on 7 continents in 7 days that Dave will run"),
  ("$570","in honor of O.J. Brigance's jersey #57 (+ an extra zero &#128521;)"),
  ("$465","in honor of the number of people in the U.S. diagnosed with ALS each month"),
  ("$343","in honor of Dave's 7 &times; 7 &times; 7 World Marathon Challenge"),
  ("$295.37","in honor of the 295.365 kilometers Dave will run throughout the seven marathons"),
  ("$183.40","in honor of the 183.4 total miles Dave will run throughout the seven marathons"),
  ("$57","in honor of O.J. Brigance's jersey #57"),
  ("$26.20","in honor of the 26.2 miles run in a marathon"),
]
IMPACT = [
  ("$5,000","covers the cost of one BBF PALS Grant to a family in need"),
  ("$2,500","helps a family bring in an outside care agency 3 days a week for a full month"),
  ("$1,000","helps pay out-of-pocket costs for an eye gaze machine, allowing a PALS to communicate with loved ones"),
  ("$500","covers an additional battery for a breathing machine not covered by standard insurance"),
  ("$250","covers a transfer bench or shower chair to ensure safety and security at home"),
  ("$150","pays for a day of care so a PALS primary caregiver can go to work"),
  ("$50","pays for in-home care so a family caregiver can attend their own doctor appointment"),
  ("$25","covers 1 hour of medical care &amp; consultation for a family touched by ALS"),
  ("$10","covers the cost of a gait belt so someone with ALS can be transferred more safely"),
]

def donate():
    gifts = "".join('<div class="amount reveal"><div class="amount__val">' + v + '</div><div class="amount__txt">' + t + '</div></div>' for v, t in GIFTS)
    impact = "".join('<div class="amount reveal"><div class="amount__val">' + v + '</div><div class="amount__txt">' + t + '</div></div>' for v, t in IMPACT)
    return '''
<section class="page-hero">
  <div class="page-hero__bg"><img src="''' + img("img_donate_af97a5c90e.jpg") + '''" alt="Donate"></div>
  <div class="page-hero__inner"><div class="wrap">
    <span class="eyebrow">Make An Impact</span>
    <h1 class="h-display">Donate</h1>
    <p class="lead">There are two ways you can financially support Dave's Run the World for ALS mission.</p>
  </div></div>
</section>

<section class="section">
  <div class="wrap">
    <div class="give-grid">
      <div class="give-card reveal">
        <div class="give-card__num">01</div>
        <h3>Help Dave Reach the Start Line</h3>
        <p>Assist with the remaining part of Dave's World Marathon Challenge entry fee &mdash; which covers intercontinental flights, race aid, medical support and some meals.</p>
        <a href="''' + DONATE_WMC + '''" target="_blank" rel="noopener" class="btn btn--primary btn--block">Donate to Dave's World Marathon Challenge</a>
      </div>
      <div class="give-card reveal">
        <div class="give-card__num">02</div>
        <h3>Fuel the $100K+ Goal</h3>
        <p>Help Dave surpass his ambitious $100K+ fundraising goal. 100% of your tax-deductible donation will go towards the Brigance Brigade Foundation to provide life-changing assistance to those battling ALS and to their families.</p>
        <a href="''' + DONATE_BBF + '''" target="_blank" rel="noopener" class="btn btn--primary btn--block">Donate to Run the World for ALS</a>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--bg-2);border-top:1px solid var(--border)">
  <div class="wrap">
    <div class="center" style="margin-bottom:38px">
      <span class="eyebrow reveal">Meaningful Gift Amounts</span>
      <h2 class="section-title reveal">Gifts Tied to Dave's Run</h2>
      <p class="lead mx-auto reveal">Consider these meaningful gift amounts tied to Dave's run and the Brigance Brigade.</p>
    </div>
    <div class="amount-grid">''' + gifts + '''</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="center" style="margin-bottom:38px">
      <span class="eyebrow reveal">The Impact</span>
      <h2 class="section-title reveal">The Impact of Your Gift</h2>
      <p class="lead mx-auto reveal">Every dollar to the Brigance Brigade Foundation provides real, tangible help to families touched by ALS.</p>
    </div>
    <div class="amount-grid">''' + impact + '''</div>

    <div class="feature" style="margin-top:64px">
      <div class="feature__media reveal"><img src="''' + img("img_donate_04725db375.jpg") + '''" alt="O.J. Brigance using an eye gaze machine"></div>
      <div class="reveal">
        <span class="eyebrow">Why It Matters</span>
        <h3 class="section-title" style="font-size:clamp(1.6rem,3vw,2.4rem);margin-bottom:18px">The Gift of Communication</h3>
        <p>O.J. "speaks" to Dave using his eye gaze machine. Once ALS robs someone of their ability to talk, this device allows them to communicate with family members and loved ones. With your support of this challenge, eye gaze machines may be provided to 100+ PALS and their families.</p>
        <a href="''' + DONATE_WMC + '''" target="_blank" rel="noopener" class="btn btn--primary" style="margin-top:24px">Donate Now <span class="arrow">&rarr;</span></a>
      </div>
    </div>
  </div>
</section>

<section class="cta-band section--tight">
  <div class="amber-rule" style="position:absolute;top:0;left:0;right:0"></div>
  <div class="wrap reveal">
    <h2 class="h-display">&#128257; Share The Mission</h2>
    <p class="lead mx-auto">To ignite further support, please consider sharing this page with your personal networks to inspire others to follow your lead!</p>
  </div>
</section>
'''

# ============================================================ BUILD
def build(page):
    page("index.html", "Run the World for ALS | 777 for ALS", "7 Marathons. 7 Continents. 7 Days. Dave Lang's World Marathon Challenge to benefit people living with ALS.", home(), "index.html")
    page("mission.html", "Mission | Run the World for ALS", "The World Marathon Challenge: 7 marathons across 7 continents in 7 days to raise $100K+ for the Brigance Brigade Foundation.", mission(), "mission.html")
    page("motivation.html", "The Story | Run the World for ALS", "O.J. Brigance's story and Dave Lang's motivation for taking on the World Marathon Challenge.", motivation(), "motivation.html")
    page("about.html", "About | Run the World for ALS", "About Dave Lang and the Brigance Brigade Foundation.", about(), "about.html")
    page("sponsors.html", "Sponsors | Run the World for ALS", "Corporate sponsorship opportunities for Dave Lang's World Marathon Challenge.", sponsors(), "sponsors.html")
    page("donate.html", "Donate | Run the World for ALS", "Two ways to support Dave's Run the World for ALS mission and the Brigance Brigade Foundation.", donate(), "donate.html")
