# Weekly posting job — instructions

Runs every Sunday evening. It publishes **fully automatically** (Steve's choice): posts are scheduled live, not as drafts.

## Inputs
- `brand/brand-profile.md`: voice, audience, guardrails. Follow it strictly.
- `POST-LOG.md`: what has already run. Don't repeat a topic from the last 8 weeks.
- `templates/`: `intro.html` (dark sunset ridge) and `scam.html` (light paper, dark footer band), plus `common.css`. Copy one and change the words and layout for each new post. Render with `python3 templates/render.py <file>.html <out>.png` (1080×1350). Look at every rendered PNG before using it, and fix any overflow, clipping or overlap.

## Each run
1. Work out next Tuesday and next Thursday (publish at 09:00 America/Los_Angeles).
2. Metricool brand `7770970`: call getScheduledPosts for that Mon–Sun. If a day already has a post, skip that day. If both days are covered, stop and report "nothing to do".
3. Plan 1 post per open day. Over a week: one aimed at **households** and one at **small businesses**, about 3:1 helpful tips to promotion.
   Topic ideas: Wi-Fi drops, slow PC, offline printer, email lockout, "I clicked something", camera app shows no video, backups, password managers, scam types, a website that gets calls, Google Business Profile tips, practical AI that saves an hour (job notes into an estimate draft), seasonal topics (holiday device setup, tax-season paperwork, summer heat vs electronics).
4. Write the copy:
   - **FB + IG** (one Metricool post, providers facebook + instagram): plain-English hook in the customer's words, short paragraphs, a CTA with (760) 282-4859, and 2–3 local hashtags (#Barstow #HighDesert + one topical).
   - **Google Business Profile** (separate post, provider `gmb`, gmbData type `publication`): same message, **no phone number** and no hashtags, at most 1500 characters.
5. Make the graphic in the brand palette with the logo. Keep the text short and big, and include the phone number in the footer.
6. Commit the PNG to `posts/YYYY-MM/YYYY-MM-DD-slug.png`, add rows to `POST-LOG.md`, and push to `main`.
   Image URL: `https://raw.githubusercontent.com/prinler/barstowpcpros-social/main/posts/...`. Check it returns 200 before scheduling.
7. Schedule both posts with createScheduledPost (draft false, autoPublish true) using the image URL. Write alt text that describes the graphic, set `isAiGenerated` false (designed graphics aren't AI).
8. Report a short summary: the dates, headlines, and links to the posts in Metricool.

## Hard rules (from the brand profile)
- No prices in posts (they aren't confirmed live yet) and no paid boosts/ads.
- Never invent reviews, testimonials, customers, results, statistics or credentials. Only use "20+ years in IT".
- No AI-generated images of people. No customer data, screens, footage or addresses.
- Don't name competitors. No politics. No fear-selling. Scam posts should be kind to victims.
- Don't push the remote-support link (support.barstowpcpros.com) to the public.
- Metricool free plan holds 20 scheduled posts max. If scheduling fails, don't retry in a loop: stop and report the error.
- If unsure about a claim, leave it out.
