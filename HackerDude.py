# text based game where built in programs are used to hack imaginary websites for in game money to buy better stuff (eg. better proxies, vpn upgrade)
import os, time

clear = lambda: os.system('cls')
wallet = 0
bank = 1000
clear()
name = input('Create your username: ')
creditdebt = None
creditnum = None
VPNlvl = 0

def setup(name, wallet, bank):
    print(f'You have {wallet} money in your wallet.')
    print(f'You have {bank} money in your bank.')
    input('Press <ENTER> to continue...')
    clear()

def intro(name):
    print(f'Hello, {name}.')
    print(f'You are in the role of a freelance hacker. Each time you complete a job, you will get paid.')
    print(f'You can either withdraw that money for the physical stores, or use your bank account for online stores.')
    print('Bank details are randomly allocated at the start.')

def choose(name, bank, wallet, creditnum, creditdebt):
    creditnum = '9742-6828-7642-7946'
    creditdebt = 0
    print(f'Your credit card number is {creditnum}. This will automatically fill in for online shops.')
    input('Press <ENTER> to continue.')
    clear()
    lvl1(name, bank)

def lvl1(name, bank):
    print('You recieve an email enquiring about your service.\nIt says this:\n')
    print(f'Hi {name}!\n\nI saw your ad and I have an offer. I will pay you £300 to test my website security. The web address is https://charlienet.com and the port to use is 80.\n\n-Charlie.')
    input('\n\nPress <ENTER> to begin... ')
    clear()
    hack_tutorial(name, bank)

def hack_tutorial(name, bank):

    while True:
        print('While using new software, the first thing you should do is type "programname.help". Try typing "datadump.help".\n\n')
        cmd = input('>>> ')
        if cmd.lower() == 'datadump.help':
            clear()
            break
        else:
            clear()

    while True:
        print('Next, you must choose the mode. Type "datadump.SQLi".\n\n')
        cmd = input('>>> ')
        if cmd.lower() == 'datadump.sqli':
            clear()
            break
        else:
            clear()

    while True:
        print('Now enter the web address of your target in this format:\nhttps://charlienet.com:80\nThe port will not always be so easy to gain but it was provided in the email.\n\n')
        cmd = input('>>> ')
        if  cmd.lower() == 'https://charlienet.com:80':
            clear()
            break
        else:
            clear()
    print('Now just watch the magic happen...')
    time.sleep(1)
    print('Username: Charlie0283\nPassword: WellDone123!')
    print('\n\nNow that your first job is complete, send Charlie the account details and collect your money')
    clear()
    time.sleep(2)
    print(f'Hi Charie.\n\nYour website is not very safe. The details for your account:\nUsername: Charlie0283\nPassword: WellDone123!\n\n-{name}.')
    input('Press <ENTER> to continue...')
    clear()
    print('You collected £300!')
    bank += 300
    print(f'You now have {bank} money!')
    shop_tutorial(bank, name, creditdebt, creditnum)

def shop_tutorial(bank, name, creditdebt, creditnum, VPNlvl):
    clear()
    print('Welcome to the shop!')
    print("This tutorial teaches you how to buy upgrades.\n Let's buy a VPN.")
    print('\n\n[1] VPN (Level 1): £25\n[2] Proxies (Level 1: £100)\n[3] Toolkit (Level 2): £1000')
    while True:
        print('\nType "1".')
        cmd = input('>>> ')
        if cmd = '1':
            clear()
            break
        else:
            clear()
    VPNlvl +=1
    print('Higher VPN level = lower chance of being caught (Only useful in illegal jobs).')
    menu()

def menu():
    pass    # all options (shop, exit, next level)

setup(name, wallet, bank)
intro(name)
choose(name, bank, wallet, creditnum, creditdebt)