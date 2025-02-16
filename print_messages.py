# import logging
# from colorama import init, Fore, Back, Style, Cursor
# import time

# class PrintMessage:
#     def __init__(self, port: int, host :str = 'localhost', debug: bool= False) -> None:
#         self.port: int = port
#         self.debug: bool = debug
#         self.host: str = host
#         self.logo: str = Fore.LIGHTRED_EX + f'''
# 🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊 🌱  🍊 🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊

#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⢀⣤⣶⣶⣶⣶⣤⡀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⡏⠙⢿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⡿⠋⠙⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⣴⣶⣦⡀⠸⣿⣿⣿⣿⣿⣿⠇⢀⣴⣶⣦⣀⠙⢿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⠀⠀⠀⠙⢿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠹⣿⣿⡿⠋⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠏⠀⣴⣿⣿⣿⣿⣷⡀⢿⣿⣿⣿⣿⡟⢀⣾⣿⣿⣿⣿⣧⡀⠹⣿⣿⣿
#         ⣿⣿⣿⣿⠀⠀⠀⠀⠈⢻⣧⠀⠀⠀⠀⠀⠀⠀⢀⣿⠋⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠏⠀⠸⣿⣿⣿⣿⣿⣿⣷⡘⣿⣿⣿⣿⢁⣾⣿⣿⣿⣿⣿⣿⠇⠀⠹⣿⣿
#         ⣿⡇⠙⢿⣦⡀⠀⠀⠀⠀⣹⣷⣤⠴⠶⠶⢤⣤⣿⡁⠀⠀⠀⠀⢀⣠⡿⠛⢹⣿⣿⡏⠀⢀⣀⡈⠙⠻⢿⣿⣿⣿⣷⣹⣿⣿⣯⣾⣿⣿⣿⡿⠟⠋⢁⣀⡀⠀⢹⣿
#         ⣿⡇⠀⠀⠈⠻⣦⡀⣠⡾⠋⠁⠀⣀⣤⣄⠀⠀⠙⠻⣦⡀⢀⣴⠿⠋⠀⠀⢸⣿⣿⠁⢠⣿⣿⣿⣿⣷⣶⣬⣝⣻⣿⠟⠋⠙⠻⣿⣟⣫⣥⣶⣶⣿⣿⣿⣿⡄⠈⢿
#         ⣿⡇⠀⠀⠀⠀⠈⠻⣯⡀⠀⣠⡾⠋⠁⠙⢿⣦⡀⠀⢈⣿⠟⠁⠀⠀⠀⠀⢸⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿
#         ⣿⡇⠀⠀⠀⠀⠀⠀⠙⢿⣾⠋⠀⠀⠀⠀⠀⠙⢷⣴⠟⠁⠀⠀⠀⠀⠀⠀⣼⣿⣿⡀⠘⣿⣿⣿⣿⠿⠟⢛⣯⣿⣿⣦⣄⣠⣴⣿⣿⣝⡛⠿⢿⣿⣿⣿⣿⠃⢀⣿
#         ⣿⣷⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣇⠀⠈⠉⢁⣠⣴⣾⣿⣿⣿⡿⣹⣿⣿⣟⢿⣿⣿⣿⣷⣦⣄⡈⠉⠁⠀⣸⣿
#         ⣿⣿⣇⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣆⠀⢰⣿⣿⣿⣿⣿⣿⡿⢡⣿⣿⣿⣿⡈⢿⣿⣿⣿⣿⣿⣿⡆⠀⣰⣿⣿
#         ⣿⣿⣿⣆⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣆⠈⠻⣿⣿⣿⣿⡿⠁⣾⣿⣿⣿⣿⣧⠈⢿⣿⣿⣿⣿⡟⠁⣰⣿⣿⣿
#         ⣿⣿⣿⣿⣷⣄⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⠛⠿⠟⠁⢸⣿⣿⣿⣿⣿⣿⡆⠈⠻⠿⠟⠉⣠⣾⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣷⣤⣘⣧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣃⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠈⠛⠿⠿⠿⠿⠛⠁⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿
#         ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
#         '''

#         self.info = Fore.WHITE + f'''
#                    ╔╦╗╔═╗╔╗╔╔═╗╔═╗╦═╗╦╔╗╔╔═╗  ╦ ╦╔═╗  ┬
#                     ║ ╠═╣║║║║ ╦║╣ ╠╦╝║║║║║╣   ║ ║╠═╝  │
#                     ╩ ╩ ╩╝╚╝╚═╝╚═╝╩╚═╩╝╚╝╚═╝  ╚═╝╩    o

#                     DEBUGGING: {self.debug}
#                     Server sprouted @ {self.host}:{self.port}
#                     Press Ctrl+C to stop the server


# 🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊 🌱  🍊 🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊
#         '''

#     def print_success(self):
#         print(self.logo)
#         time.sleep(0.3)
#         print(self.info)

#     def print_debug(self, message):
#         print(Fore.CYAN + message + Style.RESET_ALL)


