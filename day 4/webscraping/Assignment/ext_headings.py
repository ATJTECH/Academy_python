#1. Scrape the website: https://news.ycombinator.com/ . Extract all the headings and store it in a list.
#Extract the score and the link of the headings in its individual lists

from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Your User Agent',
    'Custom-Header': 'Custom Value'}

response=requests.get("https://news.ycombinator.com/",headers)
contents=response.text
soup=BeautifulSoup(contents,"html.parser")

headings= soup.find_all(class_='athing')
headings_text = [heading.text for heading in headings]
print(headings_text)
'''for heading in headings:
    headings_text = [heading.text]'''



score= soup.find_all(class_='score')
score_text = [s.text for s in score]
print(score_text)

site= soup.find_all(class_='sitebit comhead')
site_text = [x.text for x in site]
print(site_text)


# ['\n1. "Hacker News" for retro computing and gaming (jgc.org)', '\n2. Cloudflare Sippy: Incrementally Migrate Data from AWS S3 to Reduce Egress Fees (infoq.com)', '\n3. BeagleV-Ahead open-source RISC-V single board computer (beagleboard.org)', '\n4. Breakelse: When Compiler Developers Get Bored (neat-lang.github.io)', '\n5. Sessionic: A cross-browser extension to save, manage, restore tabs and sessions (github.com/navorite)', '\n6. Cursor – The AI-First Code Editor (cursor.sh)', '\n7. The British Mosquito once carried Niels Bohr in its bomb bay (thedrive.com)', '\n8. Show HN: mystery-o-matic offers a daily random murder mystery (mystery-o-matic.com)', '\n9. The Welsh Punk Scene of the 1980s (huckmag.com)', '\n10. Show HN: 3D Binpacking Algorithm Visualized (skusavvy.com)', '\n11. Think in Analog, Capture in Digital (huwfulcher.com)', '\n12. Transactions and Concurrency in PostgreSQL (doadm-notes.blogspot.com)', '\n13.  Supabase (YC S20) Is Hiring a Technical Docs Lead (Fully Remote) (greenhouse.io)', "\n14. Steve's Explanation of the Viterbi Algorithm (2003) (toronto.edu)", '\n15. Linux on an 8bit Microcontroller (dmitry.gr)', "\n16. Google has sent internet into 'spiral of decline', claims DeepMind co-founder (telegraph.co.uk)", '\n17. Ten Years Writing Book Reviews (dannyreviews.com)', '\n18. Recursive Recipes (schollz.com)', "\n19. Implementing a GPU's programming model on a CPU (litherum.blogspot.com)", '\n20. The Apple Macintosh Primer (1984) [pdf] (vintageapple.org)', '\n21. History of the Mackintosh: 200 years of the classic raincoat (theguardian.com)', '\n22. FBI warns against using public USB charging ports (go.com)', '\n23. Show HN: Mini-Woo, luanch Telegram mini app for WooCommerce in seconds (github.com/mini-woo)', "\n24. On the Experience of Being Poor-Ish, for People Who Aren't (residentcontrarian.com)", '\n25. QNX Demo Disk screen shots (toastytech.com)', '\n26. Jupe: Off-grid shelters that pop up anywhere on Earth (jupe.com)', '\n27. Websites of 2000 [video] (bbc.co.uk)', '\n28. The Garden of the Five Senses (worldsensorium.com)', '\n29. ChatGPT’s system prompts (github.com/spdustin)', '\n30. Show HN: Firefox add-on to open YouTube videos in alternative front ends (github.com/d3vr)']