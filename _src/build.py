import json, html, sys
import os; R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
apps = {json.loads(l)['app']: json.loads(l) for l in open(f'{R}/_src/apps.jsonl')}
SHOW = 'https://dev-sitex1322616033.wixdev-sites.org/'
demo = {
 'polls': SHOW+'poll-maker', 'quiz-maker': SHOW+'quiz-maker', 'meme-maker': SHOW+'meme-maker',
 'launch-countdown': SHOW+'launch-countdown', 'seasonal-effects': 'https://dev-sitex-1203479084.wix-dev-sites.org/',
 'pricing-tables': SHOW+'pricing-tables', 'quote-calculator': SHOW+'quote-calculator',
 'testimonials-wall': SHOW+'testimonials-wall', 'before-after': SHOW+'before-after', 'qr-codes': SHOW+'qr-code-generator',
 'faq-accordion': SHOW+'faq-accordion', 'data-tables': SHOW+'data-tables', 'property-listings': SHOW+'property-listings',
 'accessibility-widget': 'https://dev-sitex-2077286960.wixdev-sites.org/',
 'content-protection': 'https://dev-sitex1967101572.wix-development-sites.org/',
 'age-verification': 'https://dev-sitex1322616033.wixdev-sites.org/age-check',
}
groups = [
 ('Engage your visitors', ['polls', 'quiz-maker', 'meme-maker', 'launch-countdown', 'seasonal-effects']),
 ('Sell and build trust', ['pricing-tables', 'quote-calculator', 'testimonials-wall', 'before-after', 'qr-codes']),
 ('Organize information', ['faq-accordion', 'data-tables', 'property-listings', 'accessibility-widget', 'content-protection', 'age-verification']),
]
assert sorted(sum((g[1] for g in groups), [])) == sorted(apps), 'every app in exactly one group'
e = html.escape
def card(a):
    d = apps[a]
    return f'''      <article class="app">
        <img src="img/{a}.png" alt="" width="64" height="64" loading="lazy">
        <div>
          <h3>{e(d['name'])}</h3>
          <p>{e(d['teaser'])}</p>
          <div class="links"><a class="btn" href="https://www.wix.com/app-market/{d['id']}">App Market</a><a href="{demo[a]}">Live demo</a></div>
        </div>
      </article>'''
sections = '\n'.join(f'''    <section>
      <h2>{e(t)}</h2>
      <div class="grid">
{chr(10).join(card(a) for a in ids)}
      </div>
    </section>''' for t, ids in groups)
n = len(apps)
page = open(f'{R}/_src/template.html').read().replace('{{SECTIONS}}', sections).replace('{{N}}', str(n))
open(f'{R}/index.html', 'w').write(page)
print('ok', n)
