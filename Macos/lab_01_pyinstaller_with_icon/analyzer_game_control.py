import os
import xlrd
import random
import collections
import sys
import copy
import json
from datetime import date
import datetime
import argparse
import numpy as np
import time

import collections

# Préparer des cartes:  Karten vorbereiten:     カードを準備する:   카드 준비
# Une card set: Il a 52 cardes, sans joker. (S1-S13,H1-H13,C1-C13,D1-D13)
def card_game_preparer_les_cartes_by_numbers_of_card_set(input_number_of_card_set):
    les_cartes_list = []
    for _ in range(input_number_of_card_set):
        #S, H, D, C
        for i in range(1, 14):
            tem_str = "S"+str(i)
            les_cartes_list.append(tem_str)
            tem_str = "H"+str(i)
            les_cartes_list.append(tem_str)
            tem_str = "D"+str(i)
            les_cartes_list.append(tem_str)
            tem_str = "C"+str(i)
            les_cartes_list.append(tem_str)
    return_list = les_cartes_list.copy()
    return return_list

def __card_game_afficher_les_cartes_chinoise(input_list):
    return_list = []
    for any_carte in input_list:
        tem_carte = ""
        if any_carte[0] == "S":
            tem_carte = "黑桃" + any_carte[1:]
            return_list.append(tem_carte)
        elif any_carte[0] == "H":
            tem_carte = "紅心" + any_carte[1:]
            return_list.append(tem_carte)
        elif any_carte[0] == "D":
            tem_carte = "方塊" + any_carte[1:]
            return_list.append(tem_carte)
        elif any_carte[0] == "C":
            tem_carte = "梅花" + any_carte[1:]
            return_list.append(tem_carte)
        else:
            print(
                "[afficher_list_cartes_chinoise][Error]: We don't have this cartes types! %s" % any_carte)
            return False

    return return_list

def card_game_afficher_le_table_chinoise_v1(input_list_list, input_runs=99999999):
    msg = "第[%d]局的盤面表現:\n----------------------------------------------------------------------\n" % input_runs
    for index, tem_list in enumerate(input_list_list):
        if index == 0:
            les_cartes = __card_game_afficher_les_cartes_chinoise(tem_list)
            msg += "[莊家]:\t\t\t%s\n" % les_cartes
        elif index == 1:
            les_cartes = __card_game_afficher_les_cartes_chinoise(tem_list)
            msg += "[天 ]:\t\t\t%s\n" % les_cartes
        elif index == 2:
            les_cartes = __card_game_afficher_les_cartes_chinoise(tem_list)
            msg += "[地 ]:\t\t\t%s\n" % les_cartes
        elif index == 3:
            les_cartes = __card_game_afficher_les_cartes_chinoise(tem_list)
            msg += "[玄 ]:\t\t\t%s\n" % les_cartes
        elif index == 4:
            les_cartes = __card_game_afficher_les_cartes_chinoise(tem_list)
            msg += "[黃 ]:\t\t\t%s\n" % les_cartes
        else:
            print(
                "[afficher_le_table_chinoise_v1][Error]: the input_list_list index over-limit %d" % index)
    return msg



class analyzer_weight_agent():
    def __init__(self):
        self.control_name = "analyzer_weight_agent"
        self.target_weight_list = []
        self.target_numbers = 0
        self.target_weight_dictionary = {}
        self.target_weight_inverse_dictionary = {}

        # avec the medhod pick_by_random_pop
        self.target_remain_weight_list = []

    def initial_by_excel(self,input_excel_name,input_table_name,read_length):
        
        # Set norm:
        self.control_name = input_table_name
        # Set numbers:
        self.target_numbers = read_length
        # Ouverte workbook
        workbook = xlrd.open_workbook(input_excel_name)
        # Ouverte sheet
        sheet = workbook.sheet_by_name(input_table_name)
        # Lire le values
        for v in range(read_length):
            # Set weight_list
            self.target_weight_list.append(int(float(sheet.cell_value(v+1,2))))
            
        # Set dictionary:
        self.target_weight_dictionary  = { index: str(sheet.cell_value(index+1,1)) for index in range(read_length) }
        self.target_weight_inverse_dictionary = {v: k for k, v in self.target_weight_dictionary.items()}

        # Set remain_weight_list:
        for index, weight_value in enumerate(self.target_weight_list):
            for _ in range(weight_value):
                self.target_remain_weight_list.append(self.target_weight_dictionary[index])
        
    def initial_by_list(self,input_list):

        # Set norm:
        self.control_name = "analyzer_weight_agent_initial_by_input_list:"

        # Set numbers:
        self.target_numbers = len(input_list)

        # Lire les values:
        self.target_weight_list  = collections.Counter(input_list)
        self.target_weight_list  = [key for key in self.target_weight_list]
        self.target_weight_list.sort()
     

        # Set Dictionary
        
        self.target_weight_dictionary = {index: key for index, key in enumerate(self.target_weight_list)}
        self.target_weight_inverse_dictionary = {v: k for k, v in self.target_weight_dictionary.items()}
        
        # Set Conteneur:
        # Set remain_weight_list:
        self.target_remain_weight_list = input_list.copy()

    def les_formation(self):
        msg  = "[%s]:\n"%self.control_name
        msg += "target_numbers                         = %d\n"%self.target_numbers
        msg += "target_weight_list                     = %s\n"%self.target_weight_list
        msg += "target_weight_dictionary               = %s\n"%self.target_weight_dictionary
        msg += "target_weight_inverse_dictionary       = %s\n"%self.target_weight_inverse_dictionary
        msg += "target_remain_weight_list              = %s\n"%self.target_remain_weight_list
        return msg

    def pick_by_random_pop(self):
        msg  = "Run [pick_by_random_pop]:   " 
        # Random Pick
        pick_target = random.choice(self.target_remain_weight_list)
        # Remove picked target
        self.target_remain_weight_list.remove(pick_target)
            
        msg += "Pick:  %s\n"%pick_target
        msg += self.les_formation()

        # Check the remain_list is empty or not
        if len(self.target_remain_weight_list) == 0:
            msg += "list empty: Reset !  "
            for index, weight_value in enumerate(self.target_weight_list):
                for _ in range(weight_value):
                    self.target_remain_weight_list.append(self.target_weight_dictionary[index])
        else:
            pass
            
        return pick_target, msg

    def obtenir_remain_weight_size(self):
        return len(self.target_remain_weight_list)
        
    def afficher_remain_weight_list(self):
        msg = "Current weight_list:\n\n"
        msg += "%s\n\n"%self.target_remain_weight_list
        return msg
