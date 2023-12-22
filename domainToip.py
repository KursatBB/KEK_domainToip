import socket
import xlsxwriter
import argparse

parser = argparse.ArgumentParser(prog="KEK_domainToip", description="Takes domain names and gets their IPs.")
parser.add_argument("-f", "--filename", help="The filename/filepath to get domains from", required=True)
parser.add_argument("-o", "--output", help="The output path and name of the IPs, this will automatically create a txt file. dont write extension", required=True)
parser.add_argument("-x", "--excel", help="If you want to excel output", action="store_true")
args = parser.parse_args()

xlsx_output_file = args.output + ".xlsx"
txt_output_file=args.output + ".txt"
try:
    workbook = xlsxwriter.Workbook(xlsx_output_file)
    worksheet = workbook.add_worksheet()
    if args.excel:
        worksheet.write('A1', "IP's")
        worksheet.write('B1', "DOMAINS")
        worksheet.center_horizontally()
        worksheet.center_vertically()
except:
    pass

ipcount = 2

domainFile = args.filename

def get_ips():
    with open(domainFile, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for i in lines:
            i = i.strip()
            try:
                ip = socket.gethostbyname(i)
                write_ips(ip, i)
                if args.excel:
                    write_ips_to_excel(ip, i)
            except socket.gaierror:
                print(i + " Domaininin ipsine ulaşılamıyor.")
        f.close()
    if args.excel:
        worksheet.add_table(f"A1:B{ipcount}")

def write_ips(ip, domain):
    with open(txt_output_file, "a", encoding="utf-8") as f:
        f.write(ip + f"  {domain}\n")     

def write_ips_to_excel(ip, domain):
    global ipcount
    worksheet.write(f"A{ipcount}", ip)
    worksheet.write(f"B{ipcount}", domain)
    ipcount = ipcount + 1

if __name__ == "__main__":
    get_ips()
    if args.excel:
        workbook.close()
