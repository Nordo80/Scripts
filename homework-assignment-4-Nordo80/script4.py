sudo iptables -A OUTPUT -p tcp -d 104.244.40.0/21 -j DROP #by using iptable, block the twitter
sudo iptables -A OUTPUT -p tcp -d www.twitter.com -j DROP #by using iptable, block the twitter
sudo iptables -A OUTPUT -p tcp -d twitter.com -j DROP #by using iptable, block the twitter
sudo iptables-save # save
sudo iptables -L # pokazat chto v banje

host -t a website # uznajesh ip saita
whois website uzajew # uznajew CIDR kotorqi potom kidajew v iptables
