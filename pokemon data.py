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
#try: 
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



##############################This is where i started fixin things


# start 

 #fetching specific move descriptions 
#creating url list for all moves (Linking to a different api)
moves_list_url=[]


#looping throuugh
for dictionary in raw_moveset: 
    moveset_url = dictionary['move']['url']
    moves_list_url.append(moveset_url)

#print(moves_list_url)


#looping each url to be insert in requesting
#making json list to put in dataframe
move_description = []
for url in moves_list_url:
         second_respnse = requests.get(url)
         pokemon_moveset_specific_data = second_respnse.json()
         move_description.append(pokemon_moveset_specific_data)
         
#just made the a dictionary for each moves' descriptions on "movesets"         
         
#fetching our values from multiple json dictionaries (move_description)

#making list for each 

move_power = []
move_accuracy = []
effect_entry = []
move_type = []
damage_type = []


#looping through dictionries json values and adding them to blank lists
for move_desc in move_description:
    damage_type.append(move_desc['damage_class']['name'])
    move_type.append(move_desc['type']['name'])
    
    effect_entries = move_desc['effect_entries']
    if effect_entries:
        effect_entry.append(effect_entries[0]['short_effect'])
    else:
        effect_entry.append("N/A")
    
    
    #if power has no value!
    if move_desc['power'] is None:
        move_desc['power'] = "N/A"
        move_power.append(move_desc['power'])
    else:
        move_power.append(move_desc['power'])
        
    #if accuracy has no value
    if move_desc['accuracy'] is None:
        move_desc['accuracy'] = "N/A"
        move_accuracy.append(move_desc['accuracy'])
    
    else:
        move_accuracy.append(move_desc['accuracy'])

#making a dictionary with the values(lists(line 95-99)) i want to turn it into data frame

move_detail_dict = { 'move_powers':move_power,
                            'move_accuracys':move_accuracy,
                            'effect_entrys': effect_entry,
                            'move_types': move_type,
                            'damage_types':damage_type
}

move_df = pd.DataFrame(move_detail_dict,columns= ['move_powers','move_accuracys','effect_entrys','move_types','damage_types' ])

print(move_df)

    

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
     
     for moves in movesets:
        print(moves.title() + '\n')
    


        
#except:
   #print("Sorry that is not a pokemon or you have a mispelling.")
    
