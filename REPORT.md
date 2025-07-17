# Report for Engineering IEUK Project - Sai Raghavan Commandur

## Findings
Log analysis shows a spike in traffic, with thousands of queries coming from a small number of IP addresses. IPs like 45.133.1.1 and 45.133.1.2, for example, each sent more than 5,000 requests, utilising hundreds of different pathways and several user agents. Another, 35.185.0.156, used more than 2,000 distinct pathways and a single user agent to make 3,600 queries. These trends clearly point to automated, non-human (bot) behaviour. 

With almost 15,000 requests each, the most popular sites are /episodes/ep-42-synthesizer-history, /contact, and /about. Common browser strings that bots frequently use to imitate genuine users, such Mozilla/5.0 (Windows NT 10.0; Win64; x64) and Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7), are the top user agents.

## Recommendations 

The business should first apply rate limitation at the web server or application level in order to handle the bot traffic and minimise downtime. This limits the quantity of requests per IP address and can be configured with free tools such as Cloudflare's free tier or Nginx or Apache plugins. Next, block or challenge the suspicious IP addresses that were found during the study, including 35.185.0.156, 45.133.1.1, and 45.133.1.2. Using firewall rules, web application firewalls, or Cloudflare's bot management tools, they can be prevented or shown with CAPTCHAs.

Utilising a CDN such as Cloudflare or AWS CloudFront is also advised because these services provide basic rate limiting and bot management for free or at a minimal cost, which lowers server load and increases uptime. Small businesses can benefit from Cloudflare's free plan, which is very simple to incorporate. Lastly, ongoing log analysis should be used to continuously monitor traffic in order to spot new bot trends and modify rules as necessary. By automating reporting, the engineering team can concentrate on product development while reducing manual labour. 

## Costs & Summary

Rate limitation and basic bot protection are included in Cloudflare's free plan, while the Apache and Nginx components are open source. By taking these precautions, downtime will be decreased, resources will be safeguarded, and the engineering staff will be free to concentrate on product development rather than fighting bot traffic.