# helpers.py

import time
import logging
from colorama import init, Fore, Back, Style, Cursor

def print_logo():
    logo = Fore.LIGHTRED_EX + '''
🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊 🌱  🍊 🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊

        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⢀⣤⣶⣶⣶⣶⣤⡀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⡏⠙⢿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⡿⠋⠙⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⢀⣴⣶⣦⡀⠸⣿⣿⣿⣿⣿⣿⠇⢀⣴⣶⣦⣀⠙⢿⣿⣿⣿⣿
        ⣿⣿⣿⣿⠀⠀⠀⠙⢿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠹⣿⣿⡿⠋⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠏⠀⣴⣿⣿⣿⣿⣷⡀⢿⣿⣿⣿⣿⡟⢀⣾⣿⣿⣿⣿⣧⡀⠹⣿⣿⣿
        ⣿⣿⣿⣿⠀⠀⠀⠀⠈⢻⣧⠀⠀⠀⠀⠀⠀⠀⢀⣿⠋⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠏⠀⠸⣿⣿⣿⣿⣿⣿⣷⡘⣿⣿⣿⣿⢁⣾⣿⣿⣿⣿⣿⣿⠇⠀⠹⣿⣿
        ⣿⡇⠙⢿⣦⡀⠀⠀⠀⠀⣹⣷⣤⠴⠶⠶⢤⣤⣿⡁⠀⠀⠀⠀⢀⣠⡿⠛⢹⣿⣿⡏⠀⢀⣀⡈⠙⠻⢿⣿⣿⣿⣷⣹⣿⣿⣯⣾⣿⣿⣿⡿⠟⠋⢁⣀⡀⠀⢹⣿
        ⣿⡇⠀⠀⠈⠻⣦⡀⣠⡾⠋⠁⠀⣀⣤⣄⠀⠀⠙⠻⣦⡀⢀⣴⠿⠋⠀⠀⢸⣿⣿⠁⢠⣿⣿⣿⣿⣷⣶⣬⣝⣻⣿⠟⠋⠙⠻⣿⣟⣫⣥⣶⣶⣿⣿⣿⣿⡄⠈⢿
        ⣿⡇⠀⠀⠀⠀⠈⠻⣯⡀⠀⣠⡾⠋⠁⠙⢿⣦⡀⠀⢈⣿⠟⠁⠀⠀⠀⠀⢸⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣿
        ⣿⡇⠀⠀⠀⠀⠀⠀⠙⢿⣾⠋⠀⠀⠀⠀⠀⠙⢷⣴⠟⠁⠀⠀⠀⠀⠀⠀⣼⣿⣿⡀⠘⣿⣿⣿⣿⠿⠟⢛⣯⣿⣿⣦⣄⣠⣴⣿⣿⣝⡛⠿⢿⣿⣿⣿⣿⠃⢀⣿
        ⣿⣷⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣇⠀⠈⠉⢁⣠⣴⣾⣿⣿⣿⡿⣹⣿⣿⣟⢿⣿⣿⣿⣷⣦⣄⡈⠉⠁⠀⣸⣿
        ⣿⣿⣇⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣆⠀⢰⣿⣿⣿⣿⣿⣿⡿⢡⣿⣿⣿⣿⡈⢿⣿⣿⣿⣿⣿⣿⡆⠀⣰⣿⣿
        ⣿⣿⣿⣆⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣆⠈⠻⣿⣿⣿⣿⡿⠁⣾⣿⣿⣿⣿⣧⠈⢿⣿⣿⣿⣿⡟⠁⣰⣿⣿⣿
        ⣿⣿⣿⣿⣷⣄⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠈⠛⠿⠟⠁⢸⣿⣿⣿⣿⣿⣿⡆⠈⠻⠿⠟⠉⣠⣾⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣷⣤⣘⣧⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣃⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⡀⠀⠈⠛⠿⠿⠿⠿⠛⠁⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣤⣤⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    '''
    print(logo)

def print_info(port, host, debug):
    info = Fore.WHITE + f'''
                   ╔╦╗╔═╗╔╗╔╔═╗╔═╗╦═╗╦╔╗╔╔═╗  ╦ ╦╔═╗  ┬
                    ║ ╠═╣║║║║ ╦║╣ ╠╦╝║║║║║╣   ║ ║╠═╝  │
                    ╩ ╩ ╩╝╚╝╚═╝╚═╝╩╚═╩╝╚╝╚═╝  ╚═╝╩    o

                    DEBUGGING: {debug}
                    Server sprouted @ {host}:{port}
                    Press Ctrl+C to stop the server


🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊 🌱  🍊 🌱  🍊  🌱  🍊  🌱  🍊  🌱  🍊
    '''
    print(info)

def print_success(port, host, debug):
    print_logo()
    time.sleep(0.3)
    print_info(port, host, debug)

def print_debug(message):
    print(Fore.CYAN + message + Style.RESET_ALL)
