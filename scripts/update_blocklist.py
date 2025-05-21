import requests
import os

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
    "https://adguardteam.github.io/HostlistsRegistry/assets/filter_1.txt"
]

domains = set()

for url in urls:
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        lines = r.text.splitlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                domains.add(line)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

if not os.path.exists("data"):
    os.makedirs("data")

output_path = "data/unified_blocklist.txt"

with open(output_path, "w", encoding="utf-8") as f:
    for domain in sorted(domains):
        f.write(domain + "\n")

print(f"Saved {len(domains)} domains to {output_path}")
