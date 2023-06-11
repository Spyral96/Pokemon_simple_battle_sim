# -*- coding: utf-8 -*-
"""
Created on Wed May 31 01:57:26 2023

@author: Dan
"""
###### Imports/Requests #######
import pandas as pd
import requests
###############################
#begining 
#user types pokemon in
try: 
    pokemon = input("Type in a Pokemon to see it's stats. Examples: (Pikachu,Muk,Scizor):\n").lower()
    
    
    
    
    
    ######### raw data/json #######
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    
    pokemon_raw_data = response.json()
    
    ########   Variables      #######
    
    base_hp = pokemon_raw_data['stats'][0]["base_stat"]
    
    base_att = pokemon_raw_data['stats'][1]["base_stat"]
    
    base_def = pokemon_raw_data['stats'][2]["base_stat"]
    
    base_spa = pokemon_raw_data['stats'][3]["base_stat"]
    
    base_spd = pokemon_raw_data['stats'][4]["base_stat"]
    
    base_speed = pokemon_raw_data['stats'][5]["base_stat"]
    
    poke_name = pokemon_raw_data ["name"]
    
    type_uncleaned_data = pokemon_raw_data['types'][0:]
    
    type_names = []
    #adding stats for base stat total
    bst = base_hp + base_att + base_def + base_spa + base_spd + base_speed 
    
    dex_num = pokemon_raw_data['id']
    
    ######nes for loop
    for entry in type_uncleaned_data:
        type_name = entry['type']['name']
        type_names.append(type_name)
    
    #creating intail blank move list to soon be appended
    movesets = []
    
    #creating specific data location for moveset
    raw_moveset = pokemon_raw_data['moves'] 
    
    #looping through moveset and appending to movesets list
    for dictionary in raw_moveset:
        moveset = dictionary['move']['name']
        movesets.append(moveset)
    
    
     #fetching specific move descriptions 
    #creating url list for all moves
    moves_list_url=[]
    for dictionary in raw_moveset:
        moveset_url = dictionary['move']['url']
        moves_list_url.append(moveset_url)
    
    #print(moves_list_url)
    
    #looping each url to be insert in requesting
    #making json list to put in dataframe
    # =============================================================================
    #     move_description = []
    #     for url in moves_list_url:
    #         second_respnse = requests.get(moveset_url)
    #         pokemon_moveset_specific_data = second_respnse.json()
    #         move_description.append(pokemon_moveset_specific_data)
    #     pokemon_moveset_specific_data = pd.DataFrame(move_description)
    # =============================================================================
    # =============================================================================
    # move_description = []
    # for url in moves_list_url:
    #     second_respnse = requests.get(url)
    #     pokemon_moveset_specific_data = second_respnse.json()
    #     move_description.append(pokemon_moveset_specific_data)
    # #move varaibles
    # for move in move_description:
    # 
    #     move_accuracy = move_description["accuracy"] 
    #     move_power = move_description["power"]
    #     change_num = move_description["stat_changes"]["change"]
    #         if change_num = "":
    #             change_num = "N/A"
    #     
    #    
    # 
    #     
    #     
    #     
    #     accuracy =[]    
    #     accuracy.append(str(move_accuracy))
    #     
    #     power = []
    #     power.append(move_power)
    #     
    #     stat_change_num = []
    #     stat_change_num.append(change_num)
    #     
    #     stat_change = []
    #     stat_change.append(change_name)
    #     
    #     move_type = []
    #     move_type.append(move_type_name)
    # =============================================================================
    # =============================================================================
    #     for url in moves_list_url
    #         second_respnse = requests.get(url)
    #         pokemon_moveset_specific_data = second_respnse.json()
    #    
    #         move_data = pd.DataFrame([pokemon_moveset_specific_data])
    #         move_data.append(move)
    #         print(moves)
    # =============================================================================
    ###########  Function         ############
    #BST
    def pokemon_descript():
         print("")
         print(pokemon.title())
         print(f"Pokedex Number: {dex_num}")
         print(f'\nBase Stats:\nHP: {base_hp}\nAttack: {base_att}\nDefense: {base_def}\nSpeaial Attack: {base_spa}\nSpecial Defense: {base_spd}\nSpeed: {base_speed}')
         for x in type_names:
             print("Type: " + x.title())
         print("Moveset:\n")
         
         for x in movesets:
            print(x.title() + '\n')
        
    #for move, acc, powe, statchange, stat_changenum, typing in zip(movesets, accuracy, power, stat_change, stat_change_num, move_type):
            #print(move.title() + "\nType: " + typing.title() + "\nAccuracy: " + str(acc) + "\nPower: " + str(powe) + "\n" + statchange.title() + ' increased or decreased by ' + str(stat_changenum))
    
    pokemon_descript()
    
   
    
        
        
        
    
    
    
        

except:
   print("Sorry that is not a pokemon or you have a mispelling.")
    




pokemon_panda = pd.DataFrame
