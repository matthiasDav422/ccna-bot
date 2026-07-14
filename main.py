import difflib

# 30 CCNA Q&A - Instant answers
CCNA_DATA = {
    "what layer of osi is a switch": "Layer 2",
    "what layer of osi is a router": "Layer 3", 
    "what layer of osi is a hub": "Layer 1",
    "what is the pdu at layer 3": "Packet",
    "what is the pdu at layer 2": "Frame",
    "what port does http use": "80",
    "what port does https use": "443",
    "what port does dns use": "53",
    "what port does ssh use": "22",
    "what port does ftp use": "21",
    "what protocol does ospf use": "IP Protocol 89",
    "what protocol does eigrp use": "IP Protocol 88",
    "what is the subnet mask for a /24 network": "255.255.255.0",
    "what is a private ip range": "192.168.0.0 to 192.168.255.255 and 10.0.0.0 to 10.255.255.255",
    "what does dhcp do": "Assigns IP addresses automatically",
    "what is the purpose of arp": "Maps IP address to MAC address",
    "what is the default administrative distance of ospf": "110",
    "what is the default administrative distance of eigrp": "90",
    "what is the default administrative distance of rip": "120",
    "is ospf a link state or distance vector protocol": "Link state",
    "is rip a link state or distance vector protocol": "Distance vector",
    "what command shows the routing table": "show ip route",
    "what command shows the running configuration": "show running-config",
    "what command shows the interface status": "show ip interface brief",
    "what command shows cdp neighbors": "show cdp neighbors",
    "what command saves the configuration": "copy running-config startup-config",
    "what is the default vlan": "VLAN 1",
    "what protocol prevents switching loops": "STP Spanning Tree Protocol",
    "what is nat used for": "Translates private IP to public IP",
    "what is an acl used for": "Filters traffic based on rules"
}

def find_answer(question):
    question = question.lower().strip()
    # Find closest match
    matches = difflib.get_close_matches(question, CCNA_DATA.keys(), n=1, cutoff=0.6)
    if matches:
        return CCNA_DATA[matches[0]]
    else:
        return "I don't know that one yet. Try asking about ports, commands, or OSI layers."

def main():
    print("--- CCNA BOT READY ---")
    print("Type 'exit' to quit\n")
    while True:
        user_q = input("Ask CCNA Question: ")
        if user_q.lower() == 'exit':
            break
        answer = find_answer(user_q)
        print(f"A: {answer}\n")

if __name__ == "__main__":
    main()