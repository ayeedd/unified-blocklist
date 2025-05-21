import requests
import os

"""
update_blocklist.py

This script downloads multiple domain blocklists from predefined URLs,
merges them into a single unified blocklist, removes duplicates and comments,
and saves the combined list to a file for use in ad-blocking tools like AdGuard.

Usage:
    python update_blocklist.py

Output:
    data/unified_blocklist.txt - unified domain blocklist file

Requirements:
    - Python 3.x
    - requests library (install via pip if missing)

Author: Your Name
Date: 2025-05-21
"""

urls = [
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/doh-vpn-proxy-bypass.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_2.txt",
    "https://justdomains.github.io/blocklists/lists/adguarddns-justdomains.txt",
    "https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt",
    "https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt",
    "https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt",
    "https://justdomains.github.io/blocklists/lists/easylist-justdomains.txt",
    "https://justdomains.github.io/blocklists/lists/easyprivacy-justdomains.txt",
    "https://adaway.org/hosts.txt",
    "https://v.firebog.net/hosts/AdguardDNS.txt",
    "https://v.firebog.net/hosts/Admiral.txt",
    "https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt",
    "https://v.firebog.net/hosts/Easylist.txt",
    "https://v.firebog.net/hosts/Easyprivacy.txt",
    "https://raw.githubusercontent.com/nextdns/cname-cloaking-blocklist/master/domains",
    "https://phishing.army/download/phishing_army_blocklist.txt",
    "https://raw.githubusercontent.com/klabacita/pmoreno-list/main/proxies.txt",
    "https://perflyst.github.io/PiHoleBlocklist/SmartTV.txt",
    "https://blocklistproject.github.io/Lists/tiktok.txt",
    "https://raw.githubusercontent.com/WindowsLies/BlockWindows/master/hostslist",
    "https://raw.githubusercontent.com/bambenek/block-doh/master/doh-hosts.txt",
    "https://raw.githubusercontent.com/dibdot/DoH-IP-blocklists/master/doh-domains_abandoned.txt",
    "https://raw.githubusercontent.com/dibdot/DoH-IP-blocklists/master/doh-domains.txt",
    "https://raw.githubusercontent.com/oneoffdallas/dohservers/master/list.txt",
    "https://raw.githubusercontent.com/Sekhan/TheGreatWall/master/TheGreatWall.txt",
    "https://big.oisd.nl/",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/tif.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/ultimate.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/fake.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/popupads.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.amazon.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.apple.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.winoffice.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/domains/native.lgwebos.txt",
    "https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareAdGuardHome.txt",
    "https://raw.githubusercontent.com/laylavish/uBlockOrigin-HUGE-AI-Blocklist/main/noai_hosts.txt",
    "https://raw.githubusercontent.com/blocklistproject/Lists/refs/heads/master/smart-tv.txt",
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    "https://raw.githubusercontent.com/notracking/hosts-blocklists/master/hostnames.txt",
    "https://raw.githubusercontent.com/notracking/hosts-blocklists/master/domains.txt",
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt",
    # الرابط https://o0.pages.dev/Pro/1hosts هو غير متوفر أو يعطي خطأ 404 - يمكنك حذفه أو تعليقه مؤقتاً
    # "https://o0.pages.dev/Pro/1hosts"
]

domains = set()  # تجميع الدومينات بدون تكرار

for url in urls:
    try:
        print(f"Downloading: {url}")
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        lines = response.text.splitlines()
        for line in lines:
            line = line.strip()
            # تجاهل السطور الفارغة والتعليقات
            if line and not (line.startswith("#") or line.startswith("!")):
                domains.add(line)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# إنشاء مجلد data إذا لم يكن موجودًا
os.makedirs("data", exist_ok=True)

output_file = "data/unified_blocklist.txt"

# حفظ الدومينات بالترتيب الأبجدي في الملف
with open(output_file, "w", encoding="utf-8") as f:
    for domain in sorted(domains):
        f.write(domain + "\n")

print(f"\nSaved {len(domains)} domains to {output_file}")
